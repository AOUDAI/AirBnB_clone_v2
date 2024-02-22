#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        return self.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        class_name = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[class_name] = obj

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Deserializes the JSON file to __objects (only if the file exists)"""
        try:
            with open(self.__file_path, 'r') as file:
                data = json.load(file)
            for obj in data.values():
                class_name = obj["__class__"]
                self.new(eval(class_name)(**obj))
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """delete obj from __objects"""
        if (obj):
            className = f"{obj.__class__.__name__}.{obj.id}"
            try:
                del self.__objects[className]
            except KeyError:
                pass
    