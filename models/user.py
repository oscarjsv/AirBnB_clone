#!/usr/bin/python3
    """moldule for the user
    """

from base_model import BaseModel

class User(BaseModel):
    """class user

    Args:
        BaseModel (super class):
    """
    email = ""
    password = ""
    first_name ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)