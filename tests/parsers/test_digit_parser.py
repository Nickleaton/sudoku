import unittest
from typing import List, Tuple, Any

from src.parsers.digit_parser import DigitParser
from tests.parsers.test_parser import TestParser


class TestDigitParser(TestParser):
    """Test case for the DigitParser class."""

    def setUp(self):
        """Sets up the DigitsParser instance for testing."""
        self.parser = DigitParser()
        self.valid_input: List[Tuple[str, Any]] = \
            [
                # Valid single digit inputs
                ("0", 0),
                ("1", 1),
                ("2", 2),
                ("3", 3),
                ("4", 4),
                ("5", 5),
                ("6", 6),
                ("7", 7),
                ("8", 8),
                ("9", 9),
                # Valid input with leading/trailing whitespace
                (" 5 ", 5),
                ("  0  ", 0),
            ]
        self.invalid_input: List[str] = \
            [
                # Invalid inputs that should raise ParserError
                "10",  # More than one digit
                "a",  # Non-digit character
                " ",  # Empty input
                "5a",  # Non-digit character after a valid digit
                "1, 2",  # Invalid due to multiple digits separated by a comma
                "12",  # Two digits combined
                "abc",  # Completely invalid input
                "  ",  # Whitespace only
                "12  ",  # Spaces after an invalid digit
            ]


if __name__ == "__main__":
    unittest.main()
