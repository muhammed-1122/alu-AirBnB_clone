#!/usr/bin/python3
"""Unit tests for models/engine/file_storage.py."""
import unittest
import os
import json
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage


class TestFileStorage(unittest.TestCase):
    """Test cases for FileStorage."""

    def test_all_returns_dict(self):
        """Test that all() returns a dictionary."""
        self.assertIsInstance(storage.all(), dict)

    def test_new(self):
        """Test that new() adds an object to __objects."""
        model = BaseModel()
        storage.new(model)
        key = "BaseModel." + model.id
        self.assertIn(key, storage.all())

    def test_save_and_reload(self):
        """Test serialization and deserialization."""
        model = BaseModel()
        model.name = "Test_Model"
        model.save()
        
        # Create a new storage instance to simulate a fresh start
        new_storage = FileStorage()
        new_storage.reload()
        key = "BaseModel." + model.id
        self.assertIn(key, new_storage.all())
        self.assertEqual(new_storage.all()[key].name, "Test_Model")

    def tearDown(self):
        """Clean up file.json after tests."""
        if os.path.exists("file.json"):
            os.remove("file.json")


if __name__ == "__main__":
    unittest.main()
