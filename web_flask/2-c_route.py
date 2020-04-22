#!/usr/bin/python3
""" my first flask service """
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_flask():
    """ Return Hello HBNB """
    return "Hello HBNB!"


@app.route('/hbnb')
def hello_hbnb():
    """ Return HBNB """
    return "HBNB"


@app.route('/c/<text>')
def content(text):
    """ Return any text with C """
    content = str(text).replace("_", " ")
    return "C {}".format(escape(text))

if __name__ == "__main__":
    app.run("0.0.0.0", 5000)
