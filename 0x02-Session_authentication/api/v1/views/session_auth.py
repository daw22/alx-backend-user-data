#!/usr/bin/env python3
"""
handles all routes for the Session authentication
"""
from api.v1.views import app_views
from flask import abort, jsonify, request
from models.user import User
from os import getenv


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login():
    """ POST /api/v1/auth_session/login
    Returns:
        - Authenticated user
    """
    email = request.form.get("email")
    if email is None:
        return jsonify({"error": "email missing"}), 400
    password = request.form.get("password")
    if password is None:
        return jsonify({"error": "password missing"}), 400
    try:
        users = User.search({"email": email})
    except Exception:
        return jsonify({"error": "no user found for this email"}), 404
    if users is None or users == []:
        return jsonify({"error": "no user found for this email"}), 404
    if not users[0].is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401
    session_name = getenv("SESSION_NAME")
    from api.v1.app import auth
    user = users[0]
    session_id = auth.create_session(user.id)
    response = jsonify(user.to_json())
    response.set_cookie(session_name, session_id)

    return response
