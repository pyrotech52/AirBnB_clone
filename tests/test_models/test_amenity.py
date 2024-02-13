#!/usr/bin/python3
"""Defines unit tests for Amenity class."""


import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Contains unit tests for the Amenity class."""

    def test_name_type(self):
        """Test if the name attribute is of type str."""
        amenity = Amenity()
        self.assertIsInstance(amenity.name, str)


if __name__ == '__main__':
    unittest.main()
