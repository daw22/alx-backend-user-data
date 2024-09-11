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


@app.route('/sessions', methods=["POST"], strict_slashes=False)
def login():
    """
    Login route - creates and saves session id
                - sends back a cookie with session_id
    """
    try:
        email = flask.request.form["email"]
        password = flask.request.form["password"]
    except Exception:
        flask.abort(400)

    if not AUTH.valid_login(email, password):
        flask.abort(401)

    response = flask.jsonify({"email": email,
                              "message": "logged in"})
    session_id = AUTH.create_session(email)
    response.set_cookie("session_id", session_id)

    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
