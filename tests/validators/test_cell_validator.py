import unittest

from src.validators.cell_validator import CellValidator
from tests.validators.test_validator import TestValidator


class TestCellValidator(TestValidator):
    """Test case for the CellValidator class."""

    def setUp(self):
        super().setUp()
        self.valid_data = [
            {'Row': 2, 'Column': 3}
        ]
        self.invalid_data = [
            {'Column': 3},
            {'Row': 2},
            {'Row': 'a', 'Column': 3},
            {'Row': 2, 'Column': 'b'},
            {'Row': 100, 'Column': 200}
        ]
        self.required_keys = ['Row', 'Column']
        self.representation = 'CellValidator()'
        self.validator = CellValidator()


if __name__ == '__main__':
    unittest.main()
