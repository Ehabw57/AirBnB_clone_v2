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


@app.route('/states', strict_slashes=False)
def states_list():
    """Display an HTML page with a list of all states"""
    states = storage.all(State)
    return render_template('9-states.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def state_by_id(id):
    """Display an HTML page with a all citites of state"""
    state = storage.all(State).get(f"State.{id}")
    if state is not None:
        return render_template('9-states.html', state=state)
    else:
        return render_template('9-states.html')


if __name__ == '__main__':
    app.run('0.0.0.0')
