#!/usr/bin/env python3
"""
Basic Auth class
"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """
    Basic Auth class, inherits from Auth
    """
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """
        Returns the base64 part of the Authorization header for
        a baic authentication
        """
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        return authorization_header[6:]
