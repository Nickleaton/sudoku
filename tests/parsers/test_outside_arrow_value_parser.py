import unittest
from typing import List, Tuple, Any

from src.parsers.outside_arrow_value_parser import OutsideArrowValueParser
from tests.parsers.test_parser import TestParser


class TestOutsideArrowValueParser(TestParser):
    """Test case for the OutsideArrowValueParser class."""

    def setUp(self):
        """Sets up the OutsideArrowValueParser instance for testing."""
        self.parser: OutsideArrowValueParser = OutsideArrowValueParser()
        self.representation: str = 'OutsideArrowValueParser()'
        self.valid_input: List[Tuple[str, Any]] = [
            # Valid inputs for the Outside Arrow Value format
            ("T0=5", ['T', 0, 5]),
            ("L1=10", ['L', 1, 10]),
            ("B2=20", ['B', 2, 20]),
            ("R3=100", ['R', 3, 100]),
            ("T4=42", ['T', 4, 42]),
            ("B5=1", ['B', 5, 1]),
            ("R9=999", ['R', 9, 999]),
        ]

        self.invalid_input: List[str] = [
            # Invalid inputs that should raise ParserError
            "A0=5",  # Invalid side character
            "L10=10",  # Invalid index (more than one digit)
            "T2=D",  # Invalid value (not a digit)
            "L3=I4",  # Invalid (non-digit after equals)
            "B7=",  # Missing value
            "R=5",  # Missing index
            "=10",  # Missing side and index
            "T0==5",  # Invalid due to double equals
            "T3=1a",  # Invalid value (non-digit character)
            "B4=5,6",  # Invalid due to multiple values
        ]


if __name__ == "__main__":
    unittest.main()
