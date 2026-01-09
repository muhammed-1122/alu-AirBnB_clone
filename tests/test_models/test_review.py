#!/usr/bin/python3
"""Unit tests for review.py"""
import unittest
from models.review import Review

class TestReview(unittest.TestCase):
    """Basic tests for review"""
    def test_exists(self):
        """Check if class exists"""
        new = Review()
        self.assertIsNotNone(new)

if __name__ == '__main__':
    unittest.main()
