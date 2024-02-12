#!/usr/bin/python3
"""This module defines a class to manage file storage"""
import json

class FileStorage:
    """Class that manages storage in JSON."""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """new objects to the storage"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file."""
        with open(self.__file_path, 'w') as f:
            serialized_objs = {}
            for key, value in self.__objects.items():
                serialized_objs[key] = value.to_dict()
            json.dump(serialized_objs, f)

    def reload(self):
        """Deserializes the JSON file to __objects."""
        try:
            with open(self.__file_path, 'r') as f:
                loaded_objs = json.load(f)
                for key, value in loaded_objs.items():
                    class_name, obj_id = key.split('.')
                    cls = globals()[class_name]
                    self.__objects[key] = cls(**value)
        except FileNotFoundError:
            pass

