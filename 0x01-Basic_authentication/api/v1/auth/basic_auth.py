#!/usr/bin/env python3
"""
Basic Auth class
"""
from api.v1.auth.auth import Auth
import base64


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

    def decode_base64_authorization_header(self,
                                           base64_authorization_header: str
                                           ) -> str:
        """
        Returns the decoded value of a base64 string
        base64_authorization_header
        """
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            decoded = base64.b64decode(base64_authorization_header)
            return decoded.decode("utf-8")
        except Exception:
            return None

    def extract_user_credentials(self, decoded_base64_authorization_header: str
                                 ) -> (str, str):
        """
        Returns the user email and password from the
        baseb4 decoded value
        """
        if decoded_base64_authorization_header is None:
            return (None, None)
        if not isinstance(decoded_base64_authorization_header, str):
            return (None, None)
        if ":" not in decoded_base64_authorization_header:
            return (None, None)
        credentials = decoded_base64_authorization_header.split(":")
        return (credentials[0], credentials[1])
