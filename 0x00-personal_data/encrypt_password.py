#!/usr/bin/env python3
""" encryption module """

import bcrypt


def hash_password(password) -> bytes:
    """ return hashed password """
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
