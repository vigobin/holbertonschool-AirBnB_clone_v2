#!/usr/bin/python3
"""Odd or even?"""
from flask import Flask, request, render_template
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


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text='is cool'):
    """display python"""
    return ('Python {}'.format(text.replace('_', ' ')))


@app.route('/number/<int:n>', strict_slashes=False)
def is_number(n):
    return ('{} is a number'.format(n))


@app.route('/number_template/<int:n>', strict_slashes=False)
def num_template(n=None):
    """number template"""
    if isinstance(n, int):
        return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_even(n=None):
    """number is odd or even"""
    if isinstance(n, int):
        if n % 2:
            o_e = "odd"
        else:
            o_e = "even"

    return render_template('6-number_odd_or_even.html', n=n, o_e=o_e)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
