#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import TestBaseModel
from models.city import City

class TestCity(TestBaseModel):
    """Test cases for the City class"""

    def __init__(self, *args, **kwargs):
        """Initializes a new City instance for testing"""
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id_attribute(self):
        """Test if the state_id attribute of City is a string"""
        new_city = self.value()
        self.assertIsInstance(new_city.state_id, str)

    def test_name_attribute(self):
        """Test if the name attribute of City is a string"""
        new_city = self.value()
        self.assertIsInstance(new_city.name, str)

    # Add more test cases as needed

if __name__ == "__main__":
    unittest.main()

