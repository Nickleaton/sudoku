import unittest

from src.validators.quadruples_validator import QuadrupleValidator
from tests.validators.test_validator import TestValidator


class TestQuadrupleValidator(TestValidator):
    """Test class for QuadrupleValidator."""

    def setUp(self):
        super().setUp()
        self.valid_data: dict = {"quadruples": [1, 2, 3, 4, '?']}
        self.invalid_data: dict = {"quadruples": [1, 2, 7, 'x']}

    def test_valid_data(self):
        """Test that validation passes with valid quadruples."""
        errors: list[str] = QuadrupleValidator.validate(self.board, self.valid_data)
        self.assertEqual(errors, [], "Validation failed for valid quadruples")

    def test_invalid_data(self):
        """Test that validation fails with invalid quadruples."""
        errors: list[str] = QuadrupleValidator.validate(self.board, self.invalid_data)
        self.assertTrue(any("not a valid digit" in error for error in errors))


if __name__ == '__main__':
    unittest.main()
