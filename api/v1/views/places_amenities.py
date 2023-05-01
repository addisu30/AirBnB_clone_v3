#!/usr/bin/python3
'''Contains the places_amenities view for the API.'''
from flask import abort, jsonify, make_response
from api.v1.views import app_views
from models import storage
from models import amenity
from models.amenity import Amenity
from models.place import Place
from os import getenv
