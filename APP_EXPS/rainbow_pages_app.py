from flask import Flask
app = Flask(__name__)
'''
A simple Flask app that serves a rainbow-colored page connected to a home page. 
The home page has a button that links to the rainbow page, and the rainbow page 
has a button to go back home.
'''

@app.route('/')
def index():
    return '<a href="/rainbow"><button>Rainbow?</button></a>'

# make html that gives us a button to go back to the home page
go_to_home_html = '''
    <form action="/" >
        <input type="submit" value = "Go home"/> <!-- note "submit" type is a button -->
    </form>
'''

@app.route('/rainbow')
def rainbow():
    colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
    color_divs = []
    for i in range(1000):
        color = colors[i % len(colors)]
        div = '''<div style="background-color: {0};
                             color: white;
                             text-align: center;">
                     {1}
                 </div>'''.format(color, '*' * 100)
        color_divs.append(div)
    return '''
            <!DOCTYPE html>
            <html>
                <head>
                    <meta charset="utf-8">
                    <title>Rainbow</title>
                </head>
                <body>{0}</body>
            </html>
            '''.format('\n'.join(color_divs)) + go_to_home_html

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
