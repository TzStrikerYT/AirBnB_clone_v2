#!/usr/bin/python3

from flask import Flask, render_template
import models
from models.state import State
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def kill(order):
    """ Close DB session """
    models.storage.close()


@app.route("/states", defaults={"id": None})
@app.route("/states/<id>")
def states(id):
    """ route to list of states """
    s_list = None
    res = s_list

    if not id:
        s_list = list(models.storage.all(State).values())
    else:
        s_list = models.storage.all(State)
        key = "State.{}".format(id)

        if key in s_list:
            res = s_list[key]
        else:
            res = None
        s_list = []
    return render_template("9-states.html", **locals())

if __name__ == "__main__":
    models.storage.reload()
    app.run("0.0.0.0", 5000)
