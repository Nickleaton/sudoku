"""TestFrameParser."""
import unittest
from typing import Any

from src.parsers.frame_parser import FrameParser
from tests.parsers.test_parser import TestParser


class TestFrameParser(TestParser):
    """Test case for the FrameParser class."""

    def setUp(self):
        """Set up the FrameParser instance for testing."""
        super().setUp()
        self.parser: FrameParser = FrameParser()
        self.representation: str = 'FrameParser()'
        self.empty_allowed = False
        self.valid_inputs: list[tuple[str, Any]] = \
            [
                # Valid FrameParser format input_types
                ("T1=2", {'Frame': {'Side': 'T', 'Index': 1, 'Value': 2}}),
                ("L3=10", {'Frame': {'Side': 'L', 'Index': 3, 'Value': 10}}),
                ("B0=5", {'Frame': {'Side': 'B', 'Index': 0, 'Value': 5}}),
                ("R9=99", {'Frame': {'Side': 'R', 'Index': 9, 'Value': 99}}),
                ("T2=123", {'Frame': {'Side': 'T', 'Index': 2, 'Value': 123}}),
            ]
        self.invalid_inputs: list[str] = \
            [
                # Invalid input_types that should raise ParserError
                "X1=5",  # Invalid side (not T, L, B, or R)
                "T1D=10",  # Extra character after '='
                "T11=10",  # Invalid index (too long)
                "B=10",  # Missing index
                "T1=abc",  # Non-integer number
                "T1=",  # Missing number after '='
                "T1==2",  # Multiple '=' signs
                "L2=5x",  # Extra characters after valid input
                "   ",  # Whitespace only
            ]


if __name__ == "__main__":
    unittest.main()
