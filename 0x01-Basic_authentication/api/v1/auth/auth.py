#!/usr/bin/env python3
""" basic authentication provider """

from flask import request
from typing import List, TypeVar


class Auth:
    """ basic authentication provider class """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ authentication method """
        if path is None or excluded_paths is None:
            return True
        elif path in excluded_paths or path + '/' in excluded_paths:
            return False
        else:
            return True

    def authorization_header(self, request=None) -> str:
        """ authorization header method """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ current user method """
        return None
