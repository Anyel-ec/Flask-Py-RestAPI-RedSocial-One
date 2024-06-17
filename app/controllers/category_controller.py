from flask import Blueprint, request, jsonify
from app.models.category import Category
from app.repositories.category_repository import CategoryRepository
from app.services.category_service import CategoryService

category_blueprint = Blueprint('category', __name__)

category_repository = CategoryRepository()
category_service = CategoryService()

@category_blueprint.route('/categories', methods=['GET'])
def get_categories():
    categories = category_service.get_all_categories()
    return jsonify([category.to_dict() for category in categories])

@category_blueprint.route('/categories/<int:category_id>', methods=['GET'])
def get_category(category_id):
    category = category_service.get_category_by_id(category_id)
    if category:
        return jsonify(category.to_dict())
    return jsonify({'message': 'Category not found'}), 404

@category_blueprint.route('/categories', methods=['POST'])
def add_category():
    data = request.json
    new_category = Category(name=data['name'], description=data['description'])
    category_service.add_category(new_category)
    return jsonify(new_category.to_dict()), 201

@category_blueprint.route('/categories/<int:category_id>', methods=['PUT'])
def update_category(category_id):
    data = request.json
    updated_category = category_service.update_category(category_id, data)
    if updated_category:
        return jsonify(updated_category.to_dict())
    return jsonify({'message': 'Category not found'}), 404

@category_blueprint.route('/categories/<int:category_id>', methods=['DELETE'])
def delete_category(category_id):
    result = category_service.delete_category(category_id)
    if result:
        return jsonify({'message': 'Category deleted'})
    return jsonify({'message': 'Category not found'}), 404
