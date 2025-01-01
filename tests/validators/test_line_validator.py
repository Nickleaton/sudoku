from src.validators.line_validator import LineValidator  # Assuming LineValidator is in src/validators/line_validator.py
from tests.validators.test_validator import TestValidator

class TestLineValidator(TestValidator):
    """Test case for the LineValidator class."""

    def setUp(self):
        """Set up the specific test input_data for LineValidator."""
        super().setUp()  # Call the base class setup

        # Specific test input_data for LineValidator
        self.valid_input_data = [
            {'row': 1, 'column': 1},  # Cell 1
            {'row': 2, 'column': 1},  # Cell 2, valid king's move (vertical)
            {'row': 2, 'column': 2},  # Cell 3, valid king's move (diagonal)
            {'row': 3, 'column': 2},  # Cell 4, valid king's move (vertical)
            {'row': 3, 'column': 3},  # Cell 5, valid king's move (diagonal)
        ]
        self.invalid_range_input_data = [
            {'row': 0, 'column': 1},  # Row 0, out of range
            {'row': 2, 'column': 2},
            {'row': 7, 'column': 3},  # Row 7, out of range
        ]
        self.duplicate_cells_input_data = [
            {'row': 1, 'column': 1},
            {'row': 2, 'column': 1},
            {'row': 2, 'column': 1},  # Duplicate cell
            {'row': 3, 'column': 2},
        ]
        self.invalid_connection_input_data = [
            {'row': 1, 'column': 1},
            {'row': 3, 'column': 3},  # Not a king's move
            {'row': 2, 'column': 2},
        ]
        self.empty_input_data = []

    def test_validate_valid(self):
        """Test that validate returns no errors for valid cell sequence."""
        self.validate_input(LineValidator, self.valid_input_data, [])

    def test_validate_invalid_range(self):
        """Test that validate returns errors for out-of-range cells."""
        expected_errors = [
            "Cell {'row': 0, 'column': 1} is out of range.",
            "Cell {'row': 7, 'column': 3} is out of range."
        ]
        self.validate_input(LineValidator, self.invalid_range_input_data, expected_errors)

    def test_validate_duplicate_cells(self):
        """Test that validate returns an error for duplicate cells."""
        expected_errors = ["Duplicate cell found: (2, 1)"]
        self.validate_input(LineValidator, self.duplicate_cells_input_data, expected_errors)

    def test_validate_invalid_connections(self):
        """Test that validate returns an error for invalid connections between cells."""
        expected_errors = [
            "Cells are not connected by a king's move: {'row': 1, 'column': 1} and {'row': 3, 'column': 3}"
        ]
        self.validate_input(LineValidator, self.invalid_connection_input_data, expected_errors)

    def test_validate_empty_input_data(self):
        """Test that validate returns an error for empty input input_data."""
        self.validate_input(LineValidator, self.empty_input_data, ['The input_data cannot be empty.'])


if __name__ == '__main__':
    unittest.main()
