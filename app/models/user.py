class User:
    def __init__(self, name, email, password, phone, birthdate, salt=None):
        self.id = None  # Deja que el UserRepository maneje la asignación del ID
        self.name = name
        self.email = email
        self.password = password
        self.phone = phone
        self.birthdate = birthdate
        self.salt = salt  # Añade el atributo salt opcional

    def to_dict(self, include_sensitive=False):
        user_dict = {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'phone': self.phone,
            'birthdate': self.birthdate
        }
        if include_sensitive:
            user_dict['password'] = self.password
            user_dict['salt'] = self.salt
        
        return user_dict