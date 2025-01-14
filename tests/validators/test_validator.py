import unittest

from src.board.board import Board
from src.validators.validator import Validator  # Assuming the Validator class is in src/validator.py


class TestValidator(unittest.TestCase):
    """Test case for the Validator class."""

    def setUp(self):
        """Set up the board and test line for each test."""
        self.board = Board(6, 6, 2, 3, {})
        self.valid_data = []
        self.invalid_data = []
        self.required_keys = ['key1', 'key2']
        self.representation = 'Validator()'
        self.validator = Validator()

    def test_repr(self):
        """Test the string representation of the Validator class."""
        self.assertEqual(self.representation, repr(self.validator))

    def test_good(self):
        print()
        for input_data in self.valid_data:
            print(f'Good {input_data!r}')
            errors = self.validator.validate(self.board, input_data)
            self.assertEqual(errors, [], f"Expected no validation errors for {input_data!r}.")

    def test_bad(self):
        print()
        for input_data in self.invalid_data:
            errors = self.validator.validate(self.board, input_data)
            print(f'Bad   {input_data!r}')
            for error in errors:
                print(f'    {error}')
            self.assertNotEqual(errors, [], f"Expected validation errors for{input_data!r}.")


if __name__ == '__main__':
    unittest.main()
