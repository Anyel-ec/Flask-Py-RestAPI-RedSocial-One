class User: 
    def __init__(self, id, name, email, password, phone, birthdate):
        self.id = id
        self.name = name
        self.email = email
        self.password = password
        self.phone = phone
        self.birthdate = birthdate

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'password': self.password,
            'phone': self.phone,
            'birthdate': self.birthdate
        }