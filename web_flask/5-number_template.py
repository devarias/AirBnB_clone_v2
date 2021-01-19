#!/usr/bin/python3
"""script that starts a Flask web application:
The application listens on 0.0.0.0, port 5000.
Routes:
    '/': Displays 'Hello HBNB!'
    '/hbnb': Displays 'HBNB'
    '/c/<name>': Displays 'C {}'.name
    '/python/(<name>)':
        - Displays default: 'Python is cool'
        - Displays 'Python {}'.name
    '/number/<n>':
        - Only if n is an integer
        - Displays '{} is a number'.n
    '/number_template/<n>':
        - Only if n is an integer
        - Displays a HTML page
"""
from flask import Flask, render_template

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

@app.route("/python/", strict_slashes=False)
@app.route("/python/(<text>)", strict_slashes=False)
def python(text="is_cool"):
    """Displays 'Python' {} text"""
    return "Python {}".format(text.replace('_', ' '))

@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """Displays 'Python' {} text"""
    return "{} is a number".format(n)

@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """Displays 'Python' {} text"""
    return render_template('5-number.html', n=n)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
