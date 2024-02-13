#!/usr/bin/python3
"""Unit tests for FileStorage class."""

import unittest
import os
import json
from models.base_model import BaseModel
from models import storage


class TestFileStorage(unittest.TestCase):
    """Test cases for the FileStorage class."""

    def setUp(self):
        """Set up the test environment."""
        del_list = []
        for key in storage._FileStorage__objects.keys():
            del_list.append(key)
        for key in del_list:
            del storage._FileStorage__objects[key]

    def tearDown(self):
        """Remove the storage file at the end of tests."""
        try:
            os.remove('file.json')
        except FileNotFoundError:
            pass

    def test_obj_list_empty(self):
        """Check if __objects is initially empty."""
        self.assertEqual(len(storage.all()), 0)

    def test_new(self):
        """Test if a new object is correctly added to __objects."""
        new = BaseModel()
        for obj in storage.all().values():
            temp = obj
        self.assertTrue(temp is obj)

    def test_all(self):
        """Check if __objects is properly returned."""
        new = BaseModel()
        temp = storage.all()
        self.assertIsInstance(temp, dict)

    def test_base_model_instantiation(self):
        """Check that no file is created on BaseModel save."""
        new = BaseModel()
        self.assertFalse(os.path.exists('file.json'))

    def test_empty(self):
        """Check if data is saved to file."""
        new = BaseModel()
        thing = new.to_dict()
        new.save()
        new2 = BaseModel(**thing)
        self.assertNotEqual(os.path.getsize('file.json'), 0)

    def test_save(self):
        """Test the save method of FileStorage."""
        new = BaseModel()
        storage.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_reload(self):
        """Test if the storage file is successfully loaded to __objects."""
        new = BaseModel()
        storage.save()
        storage.reload()
        for obj in storage.all().values():
            loaded = obj
        self.assertEqual(new.to_dict()['id'], loaded.to_dict()['id'])

    def test_reload_empty(self):
        """Test loading from an empty file."""
        with open('file.json', 'w') as f:
            pass
        with self.assertRaises(ValueError):
            storage.reload()

    def test_reload_from_nonexistent(self):
        """Test if nothing happens if file does not exist."""
        self.assertEqual(storage.reload(), None)

    def test_base_model_save(self):
        """Test if BaseModel save method calls storage save."""
        new = BaseModel()
        new.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_type_path(self):
        """Confirm that __file_path is a string."""
        self.assertEqual(type(storage._FileStorage__file_path), str)

    def test_type_objects(self):
        """Confirm that __objects is a dictionary."""
        self.assertEqual(type(storage.all()), dict)

    def test_key_format(self):
        """Check if the key is properly formatted."""
        new = BaseModel()
        _id = new.to_dict()['id']
        for key in storage.all().keys():
            temp = key
        self.assertEqual(temp, 'BaseModel' + '.' + _id)

    def test_storage_var_created(self):
        """Check if FileStorage object storage is created."""
        from models.engine.file_storage import FileStorage
        self.assertEqual(type(storage), FileStorage)


if __name__ == '__main__':
    unittest.main()
