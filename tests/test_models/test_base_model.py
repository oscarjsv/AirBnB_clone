#!/usr/bin/python3
"""Module for test base_model"""
from .test_class import TestClassDocumentation
from datetime import datetime
from models.base_model import BaseModel
from time import sleep
from unittest import TestCase


class TestBaseModel(TestCase):
    """Test cases for Base model"""

    def test_code_review(self):
        """Test documentation and pep8"""
        t = TestClassDocumentation(self, BaseModel)
        t.documentation()
        t.pep8(['models/base_model.py',
                'tests/test_models/test_base_model.py'])

    def test_init(self):
        """Test constructor of base model"""
        obj = BaseModel()
        now = datetime.now().replace(microsecond=0)

        self.assertIsInstance(obj, BaseModel)
        self.assertIsInstance(repr(obj), str)
        self.assertIsInstance(obj.id, str)
        self.assertIsInstance(obj.updated_at, datetime)
        self.assertIsInstance(obj.created_at, datetime)
        self.assertEqual(obj.created_at.replace(microsecond=0), now)
        self.assertEqual(obj.updated_at.replace(microsecond=0), now)

    def test_save(self):
        """Test save method"""
        obj = BaseModel()
        sleep(1)

        now = datetime.now().replace(microsecond=0)
        obj.save()

        self.assertEqual(obj.updated_at.replace(microsecond=0),
                         now)

    def test_dictionary(self):
        """Test to_dict method"""
        output = BaseModel().to_dict()

        self.assertIsInstance(output, dict)
