import unittest

from src.validators.none_validator import NoneValidator
from tests.validators.test_validator import TestValidator


class TestNoneValidator(TestValidator):
    """Test case for the NoneValidator class."""

    def setUp(self):
        """Set up the board and test input_data for each test."""
        super().setUp()  # Inherit setup from TestValidator
        self.valid_input_data = None
        self.invalid_input_data = {'key': 'integer_value'}  # A non-None input

    def test_validate_none_input(self):
        """Test that NoneValidator does not return an error when input_data is None."""
        errors = NoneValidator.validate(self.board, self.valid_input_data)
        self.assertEqual(errors, [], "Expected no validation errors for None input_data.")

    def test_validate_non_none_input(self):
        """Test that NoneValidator returns an error when input_data is not None."""
        errors = NoneValidator.validate(self.board, self.invalid_input_data)
        self.assertIn("Expecting None", errors, "Expected error when input_data is not None.")


if __name__ == '__main__':
    unittest.main()
