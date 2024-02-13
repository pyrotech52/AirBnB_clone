#!/usr/bin/python3
"""Unit tests for State class."""
from tests.test_models.test_base_model import TestBaseModel
from models.state import State

class TestState(TestBaseModel):
    """Test cases for the State class."""

    def __init__(self, *args, **kwargs):
        """Initialize a new State instance for testing."""
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name_attribute(self):
        """Test if the name attribute of State is a string."""
        new_state = self.value()
        self.assertIsInstance(new_state.name, str)

if __name__ == '__main__':
    unittest.main()

