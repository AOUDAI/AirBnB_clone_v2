#!/usr/bin/python3
""" Contains a simple flask web application"""

from flask import Flask

app = Flask(__name__)

app.url_map.strict_slashes = False


@app.route("/")
def hello():
    return "Hello HNBN!"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)