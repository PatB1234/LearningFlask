from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# Ways to get data
@app.route('/user/<username>')
def data(username):

    return f'Hello, {escape(username)}'