#!/usr/bin/python3
'''
Creates a Blueprint instance with `url_prefix` set to `/api/v1`.
'''

from flask import Blueprint
from api.v1.views import index, states, cities, amenities, users, places, places_reviews, places_amenities

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

# Importing views from other modules
__all__ = [index, states, cities, amenities, users, places, places_reviews, places_amenities]
