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


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    """display a HTML page"""
    states = storage.all("State")
    amenities = storage.all("Amenity")
    return render_template('10-hbnb_filters.html',
                           states=states, amenities=amenities)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
