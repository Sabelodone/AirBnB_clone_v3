#!/usr/bin/python3
'''
Create routes `/status` and `/api/v1/stats` on the object app_views.
'''
from flask import Blueprint

from flask import jsonify
from api.v1.views import app_views
from models import storage

index = Blueprint('index', __name__)

@index.route('/index', methods=['GET'])
def get_index():
    # Your view logic here
    pass

@app_views.route('/status', methods=['GET'])
def api_status():
    '''
    Returns a JSON response for RESTful API health.
    '''
    return jsonify({"status": "OK"})

@app_views.route('/api/v1/stats', methods=['GET'])
def get_stats():
    '''
    Retrieves the number of each object by type.
    '''
    stats = {
        'amenities': storage.count('Amenity'),
        'cities': storage.count('City'),
        'places': storage.count('Place'),
        'reviews': storage.count('Review'),
        'states': storage.count('State'),
        'users': storage.count('User')
    }
    return jsonify(stats)
