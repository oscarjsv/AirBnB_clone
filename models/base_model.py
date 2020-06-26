#!/usr/bin/python3


import uuid
from datetime import datetime


class BaseModel():
    """class model """

    def __init__(self):
        """comentario"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """comentario"""
        return("[{}] ({}) {}".format(BaseModel.__name__, self.id, self.__dict__))

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        var = self.__dict__.copy()
        var["__class__"] = BaseModel.__name__
        var["created_at"] = self.created_at.isoformat()
        var["updated_at"] = self.updated_at.isoformat()
        return var
