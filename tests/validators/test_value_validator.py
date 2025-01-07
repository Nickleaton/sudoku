from src.validators.value_validator import ValueValidator  # Assuming the validator is in this module
from tests.validators.test_validator import TestValidator


class TestValueValidator(TestValidator):
    """Test case for the ValueValidator class."""

    def setUp(self):
        """Set up the specific test line for ValueValidator."""
        super().setUp()  # Call the base class setup
        # Valid input line (where 'number' is an integer)
        self.valid_data = [
            {'Value': 5}
        ]
        self.invalid_data = [
            {'Value': 'five'},  # Not an integer
            {'xxx': 5},  # Missing 'Value' key
            {'Value': -5},  # Negative integer
            {'Value': 5, 'Extra': 10},  # Too many items
        ]
        self.representation = 'ValueValidator()'
        self.validator = ValueValidator()


if __name__ == '__main__':
    unittest.main()
