from typing import List
from app.models.post import Post
from app.repositories.post_repository import PostRepository


class PostService:
    def __init__(self):
        self.post_repository = PostRepository()

    def create_post(self, post_data):
        new_post = Post(usuario_id=post_data['usuario_id'],
                        title=post_data['title'],
                        content=post_data['content'],
                        category_id=post_data['category_id'],
                        time_created=post_data['time_created'])

        self.post_repository.add_post(new_post)
        return new_post
    
    def get_post(self, post_id):
        return self.post_repository.get_post_by_id(post_id)
    

    def get_all_posts(self):
        return self.post_repository.get_all_posts()
    
    def update_post(self, post_id, post_data):
        post = self.post_repository.get_post_by_id(post_id)
        if post:
            post.usuario_id = post_data.get('usuario_id', post.usuario_id)
            post.title = post_data.get('title', post.title)
            post.content = post_data.get('content', post.content)
            post.category_id = post_data.get('category_id', post.category_id)
            post.time_created = post_data.get('time_created', post.time_created)
            return post
        return None
    
    def delete_post(self, post_id):
        return self.post_repository.delete_post(post_id)
    
    def get_posts_by_user_id(self, user_id):
        return self.post_repository.get_posts_by_user_id(user_id)
    