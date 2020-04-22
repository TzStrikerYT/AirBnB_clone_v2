#!/usr/bin/python3
""" my first flask service """
from flask import Flask, render_template

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
    return "C {}".format(text.replace("_", " "))


@app.route('/python', defaults={"text": "is cool"}, strict_slashes=False)
@app.route('/python/<text>')
def content_py(text):
    """ Return any text with python """
    return "Python {}".format(text.replace("_", " "))


@app.route('/number/<int:n>')
def is_a_number(n):
    """ Return number only is a number """
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>')
def tmpl_number(n):
    """ Return template of number only is a number """
    return render_template("5-number.html", number=n)


@app.route('/number_odd_or_even/<int:n>')
def odd_even(n):
    """ Return template of number only is a number """
    return render_template("6-number_odd_or_even.html", number=n)

if __name__ == "__main__":
    app.run("0.0.0.0", 5000)
