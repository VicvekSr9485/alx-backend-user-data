#!/usr/bin/env python3
""" basic authentication provider """

from flask import request
from typing import List, TypeVar


class Auth:
    """ basic authentication provider class """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ authentication method """
        return False

    def authorization_header(self, request=None) -> str:
        """ authorization header method """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ current user method """
        return None
