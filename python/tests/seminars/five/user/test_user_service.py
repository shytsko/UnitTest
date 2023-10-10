from seminars.five.user.user_repository import UserRepository
from seminars.five.user.user_service import UserService
from mockito import mock, verify, when, spy, spy2


class TestUserService:
    def test_get_user_name(self):
        user_repository = UserRepository()
        spy2(user_repository.get_user_by_id)
        user_service = UserService(user_repository)

        user_name = user_service.get_user_name(1)

        verify(user_repository, times=1).get_user_by_id(1)
        assert user_name == "User 1"


