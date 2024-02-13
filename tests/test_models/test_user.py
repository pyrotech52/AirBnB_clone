#!/usr/bin/python3
"""Unit tests for User class."""
from tests.test_models.test_base_model import TestBaseModel
from models.user import User

class TestUser(TestBaseModel):
    """Test cases for the User class."""

    def __init__(self, *args, **kwargs):
        """Initialize a new User instance for testing."""
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name_attribute(self):
        """Test if the first_name attribute of User is a string."""
        new_user = self.value()
        self.assertIsInstance(new_user.first_name, str)

    def test_last_name_attribute(self):
        """Test if the last_name attribute of User is a string."""
        new_user = self.value()
        self.assertIsInstance(new_user.last_name, str)

    def test_email_attribute(self):
        """Test if the email attribute of User is a string."""
        new_user = self.value()
        self.assertIsInstance(new_user.email, str)

    def test_password_attribute(self):
        """Test if the password attribute of User is a string."""
        new_user = self.value()
        self.assertIsInstance(new_user.password, str)

if __name__ == '__main__':
    unittest.main()

