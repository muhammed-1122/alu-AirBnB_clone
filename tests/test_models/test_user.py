#!/usr/bin/python3
"""
Unit tests for the User class.
Includes tests for inheritance and attribute initialization.
"""
import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """Test cases for the User class."""

    def test_is_subclass(self):
        """Test that User is a subclass of BaseModel."""
        user = User()
        self.assertIsInstance(user, BaseModel)
        self.assertTrue(hasattr(user, "id"))

    def test_email_attr(self):
        """Test that User has attribute email, and it is an empty string."""
        user = User()
        self.assertTrue(hasattr(user, "email"))
        self.assertEqual(user.email, "")

    def test_password_attr(self):
        """Test that User has attribute password, and it is an empty string."""
        user = User()
        self.assertTrue(hasattr(user, "password"))
        self.assertEqual(user.password, "")

    def test_first_name_attr(self):
        """Test that User has attribute first_name, and it is an empty string."""
        user = User()
        self.assertTrue(hasattr(user, "first_name"))
        self.assertEqual(user.first_name, "")

    def test_last_name_attr(self):
        """Test that User has attribute last_name, and it is an empty string."""
        user = User()
        self.assertTrue(hasattr(user, "last_name"))
        self.assertEqual(user.last_name, "")


if __name__ == "__main__":
    unittest.main()
