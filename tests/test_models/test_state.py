if __name__ == '__main__':
    unittest.main()
#!/usr/bin/python3
"""Unit tests for state.py."""
import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """Tests for the State class."""

    def test_inheritance(self):
        """Check if State inherits from BaseModel."""
        self.assertTrue(issubclass(State, BaseModel))

    def test_attributes(self):
        """Check for name attribute."""
        state = State()
        self.assertTrue(hasattr(state, "name"))
        self.assertEqual(state.name, "")

if __name__ == "__main__":
    unittest.main()
