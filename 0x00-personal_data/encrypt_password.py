#!/usr/bin/env python3
"""Encrypting password"""
import bcrypt


def hash_password(password: str) -> bytes:
    """Return the hashpassword with the gensalt"""
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """The password matches the password of the hash"""
    return bcrypt.checkpw(password.encode("utf-8"), hashed_password)
