import requests
from app.config.app_environment import AppEnvironment

class RestConsumerRepository:
    def __init__(self):
        self.base_url = AppEnvironment.BASE_URL
        self.api_comment = AppEnvironment.API_COMMENT
        self.api_comment_count = f"{self.api_comment}contarComentariosPorPost/"


    def get_comment(self):
        response = requests.get(self.base_url + self.api_comment)
        if response.status_code == 200:
            return response.json()  # Parsear la respuesta como JSON
        else:
            response.raise_for_status()

    def count_comments_by_post_id(self, post_id):
        response = requests.get(f"{self.base_url}{self.api_comment_count}{post_id}")
        if response.status_code == 200:
            return response.json()  # Parsear la respuesta como JSON
        else:
            response.raise_for_status()