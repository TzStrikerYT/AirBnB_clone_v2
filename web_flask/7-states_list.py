#!/usr/bin/python3

from flask import Flask, render_template
import models
from models.state import State
app = Flask(__name__)


@app.teardown_appcontext
def kill(order):
    """ Close DB session """
    models.storage.close()


@app.route("/states_list")
def states():
    """ route to list of states """
    s_list = list(models.storage.all(State).values())

    s_list.sort(key=lambda state: state.name)

    return render_template("7-states_list.html", s_list=s_list)

if __name__ == "__main__":
    models.storage.reload()
    app.run("0.0.0.0", 5000)
