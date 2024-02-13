#!/usr/bin/python3
"""Unit tests for City class."""

import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """Contains unit tests for the City class."""

    def setUp(self):
        """Set up method for each test."""
        self.city = City()

    def test_state_id_type(self):
        """Test if state_id attribute is of type str."""
        self.assertIsInstance(self.city.state_id, str)

    def test_name_type(self):
        """Test if name attribute is of type str."""
        self.assertIsInstance(self.city.name, str)


if __name__ == '__main__':
    unittest.main()
