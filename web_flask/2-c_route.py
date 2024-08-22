#!/usr/bin/python3
"""A module to start a flask app on all actiove adresses"""
from flask import Flask


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


if __name__ == '__main__':
    app.run(host='0.0.0.0')
