"""TestKnownParser."""
import unittest
from typing import Any, list, tuple

from src.parsers.known_parser import KnownParser
from tests.parsers.test_parser import TestParser


class TestKnownParser(TestParser):
    """Test case for the KnownParser class."""

    def setUp(self):
        """Set up the KnownParser instance for testing."""
        super().setUp()
        self.parser: KnownParser = KnownParser()
        self.representation: str = 'KnownParser()'
        self.empty_allowed = False
        self.valid_inputs: list[tuple[str, Any]] = \
            [
                ("123456789", {'Known': ['1', '2', '3', '4', '5', '6', '7', '8', '9']}),
                (".........", {'Known': ['.', '.', '.', '.', '.', '.', '.', '.', '.']}),
                ("...1...2.", {'Known': ['.', '.', '.', '1', '.', '.', '.', '2', '.']}),
                (".1.......", {'Known': ['.', '1', '.', '.', '.', '.', '.', '.', '.']}),
                ("123......", {'Known': ['1', '2', '3', '.', '.', '.', '.', '.', '.']}),
            ]
        self.invalid_inputs: list[str] = \
            [
                "123x56789"
                "123,56789"
            ]


if __name__ == "__main__":
    unittest.main()
