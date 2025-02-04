"""TestSizeParser."""
import unittest
from typing import Any

from src.parsers.size_parser import SizeParser
from tests.parsers.test_parser import TestParser


class TestSizeParser(TestParser):
    """Test case for the SizeParser class."""

    def setUp(self):
        """Set up the SizeParser instance for testing."""
        super().setUp()
        self.parser: SizeParser = SizeParser()
        self.representation: str = 'SizeParser()'
        self.empty_allowed = False
        self.valid_inputs: List[Tuple[str, Any]] = \
            [
                ("8x8", {'Size': {'rows': 8, 'cols': 8}}),
                ("4x4", {'Size': {'rows': 4, 'cols': 4}}),
                ("9x9", {'Size': {'rows': 9, 'cols': 9}}),
                ("16x16", {'Size': {'rows': 16, 'cols': 16}}),
            ]
        self.invalid_inputs: List[str] = \
            [
                "abc",
                "3xx3",
                "3x",
                "x3x",
                "3x-3",
                "999x999"
            ]


if __name__ == "__main__":
    unittest.main()
