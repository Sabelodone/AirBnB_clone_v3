#!/usr/bin/python3
"""create blueprint"""
from flask import Blueprint
from api.v1.views.index import index
from api.v1.views.states import state
from api.v1.views.cities import city
from api.v1.views.amenities import amenity
from api.v1.views.users import user
from api.v1.views.places import place
from api.v1.views.places_reviews import places_reviews
from api.v1.views.places_amenities import places_amenities

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

# Registering blueprints
app_views.register_blueprint(index)
app_views.register_blueprint(state)
app_views.register_blueprint(city)
app_views.register_blueprint(amenity)
app_views.register_blueprint(user)
app_views.register_blueprint(place)
app_views.register_blueprint(places_reviews)
app_views.register_blueprint(places_amenities)
