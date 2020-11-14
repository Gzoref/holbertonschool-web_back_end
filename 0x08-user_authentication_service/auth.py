from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError
from db import DB
from user import User
import bcrypt
import uuid

""" Auth class to validate user attributes
"""


def _hash_password(password: str) -> str:
    """ Takes in a password and returns a salted hash.
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def _generate_uuid() -> str:
    """ Returns a string representation of a new UUID
    """
    return str(uuid.uuid4())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        """ Initailizes instance of DB
        """
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """ Returns a User object, or ValueError with a message
        """
        try:
            self._db.find_user_by(email=email)
            raise ValueError("User {} already exists.".format(email))
        except NoResultFound:
            hashed_password = _hash_password(password)
            new_user = self._db.add_user(email, hashed_password)
            return new_user

    def valid_login(self, email: str, password: str) -> bool:
        """ Tries to locate user by email and checks that
            password matches hashed password
        """
        try:
            user = self._db.find_user_by(email=email)
            if bcrypt.checkpw(password.encode('utf-8'), user.hashed_password):
                return True
        except NoResultFound:
            pass
        return False

    def create_session(self, email: str) -> str:
        """ Finds user by email, generates a UUID
            and stores it in database as the user's session_id
        """
        session_id = _generate_uuid()
        try:
            user = self._db.find_user_by(email=email)
            self._db.update_user(user.id, session_id=session_id)
            return session_id
        except NoResultFound:
            return None
