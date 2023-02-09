#!/usr/bin/env python3
""" session auth database """

from api.v1.auth.session_exp_auth import SessionExpAuth


class SessionDBAuth(SessionExpAuth):
    def create_session(self, user_id=None):
        session_id = super().create_session(user_id)
        user_session = UserSession(user_id, session_id)
        return session_id
    
    def user_id_for_session_id(self, session_id=None):
        user_session = self.session.query(UserSession).filter_by(session_id=session_id).first()
        if user_session:
            return user_session.user_id
        return None