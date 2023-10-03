from seminars.third.hw.User import User


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
