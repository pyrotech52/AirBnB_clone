#!/usr/bin/python3
"""Unit tests for User class."""

import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """Contains unit tests for the User class."""

    def setUp(self):
        """Set up method for each test."""
        self.user = User()

    def test_first_name_type(self):
        """Test if first_name attribute is of type str."""
        self.assertIsInstance(self.user.first_name, str)

    def test_last_name_type(self):
        """Test if last_name attribute is of type str."""
        self.assertIsInstance(self.user.last_name, str)

    def test_email_type(self):
        """Test if email attribute is of type str."""
        self.assertIsInstance(self.user.email, str)

    def test_password_type(self):
        """Test if password attribute is of type str."""
        self.assertIsInstance(self.user.password, str)


if __name__ == '__main__':
    unittest.main()
