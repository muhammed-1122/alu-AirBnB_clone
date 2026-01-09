#!/usr/bin/python3
"""Unit tests for state.py"""
import unittest
from models.state import State

class TestState(unittest.TestCase):
    """Basic tests for state"""
    def test_exists(self):
        """Check if class exists"""
        new = State()
        self.assertIsNotNone(new)

if __name__ == '__main__':
    unittest.main()
