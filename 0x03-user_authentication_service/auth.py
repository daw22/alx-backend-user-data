#!/usr/bin/env python3
"""
Password hasher
"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """
    Takes a string and returns a salted hash
    of the string/password
    """
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

    return hashed_password
