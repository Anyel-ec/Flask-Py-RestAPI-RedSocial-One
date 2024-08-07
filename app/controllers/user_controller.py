from flask import Blueprint, request, jsonify
from app.services.user_service import UserService

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

@user_blueprint.route('/users/<int:user_id>/verify', methods=['POST'])
def verify_password(user_id):
    password = request.json.get('password')
    if user_service.verify_password(user_id, password):
        return jsonify({'message': 'Password is correct'}), 200
    return jsonify({'message': 'Password is incorrect'}), 400

@user_blueprint.route('/users/verify', methods=['POST'])
def verify_password_with_email():
    email = request.json.get('email')
    password = request.json.get('password')
    if user_service.verify_password_with_email(email, password):
        return jsonify({'message': 'Password is correct'}), 200
    return jsonify({'message': 'Password is incorrect'}), 400

@user_blueprint.route('/user/data', methods=['GET'])
def get_user_by_email():
    email = request.args.get('email')
    user = user_service.get_user_by_email(email)
    if user:
        return jsonify(user.to_dict()), 200
    return jsonify({'message': 'User not found'}), 404

@user_blueprint.route('/users/verify_exist', methods=['POST'])
def verify_exist_user():
    email = request.json.get('email')
    if user_service.verify_exist_user(email):
        return jsonify({'message': 'User exists'}), 200
    return jsonify({'message': 'User does not exist'}), 404



