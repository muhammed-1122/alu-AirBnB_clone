#!/usr/bin/python3
"""
Module for FileStorage class.
Handles serialization and deserialization of instances to JSON.
"""
import json


class FileStorage:
    """Serializes instances to a JSON file and deserializes back."""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        if obj:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file."""
        obj_dict = {}
        for key, obj in self.__objects.items():
            obj_dict[key] = obj.to_dict()
        with open(self.__file_path, 'w', encoding="utf-8") as f:
            json.dump(obj_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects."""
        # Moving imports here prevents circular dependency crashes
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        classes = {
            "BaseModel": BaseModel, "User": User, "State": State,
            "City": City, "Amenity": Amenity, "Place": Place,
            "Review": Review
        }
        try:
            with open(self.__file_path, 'r', encoding="utf-8") as f:
                jo = json.load(f)
            for k, v in jo.items():
                cls_name = v['__class__']
                if cls_name in classes:
                    self.new(classes[cls_name](**v))
        except FileNotFoundError:
            pass
