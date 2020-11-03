#!/usr/bin/env python3

"""
Template for authentication system
"""

from api.v1.auth.auth import Auth
import base64


class BasicAuth(Auth):
    """
    Extends Auth class
    """

    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """Returns the decoded value of a Base64
           string base64_authorization_header
        """
        if authorization_header is None or not isinstance(
                authorization_header, str):
            return None
        if 'Basic ' not in authorization_header:
            return None
        return authorization_header[6:]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """ Returns the Base64 part of the Authorization
            header for a Basic Authentification
        """
        if base64_authorization_header is None or not isinstance(
                base64_authorization_header, str):
            return None
        try:
            return base64.b64encode(base64.b64decode(
                base64_authorization_header)) == base64_authorization_header
        except Exception:
            return None
