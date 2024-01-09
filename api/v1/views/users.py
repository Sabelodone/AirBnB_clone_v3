#!/usr/bin/python3
"""users"""

"""users"""

from flask import Blueprint, jsonify, abort, request
from models import storage
from models.user import User
from api.v1.views import app_views

user = Blueprint('user', __name__, url_prefix='/api/v1/users')


@app_views.route('/users/', methods=['GET'])
@app_views.route('/users', methods=['GET'])
def list_users():
    '''Retrieves a list of all User objects'''
    list_users = [obj.to_dict() for obj in storage.all("User").values()]
    return jsonify(list_users)


@app_views.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    '''Retrieves a User object'''
    all_users = storage.all("User").values()
    user_obj = [obj.to_dict() for obj in all_users if obj.id == user_id]
    if user_obj == []:
        abort(404)
    return jsonify(user_obj[0])


@app_views.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    '''Deletes a User object'''
    all_users = storage.all("User").values()
    user_obj = [obj.to_dict() for obj in all_users if obj.id == user_id]
    if user_obj == []:
        abort(404)
    user_obj.remove(user_obj[0])
    for obj in all_users:
        if obj.id == user_id:
            storage.delete(obj)
            storage.save()
    return jsonify({}), 200


@app_views.route('/users/', methods=['POST'])
def create_user():
    '''Creates a User'''
    if not request.get_json():
        abort(400, 'Not a JSON')
    if 'email' not in request.get_json():
        abort(400, 'Missing email')
    if 'password' not in request.get_json():
        abort(400, 'Missing password')
    users = []
    new_user = User(email=request.json['email'],
                    password=request.json['password'])
    storage.new(new_user)
    storage.save()
    users.append(new_user.to_dict())
    return jsonify(users[0]), 201


@app_views.route('/users/<user_id>', methods=['PUT'])
def updates_user(user_id):
    '''Updates a User object'''
    all_users = storage.all("User").values()
    user_obj = [obj for obj in all_users if obj.id == user_id]
    if not user_obj:
        abort(404)

    if not request.get_json():
        abort(400, 'Not a JSON')

    user_obj = user_obj[0]

    try:
        user_obj.first_name = request.json.get('first_name', user_obj.first_name)
        user_obj.last_name = request.json.get('last_name', user_obj.last_name)
    except Exception as e:
        abort(400, str(e))

    storage.save()
    return jsonify(user_obj.to_dict()), 200
