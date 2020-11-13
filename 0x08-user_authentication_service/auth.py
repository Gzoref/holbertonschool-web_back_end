from db import DB
import bcrypt

""" Auth class to validate user attributes
"""

def _hash_password(password: str) -> str:
    """ Takes in a password and returns a salted hash.
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        """ Initailizes instance of DB
        """
        self._db = DB()

