import unittest

from src.validators.digits_validator import DigitsValidator
from tests.validators.test_validator import TestValidator


class TestValidatorModule(TestValidator):
    """Test case for the Validator class."""

    def setUp(self):
        """Set up the board and test line for each test."""
        super().setUp()  # Call the setup of the base TestValidator class
        self.valid_data = [
            {'digits': [1, 2, 3]}
        ]
        self.invalid_data = [
            {'digits': [1, 2, 10]},
            {'digits': [1, 1]},
            {'invalid': 'key'},
            {'digits': [1, 'x']}

        ]
        self.representation = 'DigitsValidator()'
        self.validator = DigitsValidator()


if __name__ == '__main__':
    unittest.main()
