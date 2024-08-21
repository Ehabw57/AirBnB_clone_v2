#!/usr/bin/python3
"""A module to start a flask app on all actiove adresses"""
from flask import Flask


app = Flask(__name__)
app.strict_slashes = False


@app.route('/')
def HelloHBN():
    return b'Hello HBNB!'


if __name__ == '__main__':
    app.run(host='0.0.0.0')
