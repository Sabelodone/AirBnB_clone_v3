#!/usr/bin/python3
"""create blueprint"""
from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

# Import all views in the package
from .views.index import *
from .views.states import *
from .views.cities import *
from .views.amenities import *
from .views.users import *
from .views.places import *
from .views.places_reviews import *
from .views.places_amenities import *

# Registering blueprints
app_views.register_blueprint(index)
app_views.register_blueprint(state)
app_views.register_blueprint(city)
app_views.register_blueprint(amenity)
app_views.register_blueprint(user)
app_views.register_blueprint(place)
app_views.register_blueprint(places_reviews)
app_views.register_blueprint(places_amenities)
