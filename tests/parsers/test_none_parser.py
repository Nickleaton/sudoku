import unittest
from typing import List, Tuple, Any

from src.parsers.none_parser import NoneParser
from src.parsers.parser import ParserError
from tests.parsers.test_parser import TestParser


class TestNoneParser(TestParser):
    """Test case for the NoneParser class."""

    def setUp(self):
        """Sets up the NoneParser instance for testing."""
        self.parser: NoneParser = NoneParser()
        self.representation: str = 'NoneParser()'
        self.example_format: str = ''
        self.valid_input_result: List[Tuple[str, Any]] = []
        self.valid_input_answer: List[Tuple[str, Any]] = []
        self.invalid_input: List[str] = [
            "not empty",
            " ",
            "123",
            "None",
            "empty text",
        ]

    def test_parse_empty_input(self):
        """Tests parsing an empty input string doesn't apply for this parser"""
        """Tests that an empty input string is parsed successfully, while non-empty input raises ParserError."""
        # Test parsing with valid input (empty string)
        try:
            self.parser.parse("")
            self.fail("ParserError was not raised for empty input")
        except ParserError:
            pass


if __name__ == "__main__":
    unittest.main()
