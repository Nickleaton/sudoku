import unittest

from src.validators.pill_validator import PillValidator
from tests.validators.test_line_validator import TestLineValidator


class TestPillValidator(TestLineValidator):

    def setUp(self):
        """Set up common test data for PillValidator."""
        super().setUp()  # Inherit the setup from TestLineValidator

        # Set up valid cells that are on the same row and horizontally connected
        self.valid_pill_cells = [
            {'row': 1, 'column': 1},
            {'row': 1, 'column': 2}
        ]

        # Set up invalid cells that are not in the same row
        self.invalid_pill_cells_different_rows = [
            {'row': 1, 'column': 1},
            {'row': 2, 'column': 2},
            {'row': 3, 'column': 3}
        ]

        # Set up invalid cells that are not horizontally connected
        self.invalid_pill_cells_not_connected = [
            {'row': 1, 'column': 1},
            {'row': 1, 'column': 3}  # Skipping column 2
        ]

    def test_validate_valid_pill_cells(self):
        """Test PillValidator with valid pill cells (same row and horizontally connected)."""
        errors = PillValidator.validate(self.board, self.valid_pill_cells)
        self.assertEqual(errors, [], "Validation failed for valid pill cells")

    def test_validate_pill_cells_different_rows(self):
        """Test PillValidator with cells not on the same row."""
        errors = PillValidator.validate(self.board, self.invalid_pill_cells_different_rows)
        self.assertTrue(any("not in the same row" in error for error in errors))

    def test_validate_pill_cells_not_connected(self):
        """Test PillValidator with cells not horizontally connected."""
        errors = PillValidator.validate(self.board, self.invalid_pill_cells_not_connected)
        self.assertTrue(any("horizontally adjacent" in error for error in errors))


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
