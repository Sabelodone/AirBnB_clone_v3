#!/usr/bin/python3
"""
Contains the FileStorage class
"""

import json
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


class FileStorage:
    """serializes instances to a JSON file & deserializes back to instances"""

    # string - path to the JSON file
    __file_path = "file.json"
    # dictionary - empty but will store all objects by <class name>.id
    __objects = {}

    def all(self, cls=None):
        '''Retrieve all objects or objects of a specific class from the file storage.'''
        if cls:
            return {key: value for key, value in self.__objects.items() if isinstance(value, cls)}
        return self.__objects or {}

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        if obj is not None:
            key = obj.__class__.__name__ + "." + obj.id
            self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        json_objects = {}
        for key in self.__objects:
            json_objects[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(json_objects, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r') as f:
                jo = json.load(f)
            for key in jo:
                self.__objects[key] = classes[jo[key]["__class__"]](**jo[key])
        except:
            pass

    def delete(self, obj=None):
        """delete obj from __objects if it’s inside"""
        if obj is not None:
            key = obj.__class__.__name__ + '.' + obj.id
            if key in self.__objects:
                del self.__objects[key]

    def close(self):
        """call reload() method for deserializing the JSON file to objects"""
        self.reload()

    def get(self, obj_class, obj_id):
        '''Retrieve an object from the file storage by class and id.'''
        if obj_class in classes.values() and obj_id and isinstance(obj_id, str):
            objects = self.get_all_objects(obj_class)
            for key, value in objects.items():
                if key.split(".")[1] == obj_id:
                    return value
        return None

    def count(self, obj_class=None):
        '''Count the number of objects in file storage matching the given class.'''
        objects_data = self.get_all_objects(obj_class)
        return len(objects_data) if obj_class in classes.values() else 0

    def get_all_objects(self, obj_class=None):
        '''Retrieve all objects from the file storage for a given class.'''
        if self.__objects is None:
            return {}  # Return an empty dictionary if __objects is None

        objects_data = {}
        if obj_class:
            for key, value in self.__objects.items():
                if obj_class == value.__class__:
                    objects_data[key] = value
        else:
            objects_data = self.__objects

        return objects_data

