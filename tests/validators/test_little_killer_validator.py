from src.validators.little_killer_validator import LittleKillerValidator  # Assuming the validator is in this module
from tests.validators.test_validator import TestValidator


class TestLittleKillerValidator(TestValidator):
    """Test case for the LittleKillerValidator class."""

    def setUp(self):
        """Set up the specific test line for LittleKillerValidator."""
        super().setUp()  # Call the base class setup

        # Valid input for LittleKiller constraint
        self.valid_data = [
            {
                'Side': 'T',
                'Index': 2,
                'Cyclic': 'C',
                'Value': 15,
            },
            {
                'Side': 'R',
                'Index': 2,
                'Cyclic': 'C',
                'Value': 15,
            },
            {
                'Side': 'L',
                'Index': 2,
                'Cyclic': 'C',
                'Value': 15,
            },
            {
                'Side': 'B',
                'Index': 2,
                'Cyclic': 'C',
                'Value': 15,
            },
            {
                'Side': 'T',
                'Index': 3,
                'Cyclic': 'A',
                'Value': 15,
            },
        ]

        # Invalid input line for missing required keys
        self.invalid_data = [
            {
                'Index': 1,
                'Cyclic': 'C',
                'Value': 1
            },
            {
                'Side': 'T',
                'Cyclic': 'C',
                'Value': 2
            },
            {
                'Side': 'T',
                'Index': 3,
                'Value': 3
            },
            {
                'Side': 'T',
                'Index': 4,
                'Cyclic': 'C',
            },
            {
                'Side': 'X',
                'Index': 6,
                'Cyclic': 'C',
                'Value': 5
            },
            {
                'Side': 'T',
                'Index': 2,
                'Cyclic': 'X',
                'Value': 6
            },
            {
                'Side': 'T',
                'Index': 12,
                'Cyclic': 'C',
                'Value': 7
            },
            {
                'Side': 'T',
                'Index': 'X',
                'Cyclic': 'C',
                'Value': 8
            },
            {
                'Side': 'T',
                'Index': 1,
                'Cyclic': 'C',
                'Value': 'X'
            },
            {
                'Side': 'T',
                'Index': 9,
                'Cyclic': 'C',
                'Value': 15,
            },
            {
                'Side': 'L',
                'Index': 9,
                'Cyclic': 'C',
                'Value': 15,
            },
        ]
        self.representation = 'LittleKillerValidator()'
        self.validator = LittleKillerValidator()
