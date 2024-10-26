import unittest
from typing import List, Tuple, Any

from src.parsers.known_parser import KnownParser
from tests.parsers.test_parser import TestParser


class TestKnownParser(TestParser):
    """Test case for the KnownParser class."""

    def setUp(self):
        """Sets up the KnownParser instance for testing."""
        self.parser: KnownParser = KnownParser()
        self.representation: str = 'KnownParser()'
        self.valid_input: List[Tuple[str, Any]] = \
            [
                ("123456789", ['1', '2', '3', '4', '5', '6', '7', '8', '9']),
                (".........", ['.', '.', '.', '.', '.', '.', '.', '.', '.']),
                ("...o...e.", ['.', '.', '.', 'o', '.', '.', '.', 'e', '.']),
                (".f.......", ['.', 'f', '.', '.', '.', '.', '.', '.', '.']),
                ("hml......", ['h', 'm', 'l', '.', '.', '.', '.', '.', '.']),
            ]
        self.invalid_input: List[str] = \
            [
                "123x56789"
                "123,56789"
            ]


if __name__ == "__main__":
    unittest.main()