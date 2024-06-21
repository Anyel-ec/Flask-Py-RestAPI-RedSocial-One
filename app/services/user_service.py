from app.models.user import User
from app.repositories.user_repository import UserRepository
from hashlib import sha256
import uuid
class UserService:
    def __init__(self):
        self.user_repository = UserRepository()

    def create_user(self, user_data):
        password = user_data['password']
        salt = uuid.uuid4().hex
        hashed_password = sha256((salt + password).encode()).hexdigest()

        user_data['password'] = hashed_password
        user_data['salt'] = salt  # Guarda el salt junto con los datos del usuario

        # Crea el nuevo usuario y guárdalo en el UserRepository
        new_user = User(name=user_data['name'],
                        email=user_data['email'],
                        password=user_data['password'],
                        phone=user_data['phone'],
                        birthdate=user_data['birthdate'],
                        salt=user_data['salt'])  # Pasa el salt como un argumento nombrado

        self.user_repository.add_user(new_user)
        return new_user

    def get_user(self, user_id):
        return self.user_repository.get_user_by_id(user_id)

    def get_all_users(self):
        return self.user_repository.get_all_users()

    def update_user(self, user_id, user_data):
        user = self.user_repository.get_user_by_id(user_id)
        if user:
            if 'password' in user_data:
                password = user_data['password']
                salt = uuid.uuid4().hex
                hashed_password = sha256((salt + password).encode()).hexdigest()
                user_data['password'] = hashed_password
                user_data['salt'] = salt  # Actualiza también el salt
            
            updated_user = self.user_repository.update_user(user_id, user_data)
            return updated_user
        return None

    def delete_user(self, user_id):
        return self.user_repository.delete_user(user_id)

    def verify_password(self, user_id, password):
        user = self.user_repository.get_user_by_id(user_id)
        if user:
            hashed_password = sha256((user.salt + password).encode()).hexdigest()
            if hashed_password == user.password:
                return True
        return False
    
    def verify_password_with_email(self, email, password):
        for user in self.user_repository.get_all_users():
            if user.email == email:
                hashed_password = sha256((user.salt + password).encode()).hexdigest()
                if hashed_password == user.password:
                    return True
        return False
    
    def get_user_by_email(self, email):
        return self.user_repository.get_user_by_email(email)
    
    def verify_exist_user(self, email):
        return self.user_repository.verify_exist_user(email)
    
    
