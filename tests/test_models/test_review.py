#!/usr/bin/python3
"""Unit tests for Review class."""

import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """Contains unit tests for the Review class."""

    def setUp(self):
        """Set up method for each test."""
        self.review = Review()

    def test_place_id_type(self):
        """Test if place_id attribute is of type str."""
        self.assertIsInstance(self.review.place_id, str)

    def test_user_id_type(self):
        """Test if user_id attribute is of type str."""
        self.assertIsInstance(self.review.user_id, str)

    def test_text_type(self):
        """Test if text attribute is of type str."""
        self.assertIsInstance(self.review.text, str)


if __name__ == '__main__':
    unittest.main()
