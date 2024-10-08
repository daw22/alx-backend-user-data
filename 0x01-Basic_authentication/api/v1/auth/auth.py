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
        slashed = True if path[-1] == '/' else False
        temp_path = path
        if not slashed:
            temp_path += '/'
        for ex_path in excluded_paths:
            ex_path_len = len(ex_path)
            if ex_path_len == 0:
                continue
            if ex_path[-1] == '*':
                if ex_path[:-1] == path[:ex_path_len - 1]:
                    return False
            else:
                if temp_path == ex_path:
                    return False
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
