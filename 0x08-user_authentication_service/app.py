#!/usr/bin/env python3

"""Route module for the API
"""

from flask import Flask, jsonify, request, abort, redirect
from flask.helpers import make_response
from auth import Auth
from user import User


AUTH = Auth()

app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def welcome() -> str:
    """ GET /
    Return:
        welcome message
    """
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'], strict_slashes=False)
def register_users():
    """ POST /users
        JSON body:
            -email
            -password
       return:
       An endpoint to register a user
    """
    user_request = request.form
    try:
        user = AUTH.register_user(
            user_request['email'],
            user_request['password'])
        return jsonify({"email": user.email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login():
    """ POST /sessions
            - email
            - password
        Return:
            Data from "email" and "password" fields
    """
    user_request = request.form

    user_email = user_request.get('email', '')
    user_password = user_request.get('password', '')
    valid_log = AUTH.valid_login(user_email, user_password)
    if not valid_log:
        abort(401)
    response = make_response(
        jsonify({"email": user_email, "message": "logged in"}))
    response.set_cookie('session_id', AUTH.create_session(user_email))
    return response


@app.route('/sessions', methods=['DELETE'], strict_slashes=False)
def logout():
    """ DELETE /sessions
            - session_id
        Find user with requested session ID. If user exists,
        destroy session and redirect user to GET /
    """
    user_cookie = request.cookies.get("session_id")
    user = AUTH.get_user_from_session_id(user_cookie)
    if not user:
        abort(403)
    AUTH.destroy_session(user)
    return redirect('/')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
