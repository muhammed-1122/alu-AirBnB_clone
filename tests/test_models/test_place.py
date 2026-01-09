#!/usr/bin/python3
"""
This module contains the TestPlace class which verifies the 
functionality of the Place class attributes and inheritance.
"""
import unittest
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    """Tests the initialization and attributes of the Place class."""

    def test_inheritance(self):
        """Checks if Place correctly inherits from BaseModel."""
        new_place = Place()
        self.assertIsInstance(new_place, BaseModel)

    def test_attributes(self):
        """Verifies that Place has all the required class attributes."""
        p = Place()
        self.assertTrue(hasattr(p, "city_id"))
        self.assertTrue(hasattr(p, "user_id"))
        self.assertTrue(hasattr(p, "name"))
        self.assertTrue(hasattr(p, "description"))
        self.assertTrue(hasattr(p, "number_rooms"))
        self.assertTrue(hasattr(p, "number_bathrooms"))
        self.assertTrue(hasattr(p, "max_guest"))
        self.assertTrue(hasattr(p, "price_by_night"))
        self.assertTrue(hasattr(p, "latitude"))
        self.assertTrue(hasattr(p, "longitude"))
        self.assertTrue(hasattr(p, "amenity_ids"))

    def test_attribute_defaults(self):
        """Ensures that attributes are initialized with correct types and defaults."""
        p = Place()
        self.assertEqual(p.name, "")
        self.assertEqual(p.number_rooms, 0)
        self.assertEqual(p.latitude, 0.0)
        self.assertIsInstance(p.amenity_ids, list)


if __name__ == "__main__":
    unittest.main()
