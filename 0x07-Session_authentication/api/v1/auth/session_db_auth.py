#!/usr/bin/env python3
"""
Session databse class
"""

from flask import request
from typing import List
from os import environ, getenv
from datetime import datetime, timedelta, timedelta
from api.v1.auth.session_exp_auth import SessionExpAuth
from models.user_session import UserSession


class SessionDBAuth (SessionExpAuth):
    """
    SessionDBAuth class
    """

    def create_session(self, user_id=None):
        """ Generates a session ID
        """
        session_id = super().create_session(user_id)
        if user_id is None:
            return None
        user_session = UserSession(user_id=user_id, session_id=session_id)
        user_session.save()
        return session_id

    def user_id_for_session_id(self, session_id=None):
        """ Returns the User ID by requesting UserSession
            in the database based on session_id
        """
        is_valid_user = UserSession.search({'session_id': session_id})
        if not is_valid_user:
            return None

        is_valid_user = is_valid_user[0]

        start_time = is_valid_user.created_at
        time_delta = timedelta(seconds=self.session_duration)
        if (start_time + time_delta) < datetime.now():
            return None
        return is_valid_user.user_id

    def destroy_session(self, request=None):
        """ Destroys the UserSession based on session
            ID from the request cookie
        """
        cookie_data = self.session_cookie(request)
        if cookie_data is None:
            return False

        if not self.user_id_for_session_id(cookie_data):
            return False

        del self.user_id_by_session_id[cookie_data]
        return True