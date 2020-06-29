#!/usr/bin/python3
    """module for task 5
    """
import json
from models.base_model import BaseModel 


class FileStorage:
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """return the dictionary
        """
    return FileStorage.__objects

    def new(self, obj):
        """new """
        var = "{} {}".format(obj.__class__.__name__, obj.id)
        self.__objects[var] = obj

    def save(self):
        temp = {}
        for key, value in self.__objects.items():
            temp[key] = value.to_dict

    def reload(self):
        pass