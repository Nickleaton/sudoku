import unittest
from typing import List, Tuple, Any

from src.parsers.little_killers_parser import LittleKillersParser
from tests.parsers.test_parser import TestParser


class TestLittleKillersParser(TestParser):
    """Test case for the LittleKillersParser class."""

    def setUp(self):
        """Sets up the LittleKillersParser instance for testing."""
        self.parser: LittleKillersParser = LittleKillersParser()
        self.representation: str = 'LittleKillersParser()'
        self.valid_input: List[Tuple[str, Any]] = \
            [
                # Valid Little Killers format inputs
                ("T1C=5", ['T', 1, 'C', 5]),
                ("L2A=10", ['L', 2, 'A', 10]),
                ("B3C=12", ['B', 3, 'C', 12]),
                ("R0A=0", ['R', 0, 'A', 0]),
                ("T9C=100", ['T', 9, 'C', 100]),
                ("L5A=50", ['L', 5, 'A', 50]),
                ("T0C=1", ['T', 0, 'C', 1]),
                ("R9A=999", ['R', 9, 'A', 999]),
                ("B4C=2000", ['B', 4, 'C', 2000]),
                # Valid input with spaces
                (" L2 A = 5 ", ['L', 2, 'A', 5]),
            ]
        self.invalid_input: List[str] = \
            [
                # Invalid inputs that should raise ParserError
                "X1C=5",  # Invalid side (not T, L, B, or R)
                "T1D=10",  # Invalid direction (not C or A)
                "T11C=10",  # Invalid index (out of range)
                "B2=10",  # Missing direction
                "T1C=abc",  # Non-integer value
                "C=5",  # Missing side and index
                "T2C=5=10",  # Multiple '=' signs
                "L2A=10x",  # Extra characters after valid input
                " T2C= ",  # Empty value after '='
                "T1CA=5",  # Invalid format (wrong character sequence)
                "L2A=10 20",  # Invalid due to extra value after '='
                "   ",  # Whitespace only
            ]


if __name__ == "__main__":
    unittest.main()
