#!/usr/bin/env python3
""" Module of Auth
"""
from flask import request
from typing import TypeVar


class Auth:
    """ Auth class
    """
    def require_auth(self, path: str, excluded_paths: list[str]) -> bool:
        """ require_auth method
        """
        if path is None or excluded_paths is None or excluded_paths == []:
            return True
        if path in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """ authorization_header method
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ current_user method
        """
        return None
