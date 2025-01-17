#!/usr/bin/python3
"""C is fun"""
from flask import Flask, request
from markupsafe import escape

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """route"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def Hbnb():
    """Display HBNB"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """Display C"""
    return ('C {}'.format(text.replace('_', ' ')))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
