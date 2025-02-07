import unittest

from src.validators.cell_validator import CellValidator
from tests.validators.test_validator import TestValidator


class TestCellValidator(TestValidator):
    """Test case for the CellValidator class."""

    def setUp(self):
        super().setUp()
        self.valid_data = (
            {'Row': 2, 'Column': 3},
            {'Row': 4, 'Column': 3},
        )
        self.invalid_data = (
            {'Column': 3},
            {'Row': 2},
            {'Row': 'a', 'Column': 3},
            {'Row': 2, 'Column': 'b'},
            {'Row': 100, 'Column': 200}
        )
        self.required_keys = ['Row', 'Column']
        self.representation = 'CellValidator()'
        self.validator = CellValidator()

    def test_validate_horizontal_connectivity(self):
        """Test validate_horizontal_connectivity method."""
        cases = (
            # Valid case: horizontally connected
            {
                'cell1': {'Row': 1, 'Column': 1},
                'cell2': {'Row': 1, 'Column': 2},
                'expected': []
            },
            # Invalid case: not in the same row
            {
                'cell1': {'Row': 1, 'Column': 1},
                'cell2': {'Row': 2, 'Column': 1},
                'expected': ["Cells {'Row': 1, 'Column': 1} and {'Row': 2, 'Column': 1} are not in the same row."]
            },
            # Invalid case: not horizontally adjacent
            {
                'cell1': {'Row': 1, 'Column': 1},
                'cell2': {'Row': 1, 'Column': 3},
                'expected': ["Cells {'Row': 1, 'Column': 1} and {'Row': 1, 'Column': 3} are not horizontally adjacent."]
            },
        )

        for case in cases:
            with self.subTest(cell1=case['cell1'], cell2=case['cell2']):
                errors = self.validator.validate_horizontal_connectivity(case['cell1'], case['cell2'])
                self.assertEqual(errors, case['expected'])


if __name__ == '__main__':
    unittest.main()
