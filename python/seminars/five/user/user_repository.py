class UserRepository:

    def get_user_by_id(self, pk: int) -> str:
        # В реальной жизни здесь был бы код, работающий с базой данных
        return f"User {pk}"
