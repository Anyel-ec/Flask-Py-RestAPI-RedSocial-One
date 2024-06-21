class UserRepository:
    def __init__(self):
        self.users = []
        self.next_id = 1

    def add_user(self, user):
        user.id = self.next_id  # Asigna el ID
        self.users.append(user)
        self.next_id += 1  # Incrementa el contador de ID

    def get_user_by_id(self, user_id):
        for user in self.users:
            if user.id == user_id:
                return user
        return None
    
    def get_user_by_email(self, email):
        for user in self.users:
            if user.email == email:
                return user
        return None

    def get_all_users(self):
        return self.users

    def update_user(self, user_id, user_data):
        user = self.get_user_by_id(user_id)
        if user:
            user.name = user_data.get('name', user.name)
            user.email = user_data.get('email', user.email)
            user.phone = user_data.get('phone', user.phone)
            user.birthdate = user_data.get('birthdate', user.birthdate)
            
            if 'password' in user_data:
                user.password = user_data['password']
                user.salt = user_data.get('salt', user.salt)  # Asegúrate de actualizar el salt si se proporciona
            
            return user
        return None

    def delete_user(self, user_id):
        user = self.get_user_by_id(user_id)
        if user:
            self.users.remove(user)
            return True
        return False
    
    def verify_exist_user(self, email):
        for user in self.users:
            if user.email == email:
                return True
        return False

