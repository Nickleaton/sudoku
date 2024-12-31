from src.validators.value_validator import ValueValidator  # Assuming the validator is in this module
from tests.validators.test_validator import TestValidator


class TestValueValidator(TestValidator):
    """Test case for the ValueValidator class."""

    def setUp(self):
        """Set up the specific test data for ValueValidator."""
        super().setUp()  # Call the base class setup

        # Example board (this can be mocked if necessary)
        self.board = Board(digit_range={1, 2, 3, 4, 5, 6, 7, 8, 9})

        # Valid input data (where 'number' is an integer)
        self.valid_input_data = {
            'number': 5
        }

        # Invalid input data (where 'number' is a string, not an integer)
        self.invalid_input_data = {
            'number': 'five'
        }

        # Missing 'number' key
        self.missing_number_data = {}

    def test_validate_valid(self):
        """Test that validate returns no errors for valid 'number'."""
        self.validate_input(ValueValidator, self.valid_input_data, [])

    def test_validate_invalid(self):
        """Test that validate returns an error for invalid 'number'."""
        expected_errors = ['Value must be an integer']
        self.validate_input(ValueValidator, self.invalid_input_data, expected_errors)

    def test_validate_missing_number(self):
        """Test that validate returns an error when 'number' is missing."""
        expected_errors = ['Value must be an integer']
        self.validate_input(ValueValidator, self.missing_number_data, expected_errors)


if __name__ == '__main__':
    unittest.main()
