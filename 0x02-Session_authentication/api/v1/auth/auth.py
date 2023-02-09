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
        if path in excluded_paths or path + '/' in excluded_paths:
            return False
        for e_path in excluded_paths:
            if e_path.endswith('*'):
                if path.startswith(e_path[:1]):
                    return False
        return True

    def authorization_header(self, request=None) -> str:
        """ authorization header method """
        if not request or not request.headers:
            return None
        if not request.headers.get('Authorization'):
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """ current user method """
        return None
