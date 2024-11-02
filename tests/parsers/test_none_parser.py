import unittest
from typing import List, Tuple, Any

from src.parsers.none_parser import NoneParser
from tests.parsers.test_parser import TestParser


class TestNoneParser(TestParser):
    """Test case for the NoneParser class."""

    def setUp(self):
        """Sets up the NoneParser instance for testing."""
        self.parser: NoneParser = NoneParser()
        self.representation: str = 'NoneParser()'
        self.example_format: str = ''
        self.valid_input_result: List[Tuple[str, Any]] = [
            ("", None),
        ]
        self.valid_input_answer: List[Tuple[str, Any]] = [
            ("", None),
        ]
        self.invalid_input: List[str] = [
            "not empty",
            " ",
            "123",
            "None",
            "empty text",
        ]

    def test_parse_empty_input(self):
        """Tests parsing an empty input string doesn't apply for this parser """
        pass

if __name__ == "__main__":
    unittest.main()
