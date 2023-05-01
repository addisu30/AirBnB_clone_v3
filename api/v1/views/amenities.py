#!/usr/bin/python3
"""
view for Amenity objects that handles all default RestFul API actions
"""
from flask import jsonify, abort, request
from models import storage
from api.v1.views import app_views
from models.amenity import Amenity
