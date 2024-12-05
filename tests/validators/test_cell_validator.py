import unittest

from src.validators.cell_validator import CellValidator
from tests.validators.test_validator import TestValidator


class TestCellValidator(TestValidator):
    """Unit tests for CellValidator methods."""

    def setUp(self):
        super().setUp()

    def test_has_valid_keys_valid(self):
        """Test that has_valid_keys correctly identifies valid cells."""
        valid_cell = {'row': 2, 'column': 3}
        errors = CellValidator.has_valid_keys(valid_cell)
        self.assertEqual(errors, [])

    def test_has_valid_keys_missing_keys(self):
        """Test that has_valid_keys identifies missing keys."""
        invalid_cell = {'row': 2}
        errors = CellValidator.has_valid_keys(invalid_cell)
        self.assertEqual(errors, ["Cell is missing 'row' or 'column' keys."])

    def test_has_valid_keys_non_integer_values(self):
        """Test that has_valid_keys identifies non-integer values."""
        invalid_cell = {'row': '2', 'column': 3}
        errors = CellValidator.has_valid_keys(invalid_cell)
        self.assertEqual(errors, ["Cell must have integer 'row' and 'column' values."])

    def test_validate_range_valid(self):
        """Test that validate_range identifies valid cells within the board."""
        valid_cell = {'row': 3, 'column': 4}
        errors = CellValidator.validate_range(self.board, valid_cell)
        self.assertEqual(errors, [])

    def test_validate_range_invalid(self):
        """Test that validate_range identifies cells outside the board range."""
        invalid_cell = {'row': 7, 'column': 3}
        errors = CellValidator.validate_range(self.board, invalid_cell)
        self.assertEqual(errors, ["Invalid cell: (7, 3)"])

    def test_validate_connected_valid(self):
        """Test that validate_connected identifies connected cells."""
        cell1 = {'row': 2, 'column': 3}
        cell2 = {'row': 2, 'column': 4}
        errors = CellValidator.validate_connected(cell1, cell2)
        self.assertEqual(errors, [])

    def test_validate_connected_not_connected(self):
        """Test that validate_connected identifies unconnected cells."""
        cell1 = {'row': 2, 'column': 3}
        cell2 = {'row': 4, 'column': 5}
        errors = CellValidator.validate_connected(cell1, cell2)
        self.assertEqual(errors, ["Cells at (2, 3) and (4, 5) are not connected by a king's move."])

    def test_validate_horizontal_connectivity_valid(self):
        """Test that validate_horizontal_connectivity identifies horizontally connected cells."""
        cell1 = {'row': 2, 'column': 3}
        cell2 = {'row': 2, 'column': 4}
        errors = CellValidator.validate_horizontal_connectivity(cell1, cell2)
        self.assertEqual(errors, [])

    def test_validate_horizontal_connectivity_not_connected(self):
        """Test that validate_horizontal_connectivity identifies cells that are not horizontally connected."""
        cell1 = {'row': 2, 'column': 3}
        cell2 = {'row': 2, 'column': 5}
        errors = CellValidator.validate_horizontal_connectivity(cell1, cell2)
        self.assertEqual(errors, ["Cells at (2, 3) and (2, 5) are not horizontally adjacent."])

    def test_validate_horizontal_connectivity_not_same_row(self):
        """Test that validate_horizontal_connectivity identifies cells not in the same row."""
        cell1 = {'row': 2, 'column': 3}
        cell2 = {'row': 3, 'column': 3}
        errors = CellValidator.validate_horizontal_connectivity(cell1, cell2)
        self.assertEqual(errors, ["Cells at (2, 3) and (3, 3) are not in the same row."])

    def test_validate_all_validations(self):
        """Test that validate method runs all individual validations correctly."""
        valid_cell = {'row': 3, 'column': 4}
        errors = CellValidator.validate(self.board, valid_cell)
        self.assertEqual(errors, [])

    def test_validate_all_invalidations(self):
        """Test that validate method identifies all errors when the cell is invalid."""
        invalid_cell = {'row': 7, 'column': 8}
        errors = CellValidator.validate(self.board, invalid_cell)
        self.assertTrue(any("Invalid cell" in error for error in errors))


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
