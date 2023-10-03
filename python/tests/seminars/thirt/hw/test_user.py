from seminars.third.hw.user import User, UserRepository


class TestUser:
    def setup(self):
        self.user_name = "username"
        self.password = "secret"
        self.bad_password = "bad_password"
        self.user = User(self.user_name, self.password)
        self.admin = User(self.user_name, self.password, True)

    def test_user_authenticate_successful(self):
        assert self.user.authenticate(self.user_name, self.password)

    def test_user_authenticate_unsuccessful(self):
        assert not self.user.authenticate(self.user_name, self.bad_password)

    def test_user_is_admin(self):
        assert self.admin.is_admin

    def test_user_not_admin(self):
        assert not self.user.is_admin


class TestUserRepository:
    def setup(self):
        self.user_is_admin_flag = [i % 3 == 0 for i in range(10)]
        self.users = [User(f"username{i}", f"password{i}", self.user_is_admin_flag[i]) for i in range(10)]
        self.user_repository = UserRepository()

    def test_user_repository_add_find_by_name(self):
        self.user_repository.add_user(self.users[0])
        assert self.user_repository.find_by_name(self.users[0].name)

    def test_user_repository_logout_not_admin(self):
        for user in self.users:
            self.user_repository.add_user(user)
        self.user_repository.logout_not_admin()
        users_authorized = [self.user_repository.find_by_name(user.name) for user in self.users]
        assert users_authorized == self.user_is_admin_flag
