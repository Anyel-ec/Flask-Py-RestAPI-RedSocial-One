from app.repositories.consumer_comment_repository import RestConsumerRepository


class RestConsumerService:
    def __init__(self):
        self.rest_consumer_repository = RestConsumerRepository()

    def get_comment(self):
        return self.rest_consumer_repository.get_comment()
    
    def count_comments_by_post_id(self, post_id):
        return self.rest_consumer_repository.count_comments_by_post_id(post_id)