from app.models.post import Post


class Category:
    def __init__(self, name, description):
        self.id = None
        self.name = name
        self.description = description

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description
        }
    