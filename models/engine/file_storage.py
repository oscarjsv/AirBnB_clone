#!/usr/bin/python3
    """module for task 5
    """
import json


class FileStorage:
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """return the dictionary
        """
    return FileStorage.__objects

    def new(self, obj):
        """new """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        var = {}
        for key, value in FileStorage.__objects.items():
            var[key] = value.to_dict
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as file:
            json.dump(var, file)

    def reload(self):
        try:
            with open(FileStorage.__file_path, mode='r', encoding='utf-8') as file:
                from models.base_model import BaseModel
                temp = json.loads(file.read())
                for key, value in FileStorage.__objects.items():
                    obj = BaseModel(**value)
                    FileStorage.__objects[key] = obj
        except IOError:
            pass
                    
            

