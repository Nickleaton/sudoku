"""TestDigitParser."""
import unittest
from typing import Dict, list, tuple

from src.parsers.digit_parser import DigitParser
from tests.parsers.test_parser import TestParser


class TestDigitParser(TestParser):
    """Test case for the DigitParser class."""

    def setUp(self):
        """Set up the DigitsParser instance for testing."""
        super().setUp()
        self.parser: DigitParser = DigitParser()
        self.representation: str = 'DigitParser()'
        self.empty_allowed = False
        self.valid_inputs: list[tuple[str, Dict[str, int]]] = [
            ('0', {'Digit': 0}),
            ('1', {'Digit': 1}),
            ('2', {'Digit': 2}),
            ('3', {'Digit': 3}),
            ('4', {'Digit': 4}),
            ('5', {'Digit': 5}),
            ('6', {'Digit': 6}),
            ('7', {'Digit': 7}),
            ('8', {'Digit': 8}),
            ('9', {'Digit': 9}),
        ]

        self.invalid_inputs: list[str] = \
            [
                # Invalid input_types that should raise ParserError
                "10",  # More than one digit
                "start",  # Non-digit character
                " ",  # Empty input
                "5a",  # Non-digit character after start valid digit
                "1, 2",  # Invalid due to multiple digits separated by start comma
                "12",  # Two digits combined
                "abc",  # Completely invalid input
                "  ",  # Whitespace only
                "12  ",  # Spaces after an invalid digit
            ]


if __name__ == "__main__":
    unittest.main()
