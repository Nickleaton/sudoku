"""TestNoneParser."""
import unittest
from typing import Any, list, tuple

from src.parsers.none_parser import NoneParser
from src.utils.sudoku_exception import SudokuError
from tests.parsers.test_parser import TestParser


class TestNoneParser(TestParser):
    """Test case for the NoneParser class."""

    def setUp(self):
        """Set up the NoneParser instance for testing."""
        super().setUp()
        self.parser: NoneParser = NoneParser()
        self.representation: str = 'NoneParser()'
        self.valid_inputs: list[tuple[str, Any]] = []
        self.empty_allowed = False
        self.invalid_inputs: list[str] = [
            "not empty",
            " ",
            "123",
            "None",
            "empty text",
        ]

    def test_parse_empty_input(self):
        """Tests parsing an empty input string doesn't apply for this parser."""
        if self.empty_allowed:
            with self.assertRaises(SudokuError):
                self.parser.parse("")


if __name__ == "__main__":
    unittest.main()
