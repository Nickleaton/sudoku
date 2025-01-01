import unittest

from src.validators.known_validator import \
    KnownValidator  # Assuming KnownValidator is in src/validators/known_validator.py
from tests.validators.test_validator import TestValidator


class TestKnownValidator(TestValidator):
    """Test case for the KnownValidator class."""

    def setUp(self):
        super().setUp()
        """Set up the board and test input_data for each test."""
        self.valid_input_data = {
            'Known': [
                '123456',  # Row 1
                '234561',  # Row 2
                '345612',  # Row 3
                '4oe123',  # Row 4
                '.....4',  # Row 5
                '678901'  # Row 6
            ]
        }
        self.invalid_input_data = {
            'Known': [
                '12345X',  # Row 1: Invalid character 'X'
                '234567',  # Row 2
                '345678',  # Row 3
                '456789',  # Row 4
                '567890',  # Row 5
                '678901'  # Row 6
            ]
        }
        self.missing_known_data = {
            'SomeOtherKey': 'integer_value'
        }

    def test_validate_valid(self):
        """Test that validate returns no errors for valid 'Known' input_data."""
        errors = KnownValidator.validate(self.board, self.valid_input_data)
        self.assertEqual(errors, [], "Expected no validation errors for valid 'Known' input_data.")

    def test_validate_invalid_character(self):
        """Test that validate returns an error for an invalid character in the 'Known' input_data."""
        errors = KnownValidator.validate(self.board, self.invalid_input_data)
        self.assertIn("Invalid digit/type 'X' at row 1, column 6", errors, "Expected error for invalid character 'X'.")

    def test_validate_row_length_mismatch_long(self):
        """Test that validate returns an error for row length mismatch."""
        invalid_row_length_data = {
            'Known': [
                '1234567',  # Row 1: Extra column
                '234561',  # Row 2
                '234561',  # Row 3
                '234561',  # Row 4
                '234561',  # Row 5
                '234561'  # Row 6
            ]
        }
        errors = KnownValidator.validate(self.board, invalid_row_length_data)
        self.assertIn('Row 1 has 7 columns, but the board has 6 columns.', errors,
                      "Expected error for row length mismatch.")

    def test_validate_row_length_mismatch_short(self):
        """Test that validate returns an error for row length mismatch."""
        invalid_row_length_data = {
            'Known': [
                '12347',  # Row 1: Short column
                '234561',  # Row 2
                '234561',  # Row 3
                '234561',  # Row 4
                '234561',  # Row 5
                '234561'  # Row 6
            ]
        }
        errors = KnownValidator.validate(self.board, invalid_row_length_data)
        self.assertIn('Row 1 has 7 columns, but the board has 6 columns.', errors,
                      "Expected error for row length mismatch.")

    def test_validate_missing_known_key(self):
        """Test that validate returns an error for missing 'Known' key in input input_data."""
        errors = KnownValidator.validate(self.board, self.missing_known_data)
        self.assertIn("Missing key 'Known' in the input_data.", errors, "Expected error for missing 'Known' key.")

    def test_validate_row_count_mismatch(self):
        """Test that validate returns an error for row count mismatch."""
        invalid_row_count_data = {
            'Known': [
                '123456',  # Row 1
                '234567',  # Row 2
            ]
        }
        errors = KnownValidator.validate(self.board, invalid_row_count_data)
        self.assertIn('Number of rows 2 does not match the row count (6).', errors,
                      "Expected error for row count mismatch.")


if __name__ == '__main__':
    unittest.main()
