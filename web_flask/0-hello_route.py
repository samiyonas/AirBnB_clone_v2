#!/usr/bin/python3
""" First time using Flask, so Hello Flask! """
from flask import Flask


app = Flask(__name__)

@app.route("/", strict_slashes=False)
def hello():
    """ The home page(kind of) """
    return "Hello HBNB!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
