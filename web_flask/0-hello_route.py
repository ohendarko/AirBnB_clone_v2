#!/usr/bin/python3
"""a script that starts a Flask web application"""
from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello_hbnb():
    """/: display “Hello HBNB!" """
    return "<p>Hello HBNB!</p>"
