#!/usr/bin/env python3
""" auth provider """

import bcrypt


def _hash_password(password: str) -> bytes:
    """ returns hashed password """
    bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hash = bcrypt.hashpw(bytes, salt)
    return hash
