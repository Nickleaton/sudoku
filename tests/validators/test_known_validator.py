"""TestKnownValidator."""
import unittest

from src.validators.known_validator import KnownValidator
from tests.validators.test_validator import TestValidator


class TestKnownValidator(TestValidator):
    """Test case for the KnownValidator class."""

    def setUp(self):
        """Set up the board and test line for each test."""
        super().setUp()
        self.valid_data = [
            {'Known': [
                '123456',  # Row 1
                '234561',  # Row 2
                '345612',  # Row 3
                '4..123',  # Row 4
                '.....4',  # Row 5
                '612345'  # Row 6
            ]
            },

        ]
        self.invalid_data = [
            {'Known': [
                '12345X',  # Row 1: Invalid character 'X'
                '234561',  # Row 2
                '345612',  # Row 3
                '456123',  # Row 4
                '561234',  # Row 5
                '612345'  # Row 6
            ]
            },
            {'Known': 1},
            {'Known': [
                '1234567',  # Row 1: Extra column
                '234561',  # Row 2
                '234561',  # Row 3
                '234561',  # Row 4
                '234561',  # Row 5
                '234561'  # Row 6
            ]
            },
            {'Known': [
                '12347',  # Row 1: Short column
                '234561',  # Row 2
                '234561',  # Row 3
                '234561',  # Row 4
                '234561',  # Row 5
                '234561'  # Row 6
            ]
            },
            {'Known': [
                '123456',  # Row 1
                '234561',  # Row 2
            ],
            },
            {'Bad': [
                '123456',
                '234561',
                '234561',
                '234561',
                '234561',
                '234561'
            ]
            }
        ]
        self.representation = 'KnownValidator()'
        self.validator = KnownValidator()


if __name__ == '__main__':
    unittest.main()
