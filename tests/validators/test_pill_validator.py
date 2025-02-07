import unittest

from src.validators.pill_validator import PillValidator
from tests.validators.test_validator import TestValidator


class TestPillValidator(TestValidator):
    """Test case for the PillValidator class."""

    def setUp(self):
        """Set up the specific test line for PillValidator."""
        super().setUp()  # Call the base class setup

        # Valid input for Pill constraint (same Row, unique, connected horizontally)
        self.valid_data = [
            [
                {'Row': 1, 'Column': 2},
                {'Row': 1, 'Column': 3},
                {'Row': 1, 'Column': 4}
            ],
            [
                {'Row': 2, 'Column': 4},
                {'Row': 3, 'Column': 4},
                {'Row': 4, 'Column': 4}

            ],
        ]

        # Invalid input line for cells in different rows (same Row condition fails)
        self.invalid_data = \
            [
                [
                    {'Row': 1, 'Column': 2},
                    {'Row': 2, 'Column': 3},
                    {'Row': 1, 'Column': 4}
                ],
                [
                    {'Row': 1, 'Column': 2},
                    {'Row': 1, 'Column': 2},
                    {'Row': 1, 'Column': 4}
                ],
                [
                    {'Row': 1, 'Column': 2},
                    {'Row': 1, 'Column': 4},
                    {'Row': 1, 'Column': 6}  # Cells are not adjacent
                ]
            ]
        self.representation = 'PillValidator()'
        self.validator = PillValidator()


if __name__ == '__main__':
    unittest.main()
