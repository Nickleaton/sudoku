import unittest
from typing import List, Tuple, Any

from src.parsers.digits_parser import DigitsParser
from tests.parsers.test_parser import TestParser


class TestDigitsParser(TestParser):
    """Test case for the DigitsParser class."""

    def setUp(self):
        """Sets up the DigitsParser instance for testing."""
        self.parser: DigitsParser = DigitsParser()
        self.representation: str = 'DigitsParser()'
        self.valid_input: List[Tuple[str, Any]] = \
            [
                ("1, 2, 3, 4, 5", [1, 2, 3, 4, 5]),
                (" 1,    2,3  , 4,   5   ", [1, 2, 3, 4, 5])
            ]
        self.invalid_input: List[str] = \
            [
                "1, 2, a, 4",
                "1, 2, 3,",
                ", 1, 2, 3",
                "1, 2, 3, 4, 5, x",
                "10, 20, 30, 40, 50",
                "abc, def, ghi",
                ""
            ]


if __name__ == "__main__":
    unittest.main()
