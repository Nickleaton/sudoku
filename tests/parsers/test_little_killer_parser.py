"""TestLittleKillerParser."""
import unittest
from typing import list

from src.parsers.little_killer_parser import LittleKillerParser
from tests.parsers.test_parser import TestParser


class TestLittleKillerParser(TestParser):
    """Test case for the LittleKillerParser class."""

    def setUp(self):
        """Set up the LittleKillerParser instance for testing."""
        super().setUp()
        self.parser: LittleKillerParser = LittleKillerParser()
        self.representation: str = 'LittleKillerParser()'
        self.empty_allowed = False
        self.valid_inputs: list[tuple[str, dict[str, dict[str, str | int]]]] = [
            # Valid Little Killers format input_types
            ("T1C=14", {'LittleKiller': {'Side': 'T', 'Index': 1, 'Cyclic': 'C', 'Value': 14}}),
            ("T1C=5", {'LittleKiller': {'Side': 'T', 'Index': 1, 'Cyclic': 'C', 'Value': 5}}),
            ("L2A=10", {'LittleKiller': {'Side': 'L', 'Index': 2, 'Cyclic': 'A', 'Value': 10}}),
            ("B3C=12", {'LittleKiller': {'Side': 'B', 'Index': 3, 'Cyclic': 'C', 'Value': 12}}),
            ("R0A=0", {'LittleKiller': {'Side': 'R', 'Index': 0, 'Cyclic': 'A', 'Value': 0}}),
            ("T9C=100", {'LittleKiller': {'Side': 'T', 'Index': 9, 'Cyclic': 'C', 'Value': 100}}),
            ("L5A=50", {'LittleKiller': {'Side': 'L', 'Index': 5, 'Cyclic': 'A', 'Value': 50}}),
            ("T0C=1", {'LittleKiller': {'Side': 'T', 'Index': 0, 'Cyclic': 'C', 'Value': 1}}),
            ("R9A=999", {'LittleKiller': {'Side': 'R', 'Index': 9, 'Cyclic': 'A', 'Value': 999}}),
            ("B4C=2000", {'LittleKiller': {'Side': 'B', 'Index': 4, 'Cyclic': 'C', 'Value': 2000}}),
        ]
        self.invalid_inputs: list[str] = \
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
