class PostRepository:
    def __init__(self):
        self.posts = []
        self.next_id = 1

    def add_post(self, post):
        post.id = self.next_id  
        self.posts.append(post)
        self.next_id += 1
    
    def get_post_by_id(self, post_id):
        for post in self.posts:
            if post.id == post_id:
                return post
        return None
    
    def get_all_posts(self):
        return self.posts
    
    def update_post(self, post_id, post_data):
        post = self.get_post_by_id(post_id)
        if post:
            post.usuario_id = post_data.get('usuario_id', post.usuario_id)
            post.title = post_data.get('title', post.title)
            post.content = post_data.get('content', post.content)
            post.category_id = post_data.get('category_id', post.category_id)
            post.time_created = post_data.get('time_created', post.time_created)
            return post
        return None
    
    def delete_post(self, post_id):
        post = self.get_post_by_id(post_id)
        if post:
            self.posts.remove(post)
            return True
        return False
    
    def get_posts_by_user_id(self, user_id):
        return [post for post in self.posts if post.usuario_id == user_id]
    