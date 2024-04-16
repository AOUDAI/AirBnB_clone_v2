#!/usr/bin/python3
""" Flask web application that fetchs data from storage"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)

app.url_map.strict_slashes = False
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True


@app.route('/states_list')
def States():
    states = list(storage.all(State).values())
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def clearUp(exeption):
    """ clean things up after the app is completed"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
