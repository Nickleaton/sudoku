"""TestRossiniParser."""
import unittest
from typing import List, Tuple, Any

from src.parsers.rossini_parser import RossiniParser
from tests.parsers.test_parser import TestParser


class TestRossiniParser(TestParser):
    """Test case for the RossiniParser class."""

    def setUp(self):
        """Set up the RossiniParser instance for testing."""
        self.parser: RossiniParser = RossiniParser()
        self.representation: str = "RossiniParser()"
        self.example_format: str = '[TLBR]d=[DIU]'
        self.valid_input_result: List[Tuple[str, Any]] = [
            # Valid input_types for the Rossini format
            (
                "T0=D",
                ['T', 0, 'D']
            ),
            (
                "L1=I",
                ['L', 1, 'I']
            ),
            (
                "B2=U",
                ['B', 2, 'U']
            ),
            (
                "R3=D",
                ['R', 3, 'D']
            ),
            (
                "T4=I",
                ['T', 4, 'I']
            ),
            (
                "B5=U",
                ['B', 5, 'U']
            ),
            (
                "R9=D",
                ['R', 9, 'D']
            ),
        ]
        self.valid_input_answer: List[Tuple[str, Any]] = [
            # Valid input_types for the Rossini format
            (
                "T0=D",
                {'side': 'T', 'index': '0', 'direction': 'D'}
            ),
            (
                "L1=I",
                {'side': 'L', 'index': '1', 'direction': 'I'}
            ),
            (
                "B2=U",
                {'side': 'B', 'index': '2', 'direction': 'U'}
            ),
            (
                "R3=D",
                {'side': 'R', 'index': '3', 'direction': 'D'}
            ),
            (
                "T4=I",
                {'side': 'T', 'index': '4', 'direction': 'I'}
            ),
            (
                "B5=U",
                {'side': 'B', 'index': '5', 'direction': 'U'}
            ),
            (
                "R9=D",
                {'side': 'R', 'index': '9', 'direction': 'D'}
            ),
        ]

        self.invalid_input: List[str] = [
            # Invalid input_types that should raise ParserError
            "A0=D",  # Invalid side character
            "L10=I",  # Invalid digit (more than one)
            "T2=X",  # Invalid direction character
            "T2=DI",  # Invalid (two characters for direction)
            "L3= ",  # Right side contains a space only
            "R=U",  # Missing index
            "=I",  # Missing side and index
            "L4D",  # Missing equals sign
            "T0==D",  # Invalid due to double equals
            "B7=DD",  # Invalid due to double direction characters
        ]


if __name__ == "__main__":
    unittest.main()

