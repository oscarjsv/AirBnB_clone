#!/usr/bin/python3
"""Module for define console actions"""
from models.base_model import BaseModel
from models.user import User
from models import storage


class Actions:
    """Handle console actions"""
    __classes = {'BaseModel': BaseModel, 'User': User}

    @staticmethod
    def class_exists(class_name):
        """Check if the class exists"""
        classes = Actions.__classes.keys()
        return class_name in set(classes)

    @staticmethod
    def valid_arguments(arg):
        """Check if the argument (tuple) is valid"""
        if not arg:
            print('** class name missing **')
            return False

        k_class = arg[0]
        if not Actions.class_exists(k_class):
            print('** class doesn\'t exist **')
            return False

        return True

    @staticmethod
    def tuple2value(arg, idx):
        """Returns the value of a tuple, or None"""
        return None if len(arg) < idx + 1 else arg[idx]

    @staticmethod
    def object_exists(arg):
        """Check if the id is a valid object id"""
        # id_obj = None if len(arg) < 2 else arg[1]
        id_obj = Actions.tuple2value(arg, 1)
        if not id_obj:
            print('** instance id missing **')
            return

        obj = storage.get_object(arg[0], id_obj)
        if obj is None:
            print('** no instance found **')
            return None

        return obj

    @staticmethod
    def create(arg):
        """Create a new instance of class @arg[0]"""
        if not Actions.valid_arguments(arg):
            return

        k_class = arg[0]
        obj = Actions.__classes[k_class]()
        obj.save()
        print(obj.id)

    @staticmethod
    def show(arg):
        """Show an instance"""
        if not Actions.valid_arguments(arg):
            return

        obj = Actions.object_exists(arg)
        if not obj:
            return

        print(obj)

    @staticmethod
    def destroy(arg):
        """Destroy an instance"""
        if not Actions.valid_arguments(arg):
            return

        obj = Actions.object_exists(arg)
        if not obj:
            return

        storage.delete(arg[0], arg[1])
        storage.save()

    @staticmethod
    def all(arg):
        """Prints string representation of all instances based"""
        if not arg:
            print(storage.get_objects())
            return

        class_name = arg[0]
        if not Actions.class_exists(class_name):
            print('** class doesn\'t exist **')
            return

        print(storage.get_objects(class_name))

    @staticmethod
    def update(arg):
        """Update an instance"""
        if not Actions.valid_arguments(arg):
            return

        obj = Actions.object_exists(arg)
        if not obj:
            return

        attribute = Actions.tuple2value(arg, 2)
        if not attribute:
            print('** attribute name missing **')
            return

        value = Actions.tuple2value(arg, 3)
        if not value:
            print('** value missing **')
            return

        cast_type = type(attribute).__name__
        value = eval('{}(value)'.format(cast_type))
        setattr(obj, attribute, value.lstrip('"').rstrip('"'))
        storage.save()
