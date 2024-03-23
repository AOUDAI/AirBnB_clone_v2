#!/usr/bin/python3
""" Contains a simple flask web application"""

from flask import Flask, render_template

app = Flask(__name__)

app.url_map.strict_slashes = False
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True


@app.route("/")
def hello():
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    return "HBNB"


@app.route("/c/<text>")
def for_c(text):
    return f"C {text.replace('_', ' ')}"


@app.route('/python/<text>')
@app.route('/python')
def for_python(text='is cool'):
    return f"Python {text.replace('_', ' ')}"


@app.route('/number/<int:n>')
def is_number(n):
    return f"{n} is a number"


@app.route('/number_template/<int:n>')
def template_renderer(n):
    return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>')
def odd_or_even(n):
    return render_template('6-number_odd_or_even.html', number=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
