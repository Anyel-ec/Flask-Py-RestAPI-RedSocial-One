from flask import Blueprint, request, jsonify
from app.services.user_service import UserService
from app.models.user import User

user_blueprint = Blueprint('user_blueprint', __name__)
user_service = UserService()

@user_blueprint.route('/users', methods=['POST'])
def create_user():
    user_data = request.json
    new_user = user_service.create_user(user_data)
    return jsonify(new_user.to_dict()), 201

@user_blueprint.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = user_service.get_user(user_id)
    if user:
        return jsonify(user.to_dict()), 200
    return jsonify({'message': 'User not found'}), 404

@user_blueprint.route('/users', methods=['GET'])
def get_all_users():
    users = user_service.get_all_users()
    return jsonify([user.to_dict() for user in users]), 200

@user_blueprint.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user_data = request.json
    updated_user = user_service.update_user(user_id, user_data)
    if updated_user:
        return jsonify(updated_user.to_dict()), 200
    return jsonify({'message': 'User not found'}), 404

@user_blueprint.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    success = user_service.delete_user(user_id)
    if success:
        return jsonify({'message': 'User deleted'}), 200
    return jsonify({'message': 'User not found'}), 404
