"""TestOutsideArrowValueParser."""
import unittest
from typing import Any, List, Tuple

from src.parsers.outside_arrow_value_parser import OutsideArrowValueParser
from tests.parsers.test_parser import TestParser


class TestOutsideArrowValueParser(TestParser):
    """Test case for the OutsideArrowValueParser class."""

    def setUp(self):
        """Set up the OutsideArrowValueParser instance for testing."""
        super().setUp()
        self.parser: OutsideArrowValueParser = OutsideArrowValueParser()
        self.representation: str = 'OutsideArrowValueParser()'
        self.empty_allowed = False
        self.valid_inputs: List[Tuple[str, Any]] = [
            # Valid input_types for the Outside Arrow number format
            ("T0D=5", {'Arrow': {'Side': 'T', 'Direction': 'D', 'Index': 0, 'Value': 5}}),
            ("T5DR=5", {'Arrow': {'Side': 'T', 'Direction': 'DR', 'Index': 5, 'Value': 5}}),
            ("T5DL=5", {'Arrow': {'Side': 'T', 'Direction': 'DL', 'Index': 5, 'Value': 5}}),
            ("L1UR=10", {'Arrow': {'Side': 'L', 'Direction': 'UR', 'Index': 1, 'Value': 10}}),
            ("L1R=10", {'Arrow': {'Side': 'L', 'Direction': 'R', 'Index': 1, 'Value': 10}}),
            ("L1DR=10", {'Arrow': {'Side': 'L', 'Direction': 'DR', 'Index': 1, 'Value': 10}}),
            ("B2U=20", {'Arrow': {'Side': 'B', 'Direction': 'U', 'Index': 2, 'Value': 20}}),
            ("B2UL=20", {'Arrow': {'Side': 'B', 'Direction': 'UL', 'Index': 2, 'Value': 20}}),
            ("B2UR=20", {'Arrow': {'Side': 'B', 'Direction': 'UR', 'Index': 2, 'Value': 20}}),
            ("R3UL=100", {'Arrow': {'Side': 'R', 'Direction': 'UL', 'Index': 3, 'Value': 100}}),
            ("R3L=100", {'Arrow': {'Side': 'R', 'Direction': 'L', 'Index': 3, 'Value': 100}}),
            ("R3DL=100", {'Arrow': {'Side': 'R', 'Direction': 'DL', 'Index': 3, 'Value': 100}}),
        ]

        self.invalid_input2: List[str] = [
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
