from flask import Blueprint, request, jsonify
from app.services.post_service import PostService

post_blueprint = Blueprint('post_blueprint', __name__)
post_service = PostService()

@post_blueprint.route('/posts', methods=['POST'])
def create_post():
    post_data = request.json
    new_post = post_service.create_post(post_data)
    return jsonify(new_post.to_dict()), 201

@post_blueprint.route('/posts/<int:post_id>', methods=['GET'])
def get_post(post_id):
    post = post_service.get_post(post_id)
    if post:
        return jsonify(post.to_dict()), 200
    return jsonify({'message': 'Post not found'}), 404

@post_blueprint.route('/posts', methods=['GET'])
def get_all_posts():
    posts = post_service.get_all_posts()
    return jsonify([post.to_dict() for post in posts]), 200

@post_blueprint.route('/posts/<int:post_id>', methods=['PUT'])
def update_post(post_id):
    post_data = request.json
    updated_post = post_service.update_post(post_id, post_data)
    if updated_post:
        return jsonify(updated_post.to_dict()), 200
    return jsonify({'message': 'Post not found'}), 404

@post_blueprint.route('/posts/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    success = post_service.delete_post(post_id)
    if success:
        return jsonify({'message': 'Post deleted'}), 200
    return jsonify({'message': 'Post not found'}), 404

@post_blueprint.route('/posts/user/<int:user_id>', methods=['GET'])
def get_posts_by_user_id(user_id):
    posts = post_service.get_posts_by_user_id(user_id)
    return jsonify([post.to_dict() for post in posts]), 200
