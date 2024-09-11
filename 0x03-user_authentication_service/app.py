#!/usr/bin/env python3
"""
flask app
"""
import flask


app = flask.Flask(__name__)


@app.route('/', methods=["GET"], strict_slashes=False)
def home():
    """
    basic route
    """
    return flask.jsonify({"message": "Bienvenue"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
