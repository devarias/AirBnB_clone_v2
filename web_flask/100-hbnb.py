#!/usr/bin/python3
"""script that starts a Flask web application:
The application listens on 0.0.0.0, port 5000.
Routes:
    '/hbnb_filters': 'Display a HTML page: (inside the tag BODY)'
"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """'/hbnb_filters': 'Display a HTML page: (inside the tag BODY)'"""
    states = storage.all("State")
    am = storage.all("Amenity")
    place = storage.all("Place")
    return render_template('100-hbnb.html', states=states, amenities=am,
                           places=place)


@app.teardown_appcontext
def use_teardown(exception):
    """Remove the current SQLAlchemy Session"""
    storage.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
