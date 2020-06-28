#!/usr/bin/python3
"""BaseModel for Airbnb Project"""
import uuid
from datetime import datetime

time = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel():
    """Base class for classes"""

    def __init__(self, *args, **kwargs):
        """Constructor"""
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
                if hasattr(self, 'created_at') and type(self.created_at) is str:
                    self.created_at = datetime.strptime(kwargs['created_at'], time)
                if hasattr(self, 'updated_at') and type(self.updated_at) is str:
                    self.updated_at = datetime.strptime(kwargs['created_at'], time)
        else:

            uuid_gen = uuid.uuid4()
            self.id = str(uuid_gen)
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
    def __str__(self):
        """Returns string representation of an instance"""
        return("[{}] ({}) {}"
               .format(type(self).__name__, self.id, self.__dict__))

    def save(self):
        """Save an instance and set the updated time"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns the attributes of the instance as a dict"""
        var = self.__dict__.copy()

        var['__class__'] = type(self).__name__
        var['created_at'] = self.created_at.isoformat()
        var['updated_at'] = self.updated_at.isoformat()

        return var
