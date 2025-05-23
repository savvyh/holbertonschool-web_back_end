#!/usr/bin/env python3
"""
encrypt_password module
"""

import bcrypt


def hash_password(password: str) -> bytes:
    """
    hash_password function that returns a salted, hashed password
    """
    salt: bytes = bcrypt.gensalt()
    hashed: bytes = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed
