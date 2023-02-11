#!/usr/bin/python3
"""
serializes instances to a JSON file and
deserializes JSON file to instances
"""
from json import load, dump
import os


class FileStorage:
    """Defines all common attributes/methods"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <className>.id"""
        key = f'{obj.__class__.__name__}.{obj.id}'
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes objects in __objects to
        the JSON file specified in __file_path
        """
        dictionary = {}

        for key, value in FileStorage.__objects.items():
            dictionary[key] = value.to_dict()

        with open(FileStorage.__file_path, 'w') as f:
            dump(dictionary, f)

    def reload(self):
        """deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists;
        otherwise, do nothing. If the file doesn't exist,
        no exception should be raised)
        """
        from models.base_model import BaseModel

        model_dict = {'BaseModel': BaseModel}

        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as f:
                for k, value in load(f).items():
                    self.new(model_dict[value['__class__']](**value))
