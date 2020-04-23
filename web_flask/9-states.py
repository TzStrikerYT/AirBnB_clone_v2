#!/usr/bin/python3
from flask import Flask, render_template
import models
from models import State
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def closedb(foo):
    """kill session DB"""
    models.storage.close()


@app.route('/states', defaults={'id': None})
@app.route('/states/<id>')
def state(id):
    """ List of states """
    state = states = None
    if not id:
        states = list(models.storage.all(State).values())
    else:
        states = models.storage.all(State)
        key = "State.{}".format(id)
        if key in states:
            state = states[key]
        else:
            state = None
        states = []
    return render_template('9-states.html', **locals())


if __name__ == '__main__':
    models.storage.reload()
    app.run("0.0.0.0", 5000)
