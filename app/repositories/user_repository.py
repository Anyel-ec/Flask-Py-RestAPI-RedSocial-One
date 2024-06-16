class UserRepository:
    def __init__(self):
        self.users = []

    def add_user(self, user):
        self.users.append(user)

    def get_user_by_id(self, user_id):
        for user in self.users:
            if user.id == user_id:
                return user
        return None

    def get_all_users(self):
        return self.users

    def update_user(self, user_id, user_data):
        user = self.get_user_by_id(user_id)
        if user:
            user.name = user_data.get('name', user.name)
            user.email = user_data.get('email', user.email)
            user.password = user_data.get('password', user.password)
            user.phone = user_data.get('phone', user.phone)
            user.birthdate = user_data.get('birthdate', user.birthdate)
            return user
        return None

    def delete_user(self, user_id):
        user = self.get_user_by_id(user_id)
        if user:
            self.users.remove(user)
            return True
        return False
