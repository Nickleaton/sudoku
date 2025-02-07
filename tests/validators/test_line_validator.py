import unittest

from src.validators.line_validator import LineValidator  # Assuming LineValidator is in src/validators/line_validator.py
from tests.validators.test_validator import TestValidator


class TestLineValidator(TestValidator):
    """Test case for the LineValidator class."""

    def setUp(self):
        """Set up the specific test line for LineValidator."""
        super().setUp()  # Call the base class setup

        self.valid_data = [
            [
                {'Row': 1, 'Column': 1},  # Cell 1
                {'Row': 2, 'Column': 1},  # Cell 2, valid king's move (vertical)
                {'Row': 2, 'Column': 2},  # Cell 3, valid king's move (diagonal)
                {'Row': 3, 'Column': 2},  # Cell 4, valid king's move (vertical)
                {'Row': 3, 'Column': 3},  # Cell 5, valid king's move (diagonal)
            ],
            [
                {'Row': 1, 'Column': 1},  # Cell 1
                {'Row': 2, 'Column': 1},  # Cell 2, valid king's move (vertical)
                {'Row': 2, 'Column': 2},  # Cell 3, valid king's move (diagonal)
                {'Row': 3, 'Column': 2},  # Cell 4, valid king's move (vertical)
                {'Row': 4, 'Column': 2},
            ],
        ]
        self.invalid_data = [
            [
                {'Row': 0, 'Column': 1},  # Row 0, out of range
                {'Row': 2, 'Column': 2},
                {'Row': 7, 'Column': 3},  # Row 7, out of range
            ],
            [
                {'Row': 1, 'Column': 1},
                {'Row': 2, 'Column': 1},
                {'Row': 2, 'Column': 1},  # Duplicate cell
                {'Row': 3, 'Column': 2},
            ],
            [
                {'Row': 1, 'Column': 1},
                {'Row': 3, 'Column': 3},  # Not a king's move
            ]
        ]
        self.representation = 'LineValidator()'
        self.validator = LineValidator()


if __name__ == '__main__':
    unittest.main()
