#!/usr/bin/python3
"""Unit tests for city.py"""
import unittest
from models.city import City

class TestCity(unittest.TestCase):
    """Basic tests for city"""
    def test_exists(self):
        """Check if class exists"""
        new = City()
        self.assertIsNotNone(new)

if __name__ == '__main__':
    unittest.main()
