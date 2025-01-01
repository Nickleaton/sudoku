"""TestLittleKillerParser."""
import unittest
from typing import List, Tuple, Any

from src.parsers.little_killer_parser import LittleKillerParser
from tests.parsers.test_parser import TestParser


class TestLittleKillerParser(TestParser):
    """Test case for the LittleKillerParser class."""

    def setUp(self):
        """Set up the LittleKillerParser instance for testing."""
        self.parser: LittleKillerParser = LittleKillerParser()
        self.representation: str = 'LittleKillerParser()'
        self.example_format: str = '[TLBR]i=dd'
        self.valid_input_result: List[Tuple[str, Any]] = \
            [
                # Valid Little Killers format input_types
                (
                    "T1C=14",
                    ['T', 1, 'C', 14]
                ),
                (
                    "T1C=5",
                    ['T', 1, 'C', 5]
                ),
                (
                    "L2A=10",
                    ['L', 2, 'A', 10]
                ),
                (
                    "B3C=12",
                    ['B', 3, 'C', 12]
                ),
                (
                    "R0A=0",
                    ['R', 0, 'A', 0]
                ),
                (
                    "T9C=100",
                    ['T', 9, 'C', 100]
                ),
                (
                    "L5A=50",
                    ['L', 5, 'A', 50]
                ),
                (
                    "T0C=1",
                    ['T', 0, 'C', 1]
                ),
                (
                    "R9A=999",
                    ['R', 9, 'A', 999]
                ),
                (
                    "B4C=2000",
                    ['B', 4, 'C', 2000]
                ),
                # Valid input with spaces
                (
                    " L2 A = 5 ",
                    ['L', 2, 'A', 5]
                ),
            ]
        self.valid_input_answer: List[Tuple[str, Any]] = [
            # Valid Little Killers format input_types
            (
                "T1C=14",
                {'side': 'T', 'index': '1', 'direction': 'C', 'number': '14'}
            ),
            (
                "T1C=5",
                {'side': 'T', 'index': '1', 'direction': 'C', 'number': '5'}
            ),
            (
                "L2A=10",
                {'side': 'L', 'index': '2', 'direction': 'A', 'number': '10'}
            ),
            (
                "B3C=12",
                {'side': 'B', 'index': '3', 'direction': 'C', 'number': '12'}
            ),
            (
                "R0A=0",
                {'side': 'R', 'index': '0', 'direction': 'A', 'number': '0'}
            ),
            (
                "T9C=100",
                {'side': 'T', 'index': '9', 'direction': 'C', 'number': '100'}
            ),
            (
                "L5A=50",
                {'side': 'L', 'index': '5', 'direction': 'A', 'number': '50'}
            ),
            (
                "T0C=1",
                {'side': 'T', 'index': '0', 'direction': 'C', 'number': '1'}
            ),
            (
                "R9A=999",
                {'side': 'R', 'index': '9', 'direction': 'A', 'number': '999'}
            ),
            (
                "B4C=2000",
                {'side': 'B', 'index': '4', 'direction': 'C', 'number': '2000'}
            ),
            # Valid input with spaces
            (
                " L2 A = 5 ",
                {'side': 'L', 'index': '2', 'direction': 'A', 'number': '5'}
            ),
        ]

        self.invalid_input: List[str] = \
            [
                # Invalid input_types that should raise ParserError
                "X1C=5",  # Invalid side (not T, L, B, or R)
                "T1D=10",  # Invalid direction (not C or A)
                "T11C=10",  # Invalid index (out of range)
                "B2=10",  # Missing direction
                "T1C=abc",  # Non-integer number
                "C=5",  # Missing side and index
                "T2C=5=10",  # Multiple '=' signs
                "L2A=10x",  # Extra characters after valid input
                " T2C= ",  # Empty number after '='
                "T1CA=5",  # Invalid format (wrong character sequence)
                "L2A=10 20",  # Invalid due to extra number after '='
                "   ",  # Whitespace only
            ]


if __name__ == "__main__":
    unittest.main()
