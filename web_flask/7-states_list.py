#!/usr/bin/python3
"""List of states"""
from flask import Flask, request, render_template
from markupsafe import escape
from models import storage

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def list_states():
    """List the states"""
    states = storage.all('State')

    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown(args):
    """Remove current SQL Alchemy session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
