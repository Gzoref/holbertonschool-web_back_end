#!/usr/bin/env python3

"""Route module for the API
"""

from flask import Flask, jsonify,request
from auth import Auth


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
        user = AUTH.register_user(user_request['email'], user_request['password'])
        return jsonify({"email": user.email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
