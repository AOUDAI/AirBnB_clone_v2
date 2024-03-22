#!/usr/bin/python3
""" Contains a simple flask web application"""

from flask import Flask

app = Flask(__name__)

app.url_map.strict_slashes = False


@app.route("/")
def hello():
    return "Hello HNBN!"


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


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
