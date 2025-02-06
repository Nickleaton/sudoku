"""TestBoxParser."""
import unittest
from typing import Any

from src.parsers.box_parser import BoxParser
from tests.parsers.test_parser import TestParser


class TestBoxParser(TestParser):
    """Test case for the BoxParser class."""

    def setUp(self):
        """Set up the BoxParser instance for testing."""
        super().setUp()
        self.parser: BoxParser = BoxParser()
        self.representation: str = 'BoxParser()'
        self.empty_allowed: bool = False

        self.valid_inputs: list[tuple[str, Any]] = \
            [
                ("3x3", {'Box': {'rows': 3, 'cols': 3}}),
                ("2x3", {'Box': {'rows': 2, 'cols': 3}}),
                ("4x4", {'Box': {'rows': 4, 'cols': 4}}),
                ("2x2", {'Box': {'rows': 2, 'cols': 2}}),
            ]
        self.invalid_inputs: list[str] = \
            [
                "abc",
                "3xx3",
                "3x",
                "x3x",
                "3x-3",
            ]


if __name__ == "__main__":
    unittest.main()
