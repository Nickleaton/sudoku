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
            {'Value': 'five'},
            {'xxx': 5}
        ]
        self.representation = 'ValueValidator()'
        self.validator = ValueValidator()


if __name__ == '__main__':
    unittest.main()
