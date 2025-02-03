"""TestSizeParser."""
import unittest
from typing import Any

from src.parsers.size_parser import SizeParser
from tests.parsers.test_parser import TestParser


class TestSizeParser(TestParser):
    """Test case for the SizeParser class."""

    def setUp(self):
        """Set up the SizeParser instance for testing."""
        self.parser: SizeParser = SizeParser()
        self.representation: str = 'SizeParser()'
        self.valid_inputs: List[Tuple[str, Any]] = \
            [
                ("8x8", {'rows': '8', 'columns': '8'}),
                ("4x4", {'rows': '4', 'columns': '4'}),
                ("9x9", {'rows': '9', 'columns': '9'}),
                ("16x16", {'rows': '16', 'columns': '16'}),
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
