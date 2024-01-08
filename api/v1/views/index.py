#!/usr/bin/python3
"""index"""
from flask import jsonify
from api.v1.views import app_views
from models import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

classes = {"users": User, "places": Place, "states": State,
           "cities": City, "amenities": Amenity,
           "reviews": Review}


@app_views.route('/status', methods=['GET'])
def status():
    ''' Routes to the status page '''
    return jsonify({'status': 'OK'})


@app_views.route('/stats', methods=['GET'])
def count():
    ''' Retrieves the number of each object by type '''
    count_dict = {}
    for cls_name, cls in classes.items():
        count_dict[cls_name] = storage.count(cls)
    return jsonify(count_dict)
