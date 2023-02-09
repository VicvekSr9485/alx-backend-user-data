#!/usr/bin/env python3
""" Sessions in database """

from models.base import Base


class UserSession(Base):
    """ user session class"""
    def __init__(self, *args: list, **kwargs: dict):
        """ init method for user session """
        super().__init__(*args, **kwargs)
        self.user_id = kwargs.user_id
        self.session_id = kwargs.session_id
