"""TestRossiniParser."""
import unittest

from src.parsers.rossini_parser import RossiniParser
from tests.parsers.test_parser import TestParser


class TestRossiniParser(TestParser):
    """Test case for the RossiniParser class."""

    def setUp(self):
        """Set up the RossiniParser instance for testing."""
        super().setUp()
        self.parser: RossiniParser = RossiniParser()
        self.representation: str = "RossiniParser()"
        self.empty_allowed = False
        self.valid_inputs = [
            # Valid input_types for the Rossini format
            ("T0=D", {'Rossini': {'Side': 'T', 'Index': 0, 'Order': 'D'}}),
            ("L1=I", {'Rossini': {'Side': 'L', 'Index': 1, 'Order': 'I'}}),
            ("B2=U", {'Rossini': {'Side': 'B', 'Index': 2, 'Order': 'U'}}),
            ("R3=D", {'Rossini': {'Side': 'R', 'Index': 3, 'Order': 'D'}}),
            ("T4=I", {'Rossini': {'Side': 'T', 'Index': 4, 'Order': 'I'}}),
            ("B5=U", {'Rossini': {'Side': 'B', 'Index': 5, 'Order': 'U'}}),
            ("R9=D", {'Rossini': {'Side': 'R', 'Index': 9, 'Order': 'D'}}),
        ]

        self.invalid_inputs: list[str] = [
            # Invalid input_types that should raise ParserError
            "A0=D",  # Invalid side character
            "L10=I",  # Invalid digit (more than one)
            "T2=X",  # Invalid Order character
            "T2=DI",  # Invalid (two characters for Order)
            "L3= ",  # Right side contains start space only
            "R=U",  # Missing index
            "=I",  # Missing side and index
            "L4D",  # Missing equals sign
            "T0==D",  # Invalid due to double equals
            "B7=DD",  # Invalid due to double Order characters
        ]


if __name__ == "__main__":
    unittest.main()
