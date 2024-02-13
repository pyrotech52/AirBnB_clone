#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import TestBaseModel
from models.place import Place

class TestPlace(TestBaseModel):
    """Test cases for the Place class"""

    def __init__(self, *args, **kwargs):
        """Initializes a new Place instance for testing"""
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id_attribute(self):
        """Test if the city_id attribute of Place is a string"""
        new_place = self.value()
        self.assertIsInstance(new_place.city_id, str)

    def test_user_id_attribute(self):
        """Test if the user_id attribute of Place is a string"""
        new_place = self.value()
        self.assertIsInstance(new_place.user_id, str)

    def test_name_attribute(self):
        """Test if the name attribute of Place is a string"""
        new_place = self.value()
        self.assertIsInstance(new_place.name, str)

    def test_description_attribute(self):
        """Test if the description attribute of Place is a string"""
        new_place = self.value()
        self.assertIsInstance(new_place.description, str)

    def test_number_rooms_attribute(self):
        """Test if the number_rooms attribute of Place is an integer"""
        new_place = self.value()
        self.assertIsInstance(new_place.number_rooms, int)

    def test_number_bathrooms_attribute(self):
        """Test if the number_bathrooms attribute of Place is an integer"""
        new_place = self.value()
        self.assertIsInstance(new_place.number_bathrooms, int)

    def test_max_guest_attribute(self):
        """Test if the max_guest attribute of Place is an integer"""
        new_place = self.value()
        self.assertIsInstance(new_place.max_guest, int)

    def test_price_by_night_attribute(self):
        """Test if the price_by_night attribute of Place is an integer"""
        new_place = self.value()
        self.assertIsInstance(new_place.price_by_night, int)

    def test_latitude_attribute(self):
        """Test if the latitude attribute of Place is a float"""
        new_place = self.value()
        self.assertIsInstance(new_place.latitude, float)

    def test_longitude_attribute(self):
        """Test if the longitude attribute of Place is a float"""
        new_place = self.value()
        self.assertIsInstance(new_place.longitude, float)

    def test_amenity_ids_attribute(self):
        """Test if the amenity_ids attribute of Place is a list"""
        new_place = self.value()
        self.assertIsInstance(new_place.amenity_ids, list)

