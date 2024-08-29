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
    enc_password = password.encode()
    hashed_passwd = bcrypt.hashpw(enc_password, bcrypt.gensalt())

    return hashed_passwd


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Validate password
    """
    encoded_pwd = password.encode()
    return bcrypt.checkpw(encoded_pwd, hashed_password)
