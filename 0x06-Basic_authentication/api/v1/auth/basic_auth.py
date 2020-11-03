#!/usr/bin/env python3

"""
Template for authentication system
"""

from typing import TypeVar
from base64 import b64decode
from api.v1.auth.auth import Auth
from models.user import User
import base64


class BasicAuth(Auth):
    """
    Extends Auth class
    """

    def extract_base64_authorization_header(self, auth_header: str) -> str:
        """Returns the decoded value of a Base64
           string base64_authorization_header
        """
        if auth_header is None or not isinstance(auth_header, str):
            return None
        if 'Basic ' not in auth_header:
            return None
        return auth_header[6:]

    def decode_base64_authorization_header(self, b64_auth_header: str) -> str:
        """ Returns the Base64 part of the Authorization
            header for a Basic Authentification
        """
        if b64_auth_header is None or not isinstance(b64_auth_header, str):
            return None
        try:
            b64 = base64.b64decode(b64_auth_header)
            b64_decode = b64.decode('utf-8')
        except Exception:
            return None
        return b64_decode

    def extract_user_credentials(
            self, decoded_b64_auth_header: str) -> (str, str):
        """ Returns the user email and password from the Base64 decoded value
        """
        if decoded_b64_auth_header is None or not isinstance(
            decoded_b64_auth_header, str)\
                or ':' not in decoded_b64_auth_header:
            return (None, None)
        return decoded_b64_auth_header.split(':')

    def user_object_from_credentials(
            self,
            user_email: str,
            user_pwd: str) -> TypeVar('User'):
        """ Returns the User instance based on his email and password.
        """
        if user_email is None or not isinstance(
                user_email, str) or user_pwd is None or not isinstance(
                user_pwd, str):
            return None
        users = User.search({'email': user_email})

        for user in users:
            if not user.is_valid_password(user_pwd):
                return None
            else:
                return user
