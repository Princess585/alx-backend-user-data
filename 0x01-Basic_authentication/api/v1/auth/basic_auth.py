#!/usr/bin/env python3
"""API Authentication"""

from api.v1.auth.auth import Auth
from base64 import b64decode
from models.user import User
from typing import TypeVar


class BasicAuth(Auth):
    """API Authentication"""

    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """Return None"""
        if type(authorization_header) is not str:
            return None
        elif authorization_header.startswith('Basic '):
            return authorization_header[6:]
        else:
            return None

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """Return None"""
        if type(base64_authorization_header) is not str:
            return None
        else:
            try:
                b64bytes = base64_authorization_header.encode('utf-8')
                string_bytes = b64decode(b64bytes)
                return string_bytes.decode('utf-8')
            except Exception:
                return None

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header: str
                                 ) -> (str, str):
        """Returns tuple"""
        if (decoded_base64_authorization_header is not None and
                type(decoded_base64_authorization_header) is str and
                ':' in decoded_base64_authorization_header):
            try:
                return tuple(decoded_base64_authorization_header.split(":"))
            except Exception:
                return (None, None)
        else:
            return (None, None)

    def user_object_from_credentials(self, user_email: str,
                                     user_pwd: str) -> TypeVar('User'):
        """Return None"""
        if type(user_email) is not str or user_email is None:
            return None

        if type(user_pwd) is not str or user_pwd is None:
            return None

        try:
            found_users = User.search({'email': user_email})
        except Exception:
            return None

        for user in found_users:
            if user.is_valid_password(user_pwd):
                return user

        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Return None"""
        auth_header = self.authorization_header(request)

        if not auth_header:
            return None

        encoded = self.extract_base64_authorization_header(auth_header)

        if not encoded:
            return None

        decoded = self.decode_base64_authorization_header(encoded)

        if not decoded:
            return None

        email, pwd = self.extract_user_credentials(decoded)

        if not email or not pwd:
            return None

        user = self.user_object_from_credentials(email, pwd)

        return user
