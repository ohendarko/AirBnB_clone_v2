#!/usr/bin/python3
"""a script that starts a Flask web application"""
from flask import Flask
from markupsafe import escape
from flask import render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.teardown_appcontext
def remove_session(exc):
    """remove the current SQLAlchemy Session"""
    storage.close()


@app.route("/states", strict_slashes=False)
def states():
    """display a HTML page"""
    states = sorted(storage.all(State).values(), key=lambda s: s.name)
    return render_template('state.html', states=states)


@app.route("/states/<id>", strict_slashes=False)
def states_id():
    """display a HTML page"""
    state = storage.get(State, id)
    if not state:
        return "State not found ERROR!"

    cities = sorted(state.cities, key=lambda c: c.name)
    return render_template('state_id.html', state=state, cities=cities)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
