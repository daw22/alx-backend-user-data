#!/usr/bin/env python3
"""
Password hasher
"""
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
import uuid
from typing import Union


def _hash_password(password: str) -> bytes:
    """
    Takes a string and returns a salted hash
    of the string/password
    """
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

    return hashed_password


def _generate_uuid() -> str:
    """
    Returns a string representation of a new UUID
    """
    uu = uuid.uuid4()
    return str(uu)


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """
        Registers a user
        - if the user already exists raise a type error
        - returns the newly created user
        """
        try:
            find_user = self._db.find_user_by(email=email)
        except NoResultFound:
            hashed_password = _hash_password(password)
            return self._db.add_user(email, hashed_password)

        raise ValueError(f"User {email} already exists")

    def valid_login(self, email: str, password: str) -> bool:
        """
        Locates user by email and if it exists checks
        the password, if it matches returns True otherwise
        False
        """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return False

        return bcrypt.checkpw(password.encode('utf-8'),
                              user.hashed_password)

    def create_session(self, email: str) -> str:
        """
        creates, stores and returns a session id
        """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return None

        session_id = _generate_uuid()
        self._db.update_user(user.id, session_id=session_id)

        return session_id

    def get_user_from_session_id(self, session_id: str
                                 )-> Union[User, None]:
        """
        Gets and returns  the user object from session id
        """
        if sesssion_id is None:
            return None

        try:
            user = self._db.find_user_by(session_id=session_id)
            return user
        except NoResultFound:
            return None

    def destroy_session(self, user_id: int) -> None:
        """
        Destroys user session - removes session_id
        value from user object
        """
        try:
            user = self._db.find_user_by(id=user_id)
        except NoResultFound:
            return None

        self.db.update_user(id, session_id=None)

        return None
