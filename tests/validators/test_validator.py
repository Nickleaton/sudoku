import unittest

from src.board.board import Board
from src.validators.validator import Validator  # Assuming the Validator class is in src/validator.py


class TestValidator(unittest.TestCase):
    """Test case for the Validator class."""

    def setUp(self):
        """Set up the board and test data for each test."""
        self.board = Board(6, 6, 2, 3, {})
        self.valid_data = {
            'Good': {
                'key1': 'value1',
                'key2': 'value2'
            },
        }
        self.invalid_data = {
            'MissingKey': {
                'key1': 'value1'
            }
        }
        self.required_keys = ['key1', 'key2']
        self.representation = 'Validator()'

    def test_repr(self):
        """Test the string representation of the Validator class."""
        self.assertEqual('Validator()', repr(Validator()))

    def test_good(self):
        for name, input_data in self.valid_data.items():
            errors = Validator.validate(self.board, input_data)
            self.assertEqual(errors, [], f"Expected no validation errors for {name}.")

    def test_bad(self):
        for name, input_data in self.invalid_data.items():
            errors = Validator.validate(self.board, input_data)
            self.assertNotEqual(errors, [], f"Expected validation errors for {name}.")


if __name__ == '__main__':
    unittest.main()
