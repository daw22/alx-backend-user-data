#!/usr/bin/env python3
"""
flask app
"""
import flask
from auth import Auth

app = flask.Flask(__name__)
AUTH = Auth()


@app.route('/', methods=["GET"], strict_slashes=False)
def home():
    """
    basic route
    """
    return flask.jsonify({"message": "Bienvenue"})


@app.route('/users', methods=["POST"], strict_slashes=False)
def register_user():
    """
    router to register a user
    """
    try:
        email = flask.request.form['email']
        password = flask.request.form['password']
    except KeyError:
        abort(400)

    try:
        new_user = AUTH.register_user(email, password)
    except ValueError:
        return flask.jsonify({"message": "email already registerd"})

    return flask.jsonify({"email": email, "message": "user created"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
