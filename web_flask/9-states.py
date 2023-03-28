#!/usr/bin/python3
"""States and State"""
from flask import Flask, request, render_template
from markupsafe import escape
from models import storage

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states(id=None):
    """List states"""
    states = storage.all('State')
    if id is not None:
        id = 'State.' + id
    return render_template('9-states.html', states=states, id=id)


def states():
    """List states"""
    states = storage.all('State')
    return render_template('9-states.html', states=states)


@app.teardown_appcontext
def teardown(args):
    """Remove current SQL Alchemy session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
