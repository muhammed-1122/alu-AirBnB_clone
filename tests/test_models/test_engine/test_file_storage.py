#!/usr/bin/python3
"""
Unit tests for models/engine/file_storage.py.
Verifies serialization, deserialization, and dictionary management.
"""
import unittest
import os
import json
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage


class TestFileStorage(unittest.TestCase):
    """Test cases for the FileStorage class."""

    def setUp(self):
        """Resets the storage objects dictionary and removes file.json."""
        storage.all().clear()
        if os.path.exists("file.json"):
            os.remove("file.json")

    def tearDown(self):
        """Cleans up file.json after tests are complete."""
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_all_returns_dict(self):
        """Test that all() returns the __objects dictionary."""
        self.assertIsInstance(storage.all(), dict)

    def test_new(self):
        """Test that new() adds an object to storage properly."""
        model = BaseModel()
        key = "BaseModel." + model.id
        self.assertIn(key, storage.all())
        self.assertIs(storage.all()[key], model)

    def test_save(self):
        """Test that save() correctly serializes __objects to file.json."""
        model = BaseModel()
        model.save()
        key = "BaseModel." + model.id
        self.assertTrue(os.path.exists("file.json"))
        with open("file.json", "r") as f:
            data = json.load(f)
            self.assertIn(key, data)
            self.assertEqual(data[key]["id"], model.id)

    def test_reload(self):
        """Test that reload() correctly deserializes JSON back to objects."""
        model = BaseModel()
        model.save()
        storage.all().clear()  # Wipe memory
        storage.reload()        # Reload from disk
        key = "BaseModel." + model.id
        self.assertIn(key, storage.all())
        self.assertEqual(storage.all()[key].id, model.id)


if __name__ == "__main__":
    unittest.main()
