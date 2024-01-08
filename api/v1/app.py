/#!/usr/bin/python3
"""app"""
'''from flask import Flask, make_response, jsonify
from models import storage
from api.v1.views import app_views
from os import getenv
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "0.0.0.0"}})
app.url_map.strict_slashes = False
app.register_blueprint(app_views)

@app.teardown_appcontext
def teardown_appcontext(self):
    '''''' Closes storage engine ''''''
    storage.close()

@app.errorhandler(404)
def not_found(error):
    '''''' Handles 404 error and gives a JSON-formatted response ''''''
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    HBNB_API_HOST = getenv("HBNB_API_HOST", '0.0.0.0')
    HBNB_API_PORT = int(getenv("HBNB_API_PORT", 5000))
    app.run(host=HBNB_API_HOST, port=HBNB_API_PORT, threaded=True)

#!/usr/bin/python3'''
"""
App module to create and configure the Flask app
"""

from flask import Flask
from models import storage
from api.v1.views import app_views
from os import getenv

app = Flask(__name__)
app.url_map.strict_slashes = False
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown_appcontext(exception):
    """Method to close storage"""
    storage.close()


if __name__ == "__main__":
    host = getenv('HBNB_API_HOST', '0.0.0.0')
    port = getenv('HBNB_API_PORT', 5000)
    app.run(host=host, port=port, threaded=True)

