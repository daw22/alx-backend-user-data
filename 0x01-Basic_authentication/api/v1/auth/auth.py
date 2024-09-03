#!/usr/bin/env python3
"""
Auth calss
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """
    Auth class
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ checks if a route requires authorization
        """
        if path is None:
            return True
        if excluded_paths is None or len(excluded_paths) == 0:
            return True
        if path[-1] != "/":
            path = path + "/"
        if path in excluded_paths:
            return False
        else:
            return True

    def authorization_header(self, request=None) -> str:
        """ Not implemented yet
        """
        if request is None:
            return None
        if 'Authorization' not in request.headers:
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """ Not implemented yet
        """
        return None
