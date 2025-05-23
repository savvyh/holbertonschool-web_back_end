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


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    is_valid function that validates a password against its hash
    """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
