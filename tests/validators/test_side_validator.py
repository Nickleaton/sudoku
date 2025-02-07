import unittest

from src.validators.side_validator import SideValidator
from tests.validators.test_validator import TestValidator


class TestSideValidator(TestValidator):
    """Test case for the SideValidator class."""

    def setUp(self):
        """Set up the specific test line for SideValidator."""
        super().setUp()
        self.valid_data = [
            {'Side': 'T'},
            {'Side': 'B'},
            {'Side': 'L'},
            {'Side': 'R'},
        ]
        self.invalid_data = [
            {'xxx': 'T'},
            {'Side': 'X'},
            {'x': 'x', 'y': 'y'},
            {'Side': 9}
        ]
        self.validator = SideValidator()
        self.representation = 'SideValidator()'


if __name__ == '__main__':
    unittest.main()
