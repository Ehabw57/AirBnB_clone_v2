#!/usr/bin/python3
"""Start a Flask web application listening on 0.0.0.0 port 5000"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    """Remove the current SQLAlchemy session"""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Display an HTML page with a list of all State objects in the database"""
    return render_template('7-states_list.html',
                           states=storage.all(State).values())


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """Display an HTML page with a list of all City objects by States"""
    states = storage.all(State).values()
    return render_template('8-cities_by_states.html', states=states)


if __name__ == '__main__':
    app.run('0.0.0.0')
