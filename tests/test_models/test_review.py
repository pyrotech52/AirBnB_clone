#!/usr/bin/python3
"""Unit tests for Review class."""
from tests.test_models.test_base_model import TestBaseModel
from models.review import Review

class TestReview(TestBaseModel):
    """Test cases for the Review class."""

    def __init__(self, *args, **kwargs):
        """Initialize a new Review instance for testing."""
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id_attribute(self):
        """Test if the place_id attribute of Review is a string."""
        new_review = self.value()
        self.assertIsInstance(new_review.place_id, str)

    def test_user_id_attribute(self):
        """Test if the user_id attribute of Review is a string."""
        new_review = self.value()
        self.assertIsInstance(new_review.user_id, str)

    def test_text_attribute(self):
        """Test if the text attribute of Review is a string."""
        new_review = self.value()
        self.assertIsInstance(new_review.text, str)

if __name__ == '__main__':
    unittest.main()

