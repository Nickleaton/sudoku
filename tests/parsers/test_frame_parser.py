"""TestFrameParser."""
import unittest
from typing import List, Tuple, Any

from src.parsers.frame_parser import FrameParser
from tests.parsers.test_parser import TestParser


class TestFrameParser(TestParser):
    """Test case for the FrameParser class."""

    def setUp(self):
        """Set up the FrameParser instance for testing."""
        self.parser: FrameParser = FrameParser()
        self.representation: str = 'FrameParser()'
        self.example_format: str = '[TLBR]i=v'
        self.valid_input_result: List[Tuple[str, Any]] = \
            [
                # Valid FrameParser format input_types
                (
                    "T1=2",
                    ['T', 1, 2]
                ),
                (
                    "L3=10",
                    ['L', 3, 10]
                ),
                (

                    "B0=5",
                    ['B', 0, 5]
                ),
                (
                    "R9=99",
                    ['R', 9, 99]
                ),
                (
                    "T2=123",
                    ['T', 2, 123]
                ),
                # Valid input with spaces
                (
                    " T 1 = 20 ",
                    ['T', 1, 20]
                ),
            ]
        self.valid_input_answer: List[Tuple[str, Any]] = \
            [
                # Valid FrameParser format input_types
                (
                    "T1=2",
                    {'side': 'T', 'index': '1', 'number': '2'}
                ),
                (
                    "L3=10",
                    {'side': 'L', 'index': '3', 'number': '10'}
                ),
                (
                    "B0=5",
                    {'side': 'B', 'index': '0', 'number': '5'}
                ),
                (
                    "R9=99",
                    {'side': 'R', 'index': '9', 'number': '99'}
                ),
                (
                    "T2=123",
                    {'side': 'T', 'index': '2', 'number': '123'}
                ),
                # Valid input with spaces
                (
                    " T 1 = 20 ",
                    {'side': 'T', 'index': '1', 'number': '20'}
                ),
            ]
        self.valid_input_result: List[Tuple[str, Any]] = \
            [
                # Valid FrameParser format input_types
                ("T1=2", ['T', 1, 2]),
                ("L3=10", ['L', 3, 10]),
                ("B0=5", ['B', 0, 5]),
                ("R9=99", ['R', 9, 99]),
                ("T2=123", ['T', 2, 123]),
                # Valid input with spaces
                (" T 1 = 20 ", ['T', 1, 20]),
            ]
        self.invalid_input: List[str] = \
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
