import unittest

from src.validators.none_validator import NoneValidator
from tests.validators.test_validator import TestValidator


class TestNoneValidator(TestValidator):
    """Test case for the NoneValidator class."""

    def setUp(self):
        """Set up the board and test line for each test."""
        super().setUp()  # Inherit setup from TestValidator
        self.valid_data = [
            {'Columns': None}
        ]
        self.invalid_data = [
            {'Columns': 'xxx'}

        ]
        self.representation = 'NoneValidator()'
        self.validator = NoneValidator()


if __name__ == '__main__':
    unittest.main()
