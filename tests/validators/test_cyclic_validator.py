"""TestCyclicValidator."""
import unittest

from src.validators.cyclic_validator import CyclicValidator
from tests.validators.test_validator import TestValidator


class TestCyclicValidator(TestValidator):
    """Test case for the CyclicValidator class."""

    def setUp(self):
        """Set up the specific test line for CyclicValidator."""
        super().setUp()
        self.valid_data = [
            {'Cyclic': 'A'},
            {'Cyclic': 'C'},
        ]
        self.invalid_data = [
            {'xxx': 'T'},
            {'Cyclic': 'X'},
            {'x': 'x', 'y': 'y'},
            {'Cyclic': 1}
        ]
        self.validator = CyclicValidator()
        self.representation = 'CyclicValidator()'


if __name__ == '__main__':
    unittest.main()
