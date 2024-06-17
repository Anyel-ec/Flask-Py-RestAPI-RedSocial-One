from flask import Blueprint, jsonify
from app.services.consumer_comment_service import RestConsumerService

consumer_comment_blueprint = Blueprint('rest_consumer', __name__)
consumer_comment_service = RestConsumerService()

@consumer_comment_blueprint.route('/getComment', methods=['GET'])
def get_comment():
    comment_data = consumer_comment_service.get_comment()
    return jsonify(comment_data), 200

@consumer_comment_blueprint.route('/contarComentariosPorPost/<int:post_id>', methods=['GET'])
def count_comments_by_post_id(post_id):
    count = consumer_comment_service.count_comments_by_post_id(post_id)
    return jsonify(count), 200