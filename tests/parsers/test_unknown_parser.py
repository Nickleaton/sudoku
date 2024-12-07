"""TestUnknownParser."""
import unittest
from typing import List, Tuple, Any

from src.parsers.unknown_parser import UnknownParser
from tests.parsers.test_parser import TestParser


class TestUnknownParser(TestParser):
    """Test case for the UnknownParser class."""

    def setUp(self):
        """Set up the UnknownParser instance for testing."""
        self.parser: UnknownParser = UnknownParser()
        self.representation: str = 'UnknownParser()'
        self.example_format: str = ""
        self.valid_input_result: List[Tuple[str, Any]] = []
        self.valid_input_answer: List[Tuple[str, Any]] = []
        self.invalid_input: List[str] = \
            [
                "1, 2, a, 4",
                ""
            ]


if __name__ == "__main__":
    unittest.main()
