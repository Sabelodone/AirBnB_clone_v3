from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

# Import all views in the package
from api.v1.views.index import *
from api.v1.views.states import state
from api.v1.views.cities import city
from api.v1.views.amenities import amenity
from api.v1.views.users import user
from api.v1.views.places import place
from api.v1.views.places_reviews import places_reviews
from api.v1.views.places_amenities import places_amenities

# Set the url_prefix for each blueprint
index.url_prefix = '/index'
state.url_prefix = '/states'
city.url_prefix = '/cities'
amenity.url_prefix = '/amenities'
user.url_prefix = '/users'
place.url_prefix = '/places'
places_reviews.url_prefix = '/reviews'
places_amenities.url_prefix = '/places_amenities'

# Registering blueprints
app_views.register_blueprint(index)
app_views.register_blueprint(state)
app_views.register_blueprint(city)
app_views.register_blueprint(amenity)
app_views.register_blueprint(user)
app_views.register_blueprint(place)
app_views.register_blueprint(places_reviews)
app_views.register_blueprint(places_amenities)
