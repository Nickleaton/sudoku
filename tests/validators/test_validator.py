import unittest

from src.board.board import Board
from src.validators.validator import Validator  # Assuming the Validator class is in src/validator.py


class TestValidator(unittest.TestCase):
    """Test case for the Validator class."""

    def setUp(self):
        """Set up the board and test data for each test."""
        self.board = Board(6, 6, 2, 3, {})
        self.valid_input_data = {
            'key1': 'value1',
            'key2': 'value2'
        }
        self.invalid_input_data = {
            'key1': 'value1'
            # Missing 'key2'
        }
        self.required_keys = ['key1', 'key2']

    def test_validate_keys_valid(self):
        """Test that validate_keys returns no errors for valid keys."""
        errors = Validator.validate_keys(self.valid_input_data, self.required_keys)
        self.assertEqual(errors, [], "Expected no validation errors for valid keys.")

    def test_validate_keys_missing_key(self):
        """Test that validate_keys returns an error for missing required key."""
        errors = Validator.validate_keys(self.invalid_input_data, self.required_keys)
        self.assertIn('Missing key: "key2"', errors, "Expected error for missing 'key2'.")

    def test_validate_no_errors(self):
        """Test the base validate method returns no errors by default."""
        errors = Validator.validate(self.board, self.valid_input_data)
        self.assertEqual(errors, [], "Expected no validation errors by default.")


if __name__ == '__main__':
    unittest.main()
