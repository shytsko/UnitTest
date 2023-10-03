# Разработайте класс User с методом аутентификации по логину и паролю. Метод должен возвращать true, если
# введенные логин и пароль корректны, иначе false. Протестируйте все методы
# Добавьте класс UserRepository для управления пользователями. В этот класс должен быть включен метод
# addUser, который добавляет пользователя в систему, если он прошел аутентификацию. Покройте тестами новую
# функциональность
# Добавьте функцию в класс UserRepository, которая разлогинивает всех пользователей,
# кроме администраторов. Для этого, вам потребуется расширить класс User новым свойством,
# указывающим, обладает ли пользователь админскими правами. Протестируйте данную функцию.

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

    @property
    def name(self):
        return self._name


class UserRepository:
    def __init__(self):
        self._data: dict[User] = dict()

    def add_user(self, user: User):
        self._data[user.name] = user

    def find_by_name(self, username: str) -> bool:
        return username in self._data

    def logout_not_admin(self):
        for name in tuple(self._data.keys()):
            if not self._data[name].is_admin:
                self._data.pop(name)
