"""TestKnownParser."""
import unittest
from typing import Any, List, Tuple

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
        self.valid_inputs: List[Tuple[str, Any]] = \
            [
                ("123456789", {'Known': ['1', '2', '3', '4', '5', '6', '7', '8', '9']}),
                (".........", {'Known': ['.', '.', '.', '.', '.', '.', '.', '.', '.']}),
                ("...o...e.", {'Known': ['.', '.', '.', 'o', '.', '.', '.', 'e', '.']}),
                (".f.......", {'Known': ['.', 'f', '.', '.', '.', '.', '.', '.', '.']}),
                ("hml......", {'Known': ['h', 'm', 'l', '.', '.', '.', '.', '.', '.']}),
            ]
        self.invalid_inputs: List[str] = \
            [
                "123x56789"
                "123,56789"
            ]


if __name__ == "__main__":
    unittest.main()
