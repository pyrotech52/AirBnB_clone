#!/usr/bin/python3
"""Unit tests for Place class."""

import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """Contains unit tests for the Place class."""

    def setUp(self):
        """Set up method for each test."""
        self.place = Place()

    def test_city_id_type(self):
        """Test if city_id attribute is of type str."""
        self.assertIsInstance(self.place.city_id, str)

    def test_user_id_type(self):
        """Test if user_id attribute is of type str."""
        self.assertIsInstance(self.place.user_id, str)

    def test_name_type(self):
        """Test if name attribute is of type str."""
        self.assertIsInstance(self.place.name, str)

    def test_description_type(self):
        """Test if description attribute is of type str."""
        self.assertIsInstance(self.place.description, str)

    def test_number_rooms_type(self):
        """Test if number_rooms attribute is of type int."""
        self.assertIsInstance(self.place.number_rooms, int)

    def test_number_bathrooms_type(self):
        """Test if number_bathrooms attribute is of type int."""
        self.assertIsInstance(self.place.number_bathrooms, int)

    def test_max_guest_type(self):
        """Test if max_guest attribute is of type int."""
        self.assertIsInstance(self.place.max_guest, int)

    def test_price_by_night_type(self):
        """Test if price_by_night attribute is of type int."""
        self.assertIsInstance(self.place.price_by_night, int)

    def test_latitude_type(self):
        """Test if latitude attribute is of type float."""
        self.assertIsInstance(self.place.latitude, float)

    def test_longitude_type(self):
        """Test if longitude attribute is of type float."""
        self.assertIsInstance(self.place.longitude, float)

    def test_amenity_ids_type(self):
        """Test if amenity_ids attribute is of type list."""
        self.assertIsInstance(self.place.amenity_ids, list)


if __name__ == '__main__':
    unittest.main()
