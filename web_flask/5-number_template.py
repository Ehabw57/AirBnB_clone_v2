#!/usr/bin/python3
"""A module to start a flask app on all actiove adresses"""
from flask import Flask, render_template


app = Flask(__name__)
app.strict_slashes = False


@app.route('/')
def hello():
    return b'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    return b'HBNB'


@app.route('/c/<string:text>')
def c(text):
    text = text.replace('_', ' ')
    return 'C {}'.format(text)


@app.route('/python/<string:text>')
@app.route('/python/')
def python(text="is cool"):
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>')
def number(n):
    return f'{n} is a number'


@app.route('/number_template/<int:n>')
def number_template(n):
    return render_template('5-number.html', number=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
