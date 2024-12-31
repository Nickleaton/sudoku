from src.validators.little_killer_validator import LittleKillerValidator  # Assuming the validator is in this module
from tests.validators.test_validator import TestValidator


class TestLittleKillerValidator(TestValidator):
    """Test case for the LittleKillerValidator class."""

    def setUp(self):
        """Set up the specific test data for LittleKillerValidator."""
        super().setUp()  # Call the base class setup

        # Valid input for LittleKiller constraint
        self.valid_input_data = {
            'side': 'T',
            'index': 2,
            'direction': 'C',
            'number': 15
        }

        # Invalid input data for missing required keys
        self.invalid_keys_input_data = {
            'side': 'T',
            'index': 2
            # Missing 'direction' and 'number'
        }

        # Invalid index (out of range)
        self.invalid_index_input_data = {
            'side': 'T',
            'index': 100,  # Out of range index
            'direction': 'C',
            'number': 15
        }

        # Valid data but invalid number for the ValueValidator (assuming it checks numbers)
        self.invalid_value_input_data = {
            'side': 'T',
            'index': 2,
            'direction': 'C',
            'number': 999  # Assuming this is invalid according to ValueValidator
        }

        # Empty input_data (edge case)
        self.empty_input_data = {}

    def test_validate_valid(self):
        """Test that validate returns no errors for valid input_data."""
        self.validate_input(LittleKillerValidator, self.valid_input_data, [])

    def test_validate_invalid_keys(self):
        """Test that validate returns errors for missing required keys."""
        expected_errors = [
            "Missing required key: direction",
            "Missing required key: number"
        ]
        self.validate_input(LittleKillerValidator, self.invalid_keys_input_data, expected_errors)

    def test_validate_invalid_index(self):
        """Test that validate returns an error for out-of-range index."""
        expected_errors = ["Invalid index: 100"]
        self.validate_input(LittleKillerValidator, self.invalid_index_input_data, expected_errors)

    def test_validate_invalid_value(self):
        """Test that validate returns an error for invalid value according to ValueValidator."""
        expected_errors = [
            "Invalid value: 999"  # Assuming this message comes from the ValueValidator
        ]
        self.validate_input(LittleKillerValidator, self.invalid_value_input_data, expected_errors)

    def test_validate_empty_input_data(self):
        """Test that validate returns an error for empty input_data."""
        expected_errors = ['The input_data cannot be empty.']
        self.validate_input(LittleKillerValidator, self.empty_input_data, expected_errors)
