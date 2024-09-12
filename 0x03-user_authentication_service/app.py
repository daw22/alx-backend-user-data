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


@app.route('/logout', methods=['DELETE'], strict_slashes=False)
def logout():
    """
    logout route - finds users, deletes session_id and
    redirects to "GET/"
    """
    session_id = request.cookies.get('session_id', None)

    if session_id is None:
        flask.abort(403)

    user = AUTH.get_user_from_session_id(session_id)

    if user is None:
        flask.abort(403)

    AUTH.destroy_session(user.id)

    return flask.redirect("/")


@app.route('/profile', methods=['GET'])
def profile() -> str:
    """ If the user exist, respond with a 200 HTTP status and a JSON Payload
    Otherwise respond with a 403 HTTP status.
    """
    session_id = request.cookies.get("session_id", None)

    if session_id is None:
        abort(403)

    user = AUTH.get_user_from_session_id(session_id)

    if user is None:
        abort(403)

    msg = {"email": user.email}

    return jsonify(msg), 200


@app.route('/reset_password', methods=['POST'])
def reset_password() -> str:
    """If the email is not registered, respond with a 403 status code.
    Otherwise, generate a token and respond with a
    200 HTTP status and JSON Payload
    """
    try:
        email = request.form['email']
    except KeyError:
        abort(403)

    try:
        reset_token = AUTH.get_reset_password_token(email)
    except ValueError:
        abort(403)

    msg = {"email": email, "reset_token": reset_token}

    return jsonify(msg), 200


@app.route('/reset_password', methods=['PUT'])
def update_password() -> str:
    """ PUT /reset_password
    Updates password with reset token
    Return:
        - 400 if bad request
        - 403 if not valid reset token
        - 200 and JSON Payload if valid
    """
    try:
        email = request.form['email']
        reset_token = request.form['reset_token']
        new_password = request.form['new_password']
    except KeyError:
        abort(400)

    try:
        AUTH.update_password(reset_token, new_password)
    except ValueError:
        abort(403)

    msg = {"email": email, "message": "Password updated"}
    return jsonify(msg), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
