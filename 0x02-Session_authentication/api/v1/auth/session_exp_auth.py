#!/usr/bin/env python3
"""
Adds expiration date to Session ID
"""
from api.v1.auth.session_auth import SessionAuth
from os import getenv
from datetime import datetime, timedelta


class SessionExpAuth(SessionAuth):
    """
    Session authentication with expiration date
    """
    def __init__(self):
        """Initializers"""
        duration = getenv("SESSION_DURATION")
        try:
            duration = int(duration)
        except Exception:
            duration = 0
        self.session_duration = duration

    def create_session(self, user_id=None):
        """
        Create session with with expiration date
        """
        session_id = super().create_session(user_id)

        if session_id is None:
            return None
        session_dict = {
            "user_id": user_id,
            "created_at": datetime.now()
        }

        self.user_id_by_session_id[session_id] = session_dict

        return session_id

    def user_id_for_session_id(self, session_id=None):
        """
        get user fron session_id
        """
        if session_id is None:
            return None
        if session_id not in self.user_id_by_session_id.keys():
            return None
        session_dictionary = self.user_id_by_session_id.get(session_id)
        if session_dictionary is None:
            return None

        if self.session_duration <= 0:
            return session_dictionary.get('user_id')

        created_at = session_dictionary.get('created_at')

        if created_at is None:
            return None

        expired_time = created_at + timedelta(seconds=self.session_duration)

        if expired_time < datetime.now():
            return None

        return session_dictionary.get('user_id')
