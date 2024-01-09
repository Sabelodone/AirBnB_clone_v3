#!/usr/bin/python3
"""
User module to create a new view for the User object that handles all default RESTFul API actions
"""

from flask import Blueprint, jsonify, abort, request
from models import storage
from models.user import User

user = Blueprint('user', __name__, url_prefix='/api/v1/users')


@user.route('/', methods=['GET'])
@user.route('', methods=['GET'])
def list_users():
    """Retrieves a list of all User objects"""
    list_users = [user.to_dict() for user in storage.all("User").values()]
    return jsonify(list_users)


@user.route('/<user_id>', methods=['GET'])
def get_user(user_id):
    """Retrieves a User object"""
    user_obj = storage.get("User", user_id)
    if user_obj is None:
        abort(404)
    return jsonify(user_obj.to_dict())


@user.route('/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    """Deletes a User object"""
    user_obj = storage.get("User", user_id)
    if user_obj is None:
        abort(404)
    storage.delete(user_obj)
    storage.save()
    return jsonify({}), 200


@user.route('/', methods=['POST'])
def create_user():
    """Creates a User"""
    data = request.get_json()
    if not data:
        abort(400, 'Not a JSON')
    if 'email' not in data:
        abort(400, 'Missing email')
    if 'password' not in data:
        abort(400, 'Missing password')
    new_user = User(**data)
    storage.new(new_user)
    storage.save()
    return jsonify(new_user.to_dict()), 201


@user.route('/<user_id>', methods=['PUT'])
def update_user(user_id):
    """Updates a User object"""
    user_obj = storage.get("User", user_id)
    if user_obj is None:
        abort(404)
    data = request.get_json()
    if not data:
        abort(400, 'Not a JSON')
    for key, value in data.items():
        if key not in ['id', 'email', 'created_at', 'updated_at']:
            setattr(user_obj, key, value)
    storage.save()
    return jsonify(user_obj.to_dict()), 200
