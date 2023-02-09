#!/usr/bin/env python3
""" session expiration for session id """

from api.v1.auth.session_auth import SessionAuth
from os import getenv
from datetime import datetime, timedelta


class SessionExpAuth(SessionAuth):
    """ session expiration class """
    def __init__(self):
        """ initializes the SessionExp auth """
        super().__init__()
        self.session_duration = 0
        try:
            self.session_duration = int(getenv("SESSION_DURATION"))
        except ValueError:
            self.session_duration = 0

    def create_session(self, user_id=None):
        """ creates session """
        session_id = super().create_session(user_id)
        if session_id is None:
            return None

        self.user_id_by_session_id[session_id] = {
            'user_id': user_id,
            'created_at': datetime.now()
        }
        return session_id

    def user_id_for_session_id(self, session_id=None):
        """ gets user_id for session_id """
        if session_id is None:
            return None
        if session_id not in self.user_id_by_session_id:
            return None

        session = self.user_id_by_session_id[session_id]
        if self.session_duration <= 0:
            return session.get('user_id')

        created_at = session.get('created_at')
        if created_at is None:
            return None

        now = datetime.now()
        if created_at + timedelta(seconds=self.session_duration) < now:
            return None
        return session.get('user_id')
