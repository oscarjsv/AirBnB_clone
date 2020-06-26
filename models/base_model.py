#!/usr/bin/python3
"""BaseModel for Airbnb Project"""
import uuid
from datetime import datetime


class BaseModel():
    """Base class for classes"""

    def __init__(self):
        """Constructor"""
        uuid_gen = uuid.uuid4()

        self.id = str(uuid_gen)
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Returns string representation of an instance"""
        return("[{}] ({}) {}"
               .format(BaseModel.__name__, self.id, self.__dict__))

    def save(self):
        """Save an instance and set the updated time"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns the attributes of the instance as a dict"""
        var = self.__dict__.copy()

        var['__class__'] = BaseModel.__name__
        var['created_at'] = self.created_at.isoformat()
        var['updated_at'] = self.updated_at.isoformat()

        return var
