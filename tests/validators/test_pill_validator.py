from src.validators.pill_validator import PillValidator
from tests.validators.test_validator import TestValidator


class TestPillValidator(TestValidator):
    """Test case for the PillValidator class."""

    def setUp(self):
        """Set up the specific test data for PillValidator."""
        super().setUp()  # Call the base class setup

        # Valid input for Pill constraint (same row, unique, connected horizontally)
        self.valid_input_data = [
            {'row': 1, 'column': 2},
            {'row': 1, 'column': 3},
            {'row': 1, 'column': 4}
        ]

        # Invalid input data for cells in different rows (same row condition fails)
        self.invalid_row_input_data = [
            {'row': 1, 'column': 2},
            {'row': 2, 'column': 3},
            {'row': 1, 'column': 4}
        ]

        # Invalid input data for duplicate cells
        self.invalid_duplicate_input_data = [
            {'row': 1, 'column': 2},
            {'row': 1, 'column': 2},
            {'row': 1, 'column': 4}
        ]

        # Invalid input data for non-horizontal (not connected) cells
        self.invalid_horizontal_input_data = [
            {'row': 1, 'column': 2},
            {'row': 1, 'column': 4},
            {'row': 1, 'column': 6}  # Cells are not adjacent
        ]

        # Empty input_data (edge case)
        self.empty_input_data = []

    def test_validate_valid(self):
        """Test that validate returns no errors for valid input_data."""
        self.validate_input(PillValidator, self.valid_input_data, [])

    def test_validate_invalid_row(self):
        """Test that validate returns an error if cells are not in the same row."""
        expected_errors = ["All cells must be in the same row."]
        self.validate_input(PillValidator, self.invalid_row_input_data, expected_errors)

    def test_validate_invalid_duplicate(self):
        """Test that validate returns an error if cells are duplicated."""
        expected_errors = ["Duplicate cell found: (1, 2)"]
        self.validate_input(PillValidator, self.invalid_duplicate_input_data, expected_errors)

    def test_validate_invalid_horizontal(self):
        """Test that validate returns an error if cells are not horizontally connected."""
        expected_errors = [
            "Cells (1, 2) and (1, 4) are not horizontally connected.",
            "Cells (1, 4) and (1, 6) are not horizontally connected."
        ]
        self.validate_input(PillValidator, self.invalid_horizontal_input_data, expected_errors)

    def test_validate_empty_input_data(self):
        """Test that validate returns an error for empty input_data."""
        expected_errors = ['The input_data cannot be empty.']
        self.validate_input(PillValidator, self.empty_input_data, expected_errors)


if __name__ == '__main__':
    unittest.main()
