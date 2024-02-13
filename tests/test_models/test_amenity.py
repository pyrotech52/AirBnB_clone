#!/usr/bin/python3
"""Unittest for Amenity class"""
import unittest
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):
    """Test cases for the Amenity class"""

    def test_default_name(self):
        """Test default name attribute"""
        amenity = Amenity()
        self.assertEqual(amenity.name, "")

    def test_setting_name(self):
        """Test setting name attribute"""
        amenity = Amenity()
        amenity.name = "WiFi"
        self.assertEqual(amenity.name, "WiFi")


if __name__ == "__main__":
    unittest.main()

