import hashlib
import os


class User:
    def __init__(self, name: str, password: str, is_admin: bool = False):
        self._name = name
        self._hashed_pws = self._get_password_hash(password)
        self._is_admin = is_admin

    def _get_password_hash(self, password: str) -> bytes:
        salt = os.urandom(32)
        key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
        return salt + key

    def _check_password(self, password):
        salt = self._hashed_pws[:32]
        key = self._hashed_pws[32:]
        check_key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
        return check_key == key

    def authenticate(self, name: str, password: str) -> bool:
        return name == self._name and self._check_password(password)

    @property
    def is_admin(self):
        return self._is_admin
