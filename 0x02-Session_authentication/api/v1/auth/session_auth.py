#!/usr/bin/env python3
""" Sessions Auth Module"""
from api.v1.auth.auth import Auth
import uuid


class SessionAuth(Auth):
    """ Session Auth class"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """ Creates Session ID for user_id"""
        if user_id is None or not isinstance(user_id, str):
            return None

        self.session_id = str(uuid.uuid4())
        self.user_id_by_session_id[self.session_id] = user_id
        return self.session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """ return User ID based on Session ID"""
        if session_id is None or not isinstance(session_id, str):
            return None

        return self.user_id_by_session_id.get(session_id)
