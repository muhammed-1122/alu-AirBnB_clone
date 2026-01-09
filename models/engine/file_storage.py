#!/usr/bin/python3
"""Module for FileStorage class."""
import json


class FileStorage:
    """Serializes instances to a JSON file and deserializes back."""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file."""
        obj_dict = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(obj_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects."""
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
            with open(self.__file_path, 'r') as f:
                jo = json.load(f)
            for k, v in jo.items():
                cls_name = v['__class__']
                if cls_name in classes:
                    # This recreates the instance using the dictionary
                    self.new(classes[cls_name](**v))
        except FileNotFoundError:
            pass
