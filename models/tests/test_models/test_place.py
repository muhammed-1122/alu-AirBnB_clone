#!/usr/bin/python3
"""Unit tests for place.py"""
import unittest
from models.place import Place

class TestPlace(unittest.TestCase):
    """Basic tests for place"""
    def test_exists(self):
        """Check if class exists"""
        new = Place()
        self.assertIsNotNone(new)

if __name__ == '__main__':
    unittest.main()
