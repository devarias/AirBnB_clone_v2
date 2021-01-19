#!/usr/bin/python3
"""script that starts a Flask web application:
The application listens on 0.0.0.0, port 5000.
Routes:
    '/state_list': 'Display a HTML page: (inside the tag BODY)'
"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/state_list", strict_slashes=False)
def state_list():
    """'/state_list': 'Display a HTML page: (inside the tag BODY)'"""
    return render_template('7-states_list.html', states=storage.all(State))


@app.teardown_appcontext
def use_teardown(exception):
    """Remove the current SQLAlchemy Session"""
    storage.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0")
