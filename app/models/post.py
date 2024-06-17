class Post:
    def __init__ (self, usuario_id, title, content, category_id , time_created, num_likes=0,  num_comments=0):
        self.id = None
        self.usuario_id = usuario_id
        self.title = title
        self.content = content
        self.category_id = category_id
        self.time_created = time_created
        self.num_likes = num_likes
        self.num_comments = num_comments

    def to_dict(self):
        return {
            'id': self.id,
            'usuario_id': self.usuario_id,
            'title': self.title,
            'content': self.content,
            'category_id': self.category_id,
            'time_created': self.time_created, 
            'num_likes': self.num_likes,
            'num_comments': self.num_comments
        }
    
    