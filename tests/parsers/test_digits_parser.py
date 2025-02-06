"""TestDigitsParser."""
import unittest
from typing import list, tuple

from src.parsers.digits_parser import DigitsParser
from tests.parsers.test_parser import TestParser


class TestDigitsParser(TestParser):
    """Test case for the DigitsParser class."""

    def setUp(self):
        """Set up the DigitsParser instance for testing."""
        super().setUp()
        self.parser: DigitsParser = DigitsParser()
        self.representation: str = 'DigitsParser()'
        self.example_format: str = '1,2,3,...'
        self.empty_allowed = False
        self.valid_inputs: list[tuple[str, dict[str: list[int]]]] = \
            [
                ('2', {'Digits': [2]}),
                ('1,2,3,4,8', {'Digits': [1, 2, 3, 4, 8]}),
            ]
        self.invalid_inputs: list[str] = \
            [
                '1, 2, start, 4',
                '1, 2, 3,',
                ', 1, 2, 3',
                '1, 2, 3, 4, 5, row',
                '10, 20, 30, 40, 50',
                'abc, def, ghi',
                ''
            ]


if __name__ == "__main__":
    unittest.main()
