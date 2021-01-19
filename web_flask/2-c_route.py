#!/usr/bin/python3
"""script that starts a Flask web application:
The application listens on 0.0.0.0, port 5000.
Routes:
    '/': Displays 'Hello HBNB!'
    '/hbnb': Displays 'HBNB'
    '/c/<name>': Displays 'C {}'.name
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def home():
    """Displays 'Hello HBNB!'"""
    return "Hello HBNB!"

@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Displays 'HBNB'"""
    return "HBNB"

@app.route("/c/<name>", strict_slashes=False)
def c(name):
    """Displays 'C' {} name"""
    return "C {}".format(name.replace('_', ' '))

if __name__ == "__main__":
    app.run(host="0.0.0.0")
