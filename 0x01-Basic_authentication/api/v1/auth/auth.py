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
        """ Not implemented yet
        """
        return False

    def authorization_header(self, request=None) -> str:
        """ Not implemented yet
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Not implemented yet
        """
        return None
