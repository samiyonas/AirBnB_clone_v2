#!/usr/bin/python3
""" script that starts a Flask web application """
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """ home page (kind of) """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ hbnb url """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text=None):
    """ C is fun """
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route("/python")
@app.route("/python/")
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    """ python is also cool """
    text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """ number only (integer) """
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """ show template only if n is integer """
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even(n):
    """ number odd or even """
    return render_template("6-number_odd_or_even.html", n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
