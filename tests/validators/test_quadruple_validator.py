from src.validators.quadruple_validator import QuadrupleValidator

from tests.validators.test_validator import TestValidator


class TestQuadrupleValidator(TestValidator):
    """Test case for the QuadrupleValidator class."""

    def setUp(self):
        """Set up the specific test data for QuadrupleValidator."""
        super().setUp()  # Call the base class setup

        # Example board with digit range
        self.board = Board(digit_range={1, 2, 3, 4, 5, 6, 7, 8, 9})

        # Valid quadruple input (using valid digits and '?')
        self.valid_input_data = {
            'quadruples': [1, 2, 3, 4, '?', 5]
        }

        # Invalid quadruple input (containing invalid digits outside the digit range)
        self.invalid_input_data = {
            'quadruples': [1, 2, 3, 10, '?', 5]
        }

        # Empty quadruples list
        self.empty_input_data = {
            'quadruples': []
        }

    def test_validate_valid(self):
        """Test that validate returns no errors for valid quadruples."""
        self.validate_input(QuadrupleValidator, self.valid_input_data, [])

    def test_validate_invalid(self):
        """Test that validate returns an error for invalid digits in quadruples."""
        expected_errors = ['Quadruple 10 is not start valid digit']
        self.validate_input(QuadrupleValidator, self.invalid_input_data, expected_errors)

    def test_validate_empty_input_data(self):
        """Test that validate returns no errors for an empty quadruples list."""
        self.validate_input(QuadrupleValidator, self.empty_input_data, [])


if __name__ == '__main__':
    unittest.main()