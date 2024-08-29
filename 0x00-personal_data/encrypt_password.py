#!/usr/bin/env python3
"""
Encrypting passwords
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """
    Returns a salted, hashed password which is
    a byte string
    """
    enc_password = passwd.encode()
    hashed_passwd = bcrypt.hashpw(enc_password, bcrypt.gensalt())

    return hashed_passwd
