#!/usr/bin/python3
""" fetching data from the database """
from models import storage
from models.state import State
from flask import Flask, render_template


info = list(storage.all(State).values())
app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    """ list of states from database """
    states = sorted(info, key=lambda i: i.name)
    return render_template("7-states_list.html", states=states)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
