import unittest

from src.validators.line_validator import LineValidator
from tests.validators.test_validator import TestValidator


class TestLineValidator(TestValidator):

    def setUp(self):
        super().setUp()
        """Set up common test data for the LineValidator."""
        # Set up some valid cells for testing
        self.valid_cells = [
            {'row': 1, 'column': 1},
            {'row': 2, 'column': 1},
            {'row': 3, 'column': 1}
        ]
        # Set up some invalid cells for testing
        self.invalid_cells_empty = []
        self.invalid_cells_duplicate = [
            {'row': 1, 'column': 1},
            {'row': 1, 'column': 1}
        ]
        self.invalid_cells_out_of_range = [
            {'row': -1, 'column': 1},  # Invalid row
            {'row': 3, 'column': 100}  # Invalid column
        ]
        self.invalid_cells_non_connected = [
            {'row': 1, 'column': 1},
            {'row': 3, 'column': 1},  # Not a king's move away
        ]

    def test_validate_valid_cells(self):
        """Test LineValidator with valid cells."""
        errors = LineValidator.validate(self.board, self.valid_cells)
        self.assertEqual(errors, [], "Validation failed for valid cells")

    def test_validate_empty_cells(self):
        """Test LineValidator with empty data."""
        errors = LineValidator.validate(self.board, self.invalid_cells_empty)
        self.assertIn("The data cannot be empty.", errors)

    def test_validate_duplicate_cells(self):
        """Test LineValidator with duplicate cells."""
        errors = LineValidator.validate(self.board, self.invalid_cells_duplicate)
        self.assertIn("Duplicate cell found: (1, 1)", errors)

    def test_validate_out_of_range_cells(self):
        """Test LineValidator with out-of-range cells."""
        errors = LineValidator.validate(self.board, self.invalid_cells_out_of_range)
        self.assertTrue(any("Invalid cell" in error for error in errors))

    def test_validate_non_connected_cells(self):
        """Test LineValidator with non-connected cells (not a king's move)."""
        errors = LineValidator.validate(self.board, self.invalid_cells_non_connected)
        self.assertTrue(any("king's move" in error for error in errors))

if __name__ == '__main__':  # pragma: no cover
    unittest.main()
