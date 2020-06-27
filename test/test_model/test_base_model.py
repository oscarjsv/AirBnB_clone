#!/usr/bin/python3
""" Test cases for task 0"""
import unittest
import pep8 as pycodestyle
import time
from datetime import datetime
from models.base_model import BaseModel


class testmodelbaseDocs(unittest.TestCase):
    """Tests to check the documentation and style of BaseModel class"""

    @classmethod
    def setUpClass(self):
        """Set up for docstring tests"""
        self.base_funcs = inspect.getmembers(BaseModel, inspect.isfunction)

    def test_pep8_conformance_rectangle(self):
         """Test that models/base_model.py conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_rectangle(self):
        """Test that tests/test_models/test_base_model.py conforms to PEP8."""

        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_models/test_base_model.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_module_docstring(self):
        """Tests for the presence of a module docstring"""
        self.assertTrue(len(module_doc.__doc__) >= 1)

    def test_class_docstring(self):
        """Tests for the presence of a class docstring"""
        self.assertTrue(len(BaseModel.__doc__) >= 1)

    def test_func_docstrings(self):
        """Tests for the presence of docstrings in all functions"""
        for func in self.base_funcs:
            self.assertTrue(len(func[1].__doc__) >= 1)

class TestBaseModel(unittest.TestCase):
    """Test the BaseModel class"""
    def test_datetime_attributes(self):
        b = BaseModel()
        b1 = BaseMOdel()
        self.assertTrue(b.created_at, b.created_at)
        self.assertEqual(b.created_at, b.created_a)
        self.assertNotEqual(b.created_at, b1.created_a)


    def test_uuid(self):
        """ test tha uuid method"""
        b = BaseModel()
        self.assertTrue(b.id, ins.id)
        self.assertNotEqual(b.id, 2)
        self.assertNotEqual(b.id, "string")

    def test_str(self):
        """test that the str method has the correct output"""
        b = BaseModel()
        string = "[BaseModel] ({}) {}".format(b.id, b.__dict__)
        self.assertEqual(string, str(b))

    def test_dict(self):
        """ test for the method to_dict """
        my_model = BaseModel()
        my_model.name = "Holberton"
        my_model.my_number = 89
        dic = my_model.to_dict()
        atri = ["id",
                "created_at",
                "pdated_at",
                "name",
                "my_number",
                "__class__"]
        self.asertCountEqual(dic.keys(), atri)
        self.assertEqual(dic['__class__'], 'BaseModel')
        self.assertEqual(dic['name'], "Holberton")
        self.assertEqual(dic['my_number'], 89)
