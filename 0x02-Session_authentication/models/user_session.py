#!/usr/bin/env python3
"""
model for user session storage
"""
from models.base import Base


class UserSession(Base):
    """
    User session model
    """
    def __init__(self, *args: list, **kwargs: dict):
        """Init"""
        super().__init__(*args, **kwargs)
        self.user_id = kwargs.get('user_id')
        self.session_id = kwargs.get('session_id')
