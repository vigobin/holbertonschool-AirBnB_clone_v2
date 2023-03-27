#!/usr/bin/python3
"""List of states"""
from flask import Flask, request, render_template
from markupsafe import escape
from models import storage

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_state():
    """List the cities by state"""
    states = storage.all('State')
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def teardown(sql):
    """Remove current SQL Alchemy session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
