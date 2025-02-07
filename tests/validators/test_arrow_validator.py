import unittest

from src.validators.arrow_validator import ArrowValidator
from tests.validators.test_validator import TestValidator


class TestArrowValidator(TestValidator):
    """Test case for the LineValidator class."""

    def setUp(self):
        """Set up the specific test line for LineValidator."""
        super().setUp()  # Call the base class setup

        self.valid_datax = [
            {
                'Arrow':
                    {
                        'Pill':
                            [
                                {'Row': 1, 'Column': 1}
                            ],
                        'Shaft':
                            [
                                {'Row': 1, 'Column': 2},
                                {'Row': 1, 'Column': 3}
                            ]
                    }
            }
        ]
        self.invalid_data = [
            {
                'Arrow':
                    {
                        'Pill': [],
                        'Shaft': []
                    }
            },
        ]
        self.representation = 'ArrowValidator()'
        self.validator = ArrowValidator()


if __name__ == '__main__':
    unittest.main()
