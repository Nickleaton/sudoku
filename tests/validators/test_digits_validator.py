import unittest

from src.board.board import Board
from src.validators.validator import Validator
from tests.validators.test_validator import TestValidator


class TestValidatorModule(TestValidator):
    """Test case for the Validator class."""

    def setUp(self):
        """Set up the board and test data for each test."""
        super().setUp()  # Call the setup of the base TestValidator class
        self.board = Board(6, 6, 2, 3, {})  # Example board setup
        self.valid_input_data = {
            'digits': [1, 2, 3]
        }
        self.invalid_input_data = {
            'digits': [1, 2, 10]  # 10 is outside the valid range (assuming board.digit_range doesn't contain 10)
        }
        self.missing_digits_data = {
            'other_key': 'value'
        }

    def test_validate_valid(self):
        """Test that validate returns no errors for valid digits."""
        errors = Validator.validate(self.board, self.valid_input_data)
        self.assertEqual(errors, [], "Expected no validation errors for valid digits.")

    def test_validate_invalid_digit(self):
        """Test that validate returns an error for an invalid digit."""
        errors = Validator.validate(self.board, self.invalid_input_data)
        self.assertIn('Invalid digit: 10', errors, "Expected error for invalid digit.")

    def test_validate_missing_digits(self):
        """Test that validate returns an error for missing 'digits' key."""
        errors = Validator.validate(self.board, self.missing_digits_data)
        self.assertIn('Missing key: "digits"', errors, "Expected error for missing 'digits' key.")


if __name__ == '__main__':
    unittest.main()
