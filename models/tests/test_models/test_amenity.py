#!/usr/bin/python3
"""Unit tests for amenity.py"""
import unittest
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):
    """Basic tests for amenity"""
    def test_exists(self):
        """Check if class exists"""
        new = Amenity()
        self.assertIsNotNone(new)

if __name__ == '__main__':
    unittest.main()
