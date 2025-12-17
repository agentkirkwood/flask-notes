from collections import Counter
from flask import Flask, request
app = Flask(__name__)


def dict_to_html(d):
    return '<br>'.join('{0}: {1}'.format(k, d[k]) for k in sorted(d))


# Form page to submit text
@app.route('/')
def submission_page():
    return '''
        <form action="/word_counter" method='POST' >
            <input type="text" name="user_input" />
            <input type="submit" />
        </form>
        '''


# My word counter app
@app.route('/word_counter', methods=['POST'] )
def word_counter():
    text = str(request.form['user_input'])
    word_counts = Counter(text.lower().split())
    total_word_count = sum(word_counts.values())
    page = 'There are {0} <em>unique</em> words and {1} words total.<br><br>Individual word counts:<br> {2}<br><br><a href="/"><button>Return</button></a>'
    return page.format(len(word_counts), total_word_count, dict_to_html(word_counts))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
