#!/usr/bin/python3
"""Unit tests for models/base_model.py."""
import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class."""

    def test_initialization(self):
        """Test attributes are correctly assigned on init."""
        model = BaseModel()
        self.assertIsInstance(model.id, str)
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)

    def test_str_representation(self):
        """Test the __str__ method output."""
        model = BaseModel()
        model_str = str(model)
        self.assertIn("[BaseModel]", model_str)
        self.assertIn(model.id, model_str)

    def test_save(self):
        """Test that save() updates updated_at."""
        model = BaseModel()
        old_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(old_updated_at, model.updated_at)

    def test_to_dict(self):
        """Test dictionary representation."""
        model = BaseModel()
        m_dict = model.to_dict()
        self.assertEqual(m_dict["__class__"], "BaseModel")
        self.assertIsInstance(m_dict["created_at"], str)
        self.assertIsInstance(m_dict["updated_at"], str)

    def test_init_with_kwargs(self):
        """Test initialization with a dictionary."""
        date = datetime.now().isoformat()
        kwargs = {
            "id": "123",
            "created_at": date,
            "updated_at": date,
            "name": "ALU"
        }
        model = BaseModel(**kwargs)
        self.assertEqual(model.id, "123")
        self.assertEqual(model.name, "ALU")
        self.assertIsInstance(model.created_at, datetime)


if __name__ == "__main__":
    unittest.main()
