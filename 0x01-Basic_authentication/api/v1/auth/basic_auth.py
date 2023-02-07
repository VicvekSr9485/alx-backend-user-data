#!/usr/bin/env python3
""" basic auth subclass of auth """

from api.v1.auth.auth import Auth
from base64 import b64decode


class BasicAuth(Auth):
    """ Basic authentication """
    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """ Extract base64 authorization header """
        if authorization_header is None:
            return None
        if type(authorization_header) != str:
            return None
        if not authorization_header.startswith('Basic '):
            return None
        else:
            return authorization_header.split(' ')[-1]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """ returns a decoded base64 authorization header """
        if not base64_authorization_header:
            return None
        if type(base64_authorization_header) != str:
            return None
        try:
            return b64decode(base64_authorization_header).decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """ extracts user credentials """
        if not decoded_base64_authorization_header:
            return None, None
        if type(decoded_base64_authorization_header) != str:
            return None, None
        if ':' not in decoded_base64_authorization_header:
            return None, None
        decoded_values = decoded_base64_authorization_header.split(':', 1)
        return decoded_values[0], decoded_values[1]
