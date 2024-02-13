#!/usr/bin/python3
""" defines unittests for base model"""

import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.model = BaseModel()

    def test_instance_attributes(self):
        self.assertTrue(hasattr(self.model, 'id'))
        self.assertTrue(hasattr(self.model, 'created_at'))
        self.assertTrue(hasattr(self.model, 'updated_at'))
        self.assertIsInstance(self.model.id, str)
        self.assertIsInstance(self.model.created_at, datetime)
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_save_method(self):
        previous_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(previous_updated_at, self.model.updated_at)

    def test_to_dict_method(self):
        obj_dict = self.model.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertIn('__class__', obj_dict)
        self.assertIn('id', obj_dict)
        self.assertIn('created_at', obj_dict)
        self.assertIn('updated_at', obj_dict)

    def test_str_method(self):
        self.assertIn("[BaseModel]", str(self.model))
        self.assertIn("'id':", str(self.model))
        self.assertIn("'created_at':", str(self.model))
        self.assertIn("'updated_at':", str(self.model))


if __name__ == '__main__':
    unittest.main()
