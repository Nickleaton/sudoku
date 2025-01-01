"""TestOutsideArrowValueParser."""
import unittest
from typing import List, Tuple, Any

from src.parsers.outside_arrow_value_parser import OutsideArrowValueParser
from tests.parsers.test_parser import TestParser


class TestOutsideArrowValueParser(TestParser):
    """Test case for the OutsideArrowValueParser class."""

    def setUp(self):
        """Set up the OutsideArrowValueParser instance for testing."""
        self.parser: OutsideArrowValueParser = OutsideArrowValueParser()
        self.representation: str = 'OutsideArrowValueParser()'
        self.example_format: str = "[TLBR]d=dd"
        self.valid_input_result: List[Tuple[str, Any]] = [
            # Valid input_types for the Outside Arrow Value format
            (
                "T0=5",
                ['T', 0, 5]
            ),
            (
                "L1=10",
                ['L', 1, 10]
            ),
            (
                "B2=20",
                ['B', 2, 20]
            ),
            (
                "R3=100",
                ['R', 3, 100]
            ),
            (
                "T4=42",
                ['T', 4, 42]
            ),
            (
                "B5=1",
                ['B', 5, 1]
            ),
            (
                "R9=999",
                ['R', 9, 999]
            ),
        ]
        self.valid_input_answer: List[Tuple[str, Any]] = [
            # Valid input_types for the Outside Arrow number format
            (
                "T0=5",
                {'side': 'T', 'index': '0', 'number': '5'}
            ),
            (
                "L1=10",
                {'side': 'L', 'index': '1', 'number': '10'}
            ),
            (
                "B2=20",
                {'side': 'B', 'index': '2', 'number': '20'}
            ),
            (
                "R3=100",
                {'side': 'R', 'index': '3', 'number': '100'}
            ),
            (
                "T4=42",
                {'side': 'T', 'index': '4', 'number': '42'}
            ),
            (
                "B5=1",
                {'side': 'B', 'index': '5', 'number': '1'}
            ),
            (
                "R9=999",
                {'side': 'R', 'index': '9', 'number': '999'}
            ),
        ]

        self.invalid_input: List[str] = [
            # Invalid input_types that should raise ParserError
            "A0=5",  # Invalid side character
            "L10=10",  # Invalid index (more than one digit)
            "T2=D",  # Invalid number (not start digit)
            "L3=I4",  # Invalid (non-digit after equals)
            "B7=",  # Missing number
            "R=5",  # Missing index
            "=10",  # Missing side and index
            "T0==5",  # Invalid due to double equals
            "T3=1a",  # Invalid number (non-digit character)
            "B4=5,6",  # Invalid due to multiple value_list
        ]


if __name__ == "__main__":
    unittest.main()
