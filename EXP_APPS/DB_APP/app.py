"""
HTML generated from data pulled from a database.

In this example we're pulling data from a simple sqlite3 database and
building an HTML template with it.

Requirements:
 * A database created with some data about authors inside.
"""
from flask import Flask, g, render_template, request
import config  # type: ignore
import os
import sqlite3

app = Flask(__name__)

def connect_db():
    return sqlite3.connect(config.DATABASE_NAME)

@app.before_request
def before_request():
    '''
    Connect to the database before the following any request is handled.
    Would enable multiple queries per request (or helper-function) if needed.
    '''
    g.db = connect_db()    

@app.route('/', methods=['POST', 'GET'])
def hello_world():
    if request.method == 'POST':
        # Clean and validate input
        author_name = request.form.get('author', '').strip()
        country_name = request.form.get('country', '').strip()
        
        # Skip if either field is empty after stripping
        if author_name and country_name:
            # Check if country exists, if not insert it
            country_cursor = g.db.execute('SELECT id FROM country WHERE name = ?', (country_name,))
            country_row = country_cursor.fetchone()
            
            if country_row is None:
                # Country doesn't exist, insert it
                g.db.execute('INSERT INTO country (name) VALUES (?)', (country_name,))
                g.db.commit()
                # Get the newly inserted country's id
                country_id = g.db.execute('SELECT last_insert_rowid()').fetchone()[0]
            else:
                # Country exists, use its id
                country_id = country_row[0]
            
            # Check if author already exists
            author_cursor = g.db.execute('SELECT id FROM author WHERE name = ?', (author_name,))
            author_row = author_cursor.fetchone()
            
            if author_row is None:
                # Author doesn't exist, insert them
                g.db.execute('INSERT INTO author (name, country_id) VALUES (?, ?)',
                             (author_name, country_id))
                g.db.commit()
            # If author exists, do nothing (skip insertion)
    
    cursor = g.db.execute('''
                        SELECT a.id, a.name, c.name as country
                        FROM author AS a
                            INNER JOIN country AS c ON a.country_id = c.id
                        ORDER BY a.name;
                        ''')
    authors = [dict(id=row[0], name=row[1], country=row[2]) for row in cursor.fetchall()]
    return render_template('authors_with_form.html', authors=authors)

if __name__ == '__main__':
	app.debug = True
	host = os.environ.get('IP', '0.0.0.0')
	port = int(os.environ.get('PORT', 8080))
	app.run(host=host, port=port)