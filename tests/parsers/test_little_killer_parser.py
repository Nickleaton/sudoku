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
                {'Side': 'T', 'Index': '1', 'Cyclic': 'C', 'Value': '14'}
            ),
            (
                "T1C=5",
                {'Side': 'T', 'Index': '1', 'Cyclic': 'C', 'Value': '5'}
            ),
            (
                "L2A=10",
                {'Side': 'L', 'Index': '2', 'Cyclic': 'A', 'Value': '10'}
            ),
            (
                "B3C=12",
                {'Side': 'B', 'Index': '3', 'Cyclic': 'C', 'Value': '12'}
            ),
            (
                "R0A=0",
                {'Side': 'R', 'Index': '0', 'Cyclic': 'A', 'Value': '0'}
            ),
            (
                "T9C=100",
                {'Side': 'T', 'Index': '9', 'Cyclic': 'C', 'Value': '100'}
            ),
            (
                "L5A=50",
                {'Side': 'L', 'Index': '5', 'Cyclic': 'A', 'Value': '50'}
            ),
            (
                "T0C=1",
                {'Side': 'T', 'Index': '0', 'Cyclic': 'C', 'Value': '1'}
            ),
            (
                "R9A=999",
                {'Side': 'R', 'Index': '9', 'Cyclic': 'A', 'Value': '999'}
            ),
            (
                "B4C=2000",
                {'Side': 'B', 'Index': '4', 'Cyclic': 'C', 'Value': '2000'}
            ),
            # Valid input with spaces
            (
                " L2 A = 5 ",
                {'Side': 'L', 'Index': '2', 'Cyclic': 'A', 'Value': '5'}
            ),
        ]

        self.invalid_input: List[str] = \
            [
                # Invalid input_types that should raise ParserError
                "X1C=5",  # Invalid side (not T, L, B, or R)
                "T1D=10",  # Invalid Cyclic (not C or A)
                "T11C=10",  # Invalid Index (out of range)
                "B2=10",  # Missing Cyclic
                "T1C=abc",  # Non-integer Value
                "C=5",  # Missing side and Index
                "T2C=5=10",  # Multiple '=' signs
                "L2A=10x",  # Extra characters after valid input
                " T2C= ",  # Empty Value after '='
                "T1CA=5",  # Invalid format (wrong character sequence)
                "L2A=10 20",  # Invalid due to extra Value after '='
                "   ",  # Whitespace only
            ]


if __name__ == "__main__":
    unittest.main()
