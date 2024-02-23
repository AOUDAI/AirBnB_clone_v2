#!/usr/bin/python3
"""This module instantiates an object of class FileStorage and DBStorage"""
from models.amenity import Amenity
from models.state import State
from models.city import City
from models.user import User
from models.review import Review
from models.place import Place
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
from os import environ


if environ.get("HBNB_TYPE_STORAGE") == "db":
    storage = DBStorage()
    storage.reload()
else:
    storage = FileStorage()
    storage.reload()
