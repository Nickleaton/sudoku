"""TestBoxParser."""
import unittest
from typing import Any

from src.parsers.box_parser import BoxParser
from tests.parsers.test_parser import TestParser


class TestBoxParser(TestParser):
    """Test case for the BoxParser class."""

    def setUp(self):
        """Set up the BoxParser instance for testing."""
        self.parser: BoxParser = BoxParser()
        self.representation: str = 'BoxParser()'
        self.example_format: str = 'dxd'
        self.valid_input_result: list[tuple[str, Any]] = \
            [
                (
                    "3x3",
                    [3, 3]
                ),
                (
                    "2x3",
                    [2, 3]
                ),
                (
                    "4x4",
                    [4, 4]
                ),
                (
                    "2x2",
                    [2, 2]
                ),
            ]
        self.valid_input_answer: List[Tuple[str, Any]] = \
            [
                (
                    "3x3",
                    {'rows': '3', 'columns': '3'}
                ),
                (
                    "2x3",
                    {'rows': '2', 'columns': '3'}
                ),
                (
                    "4x4",
                    {'rows': '4', 'columns': '4'}
                ),
                (
                    "2x2",
                    {'rows': '2', 'columns': '2'}
                ),
            ]
        self.invalid_input: List[str] = \
            [
                "abc",
                "3xx3",
                "3x",
                "x3x",
                "3x-3",
            ]


if __name__ == "__main__":
    unittest.main()
