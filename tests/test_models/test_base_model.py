#!/usr/bin/python3
"""
Contains the TestUser class which runs unit tests for the User class.
These tests verify inheritance, attribute types, and serialization.
"""
import unittest
from models.user import User
from models.base_model import BaseModel
from datetime import datetime


class TestUser(unittest.TestCase):
    """Defines test cases for the User class attributes and methods."""

    def test_inheritance(self):
        """Checks if User correctly inherits from BaseModel."""
        new_user = User()
        self.assertIsInstance(new_user, BaseModel)
        self.assertTrue(hasattr(new_user, "id"))
        self.assertTrue(hasattr(new_user, "created_at"))
        self.assertTrue(hasattr(new_user, "updated_at"))

    def test_class_attributes(self):
        """Verifies that User has the specific required class attributes."""
        new_user = User()
        self.assertTrue(hasattr(new_user, "email"))
        self.assertTrue(hasattr(new_user, "password"))
        self.assertTrue(hasattr(new_user, "first_name"))
        self.assertTrue(hasattr(new_user, "last_name"))

    def test_attribute_types(self):
        """Ensures that all User attributes are initialized as empty strings."""
        new_user = User()
        self.assertIsInstance(new_user.email, str)
        self.assertIsInstance(new_user.password, str)
        self.assertIsInstance(new_user.first_name, str)
        self.assertIsInstance(new_user.last_name, str)
        self.assertEqual(new_user.email, "")
        self.assertEqual(new_user.password, "")

    def test_to_dict_user(self):
        """Tests if to_dict method creates a dictionary with correct values."""
        new_user = User()
        new_user.first_name = "Betty"
        user_dict = new_user.to_dict()
        self.assertEqual(user_dict['__class__'], 'User')
        self.assertEqual(user_dict['first_name'], 'Betty')
        self.assertIsInstance(user_dict['created_at'], str)
        self.assertIsInstance(user_dict['updated_at'], str)

    def test_save_user(self):
        """Tests if the save method updates the updated_at timestamp."""
        new_user = User()
        old_update = new_user.updated_at
        new_user.save()
        self.assertNotEqual(old_update, new_user.updated_at)
        self.assertIsInstance(new_user.updated_at, datetime)

    def test_str_representation(self):
        """Ensures the __str__ output matches the required format."""
        new_user = User()
        string = "[User] ({}) {}".format(new_user.id, new_user.__dict__)
        self.assertEqual(string, str(new_user))


if __name__ == "__main__":
    unittest.main()
