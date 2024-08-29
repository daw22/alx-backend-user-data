#!/usr/bin/env python3
"""
Encrypting passwords
"""
import bcrypt


def hash_password(passwd: str) -> bytes:
    """
    Returns a salted, hashed password which is
    a byte string
    """
    password = passwd.encode()
    hashed_passwd = bcrypt.hashpw(password, bcrypt.gensalt())

    return hashed_passwd
