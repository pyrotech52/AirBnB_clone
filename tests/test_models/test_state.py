#!/usr/bin/python3
"""Unit tests for State class."""

import unittest
from models.state import State


class TestState(unittest.TestCase):
    """Contains unit tests for the State class."""

    def setUp(self):
        """Set up method for each test."""
        self.state = State()

    def test_name_type(self):
        """Test if name attribute is of type str."""
        self.assertIsInstance(self.state.name, str)


if __name__ == '__main__':
    unittest.main()
