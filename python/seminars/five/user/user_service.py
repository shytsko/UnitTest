from seminars.five.user.user_repository import UserRepository


class UserService:

    def __init__(self, user_repository: UserRepository):
        self._user_repository = user_repository

    def get_user_name(self, pk: int) -> str:
        return self._user_repository.get_user_by_id(pk)
