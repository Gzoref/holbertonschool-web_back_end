#!/usr/bin/env python3

"""
Template for authentication system
"""

from base64 import b64decode
from api.v1.auth.auth import Auth
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
