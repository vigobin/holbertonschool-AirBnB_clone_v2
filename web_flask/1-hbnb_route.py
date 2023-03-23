#!/usr/bin/python3
"""HBNB"""
from flask import Flask, request
from markupsafe import escape

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """route"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def Hello():
    """Display HBNB"""
    return 'HBNB'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
