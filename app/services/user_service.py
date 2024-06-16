from app.models.user import User
from app.repositories.user_repository import UserRepository
class UserService:
    def __init__(self):
        self.user_repository = UserRepository()

    def create_user(self, user_data):
        new_user = User(**user_data)
        self.user_repository.add_user(new_user)
        return new_user

    def get_user(self, user_id):
        return self.user_repository.get_user_by_id(user_id)

    def get_all_users(self):
        return self.user_repository.get_all_users()

    def update_user(self, user_id, user_data):
        return self.user_repository.update_user(user_id, user_data)

    def delete_user(self, user_id):
        return self.user_repository.delete_user(user_id)
