#!/usr/bin/python3
"""
App module to create and configure the Flask app
"""

from api.v1.views.index import app_views as index
from flask import Flask, jsonify
from werkzeug.exceptions import HTTPException, NotFound
from models import storage
from api.v1.views import app_views
from os import getenv
from flask_cors import CORS
import traceback

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "0.0.0.0"}})
app.url_map.strict_slashes = False

# Register the blueprints with unique names
app.register_blueprint(index, url_prefix="/api/v1/index")
'''app.register_blueprint(app_views, url_prefix="/api/v1")
app.register_blueprint(app_views)
app.register_blueprint(index)'''


@app.errorhandler(Exception)
def handle_exception(e):
    response = {'error': 'Not found000'}
    return jsonify(response), 500


@app.route('/api/v1/nop', methods=['GET'])
def custom_nop():
    return jsonify({'error': 'Not found'}), 404


# Route for /api/v1/stats
@app.route('/api/v1/stats', methods=['GET'])
def get_stats():
    stats = {
        'amenities': storage.count('Amenity'),
        'cities': storage.count('City'),
        'places': storage.count('Place'),
        'reviews': storage.count('Review'),
        'states': storage.count('State'),
        'users': storage.count('User')
    }
    return jsonify(stats)


@app.teardown_appcontext
def teardown_appcontext(exception):
    """Close the storage engine upon app context teardown.

    Args:
        exception (Exception): The exception that occurred during
            the app context teardown.
    """
    storage.close()


if __name__ == '__main__':
    HBNB_API_HOST = getenv("HBNB_API_HOST", '0.0.0.0')
    HBNB_API_PORT = int(getenv("HBNB_API_PORT", 5000))
    app.run(host=HBNB_API_HOST, port=HBNB_API_PORT, threaded=True)
