"""TestDigitParser."""
import unittest
from typing import List, Tuple, Dict

from src.parsers.digit_parser import DigitParser
from tests.parsers.test_parser import TestParser


class TestDigitParser(TestParser):
    """Test case for the DigitParser class."""

    def setUp(self):
        """Set up the DigitsParser instance for testing."""
        self.parser: DigitParser = DigitParser()
        self.representation: str = 'DigitParser()'
        self.example_format: str = 'd'
        self.valid_input_result: List[Tuple[str, int]] = \
            [
                # Valid single digit input_types
                ("0", [0]),
                ("1", [1]),
                ("2", [2]),
                ("3", [3]),
                ("4", [4]),
                ("5", [5]),
                ("6", [6]),
                ("7", [7]),
                ("8", [8]),
                ("9", [9]),
                # Valid input with leading/trailing whitespace
                (" 5 ", [5]),
                ("  0  ", [0]),
            ]
        self.valid_input_answer: List[Tuple[str, Dict[str, str]]] = \
            [
                # Valid single digit input_types
                ("0", {'digit': '0'}),
                ("1", {'digit': '1'}),
                ("2", {'digit': '2'}),
                ("3", {'digit': '3'}),
                ("4", {'digit': '4'}),
                ("5", {'digit': '5'}),
                ("6", {'digit': '6'}),
                ("7", {'digit': '7'}),
                ("8", {'digit': '8'}),
                ("9", {'digit': '9'}),
                # Valid input with leading/trailing whitespace
                (" 5 ", {'digit': '5'}),
                ("  0  ", {'digit': '0'})
            ]

        self.invalid_input: List[str] = \
            [
                # Invalid input_types that should raise ParserError
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

