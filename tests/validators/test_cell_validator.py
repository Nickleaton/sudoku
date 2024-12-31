import unittest

from src.validators.cell_validator import CellValidator  # Assuming CellValidator is in src/validators/cell_validator.py
from tests.validators.test_validator import TestValidator


class TestCellValidator(TestValidator):
    """Test case for the CellValidator class."""

    def setUp(self):
        super().setUp()
        # Test data
        self.valid_cell = {'row': 2, 'column': 3}
        self.invalid_cell_missing_row = {'column': 3}
        self.invalid_cell_missing_col = {'row': 2}
        self.invalid_cell_non_integer_row = {'row': 'a', 'column': 3}
        self.invalid_cell_non_integer_col = {'row': 2, 'column': 'b'}
        self.invalid_cell_out_of_range = {'row': 100, 'column': 200}  # Adjust according to board size
        self.cell1 = {'row': 1, 'column': 1}
        self.cell2 = {'row': 1, 'column': 2}
        self.cell3 = {'row': 2, 'column': 3}

    def test_has_valid_keys_valid(self):
        """Test that has_valid_keys works for valid cell."""
        errors = CellValidator.has_valid_keys(self.valid_cell)
        self.assertEqual(errors, [])

    def test_has_valid_keys_missing_row(self):
        """Test that has_valid_keys identifies missing row."""
        errors = CellValidator.has_valid_keys(self.invalid_cell_missing_row)
        self.assertIn("Cell is missing 'row'.", errors)

    def test_has_valid_keys_missing_column(self):
        """Test that has_valid_keys identifies missing column."""
        errors = CellValidator.has_valid_keys(self.invalid_cell_missing_col)
        self.assertIn("Cell is missing 'column'.", errors)

    def test_has_valid_keys_non_integer_row(self):
        """Test that has_valid_keys identifies non-integer row."""
        errors = CellValidator.has_valid_keys(self.invalid_cell_non_integer_row)
        self.assertIn("Cell must have integer 'row'.", errors)

    def test_has_valid_keys_non_integer_column(self):
        """Test that has_valid_keys identifies non-integer column."""
        errors = CellValidator.has_valid_keys(self.invalid_cell_non_integer_col)
        self.assertIn("Cell must have integer 'column'.", errors)

    def test_validate_range_valid(self):
        """Test that validate_range works for valid cell."""
        errors = CellValidator.validate_range(self.board, self.valid_cell)
        self.assertEqual(errors, [])

    def test_validate_range_invalid(self):
        """Test that validate_range identifies an invalid cell."""
        self.board.is_valid.return_value = False  # Mock is_valid to return False
        errors = CellValidator.validate_range(self.board, self.invalid_cell_out_of_range)
        self.assertIn('Invalid cell: (100, 200)', errors)

    def test_validate_kings_move_valid(self):
        """Test that validate_kings_move works for connected cells."""
        errors = CellValidator.validate_kings_move(self.cell1, self.cell2)
        self.assertEqual(errors, [])

    def test_validate_kings_move_invalid(self):
        """Test that validate_kings_move identifies non-connected cells."""
        self.cell2 = {'row': 3, 'column': 3}  # Not adjacent to cell1
        errors = CellValidator.validate_kings_move(self.cell1, self.cell2)
        self.assertIn(
            "Cells at {'row': 1, 'column': 1} and {'row': 3, 'column': 3} are not connected by start king's move.",
            errors)

    def test_validate_connected_valid(self):
        """Test that validate_connected works for connected cells."""
        errors = CellValidator.validate_connected(self.cell1, self.cell2)
        self.assertEqual(errors, [])

    def test_validate_connected_invalid(self):
        """Test that validate_connected identifies non-connected cells."""
        self.cell2 = {'row': 3, 'column': 3}  # Not adjacent to cell1
        errors = CellValidator.validate_connected(self.cell1, self.cell2)
        self.assertIn(
            "Cells at {'row': 1, 'column': 1} and {'row': 3, 'column': 3} are not connected by start king's move.",
            errors)

    def test_validate_horizontal_connectivity_valid(self):
        """Test that validate_horizontal_connectivity works for horizontally connected cells."""
        errors = CellValidator.validate_horizontal_connectivity(self.cell1, self.cell2)
        self.assertEqual(errors, [])

    def test_validate_horizontal_connectivity_invalid(self):
        """Test that validate_horizontal_connectivity identifies non-horizontally connected cells."""
        self.cell2 = {'row': 1, 'column': 3}  # Not adjacent horizontally
        errors = CellValidator.validate_horizontal_connectivity(self.cell1, self.cell2)
        self.assertIn("Cells {'row': 1, 'column': 1} and {'row': 1, 'column': 3} are not horizontally adjacent.",
                      errors)

    def test_validate_valid_cell(self):
        """Test that the main validate method works for valid cell."""
        errors = CellValidator.validate(self.board, self.valid_cell)
        self.assertEqual(errors, [])

    def test_validate_invalid_cell(self):
        """Test that the main validate method identifies an invalid cell."""
        errors = CellValidator.validate(self.board, self.invalid_cell_missing_row)
        self.assertIn("Cell is missing 'row'.", errors)


if __name__ == '__main__':
    unittest.main()
