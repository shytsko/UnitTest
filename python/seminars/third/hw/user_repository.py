from seminars.third.hw.user import User


class UserRepository:
    def __init__(self):
        self._data = dict()

    def add_user(self, user: User):
        self._data[user.name] = User

    def find_by_name(self, username: str) -> bool:
        return username in self._data

    def logout_not_admin(self):
        pass
