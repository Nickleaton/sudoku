import unittest
from typing import List, Tuple, Any

from src.parsers.cell_parser import CellParser
from tests.parsers.test_parser import TestParser


class TestCellParser(TestParser):
    """Test case for the CellParser class."""

    def setUp(self):
        """Sets up the CellParser instance for testing."""
        self.parser = CellParser()
        self.valid_input: List[Tuple[str, Any]] = \
            [
                ("12", [1, 2]),
                ("01", [0, 1]),
                ("99", [9, 9]),
                # Valid inputs with leading/trailing whitespace
                (" 12 ", [1, 2]),
                (" 01 ", [0, 1]),
                ("  99  ", [9, 9]),
            ]
        self.invalid_input: List[str] = \
            [
                # Invalid inputs that should raise ParserError
                "1",  # Only one digit
                "123",  # More than two digits
                "a2",  # Non-digit character
                "12a",  # Non-digit character at the end
                "  ",  # Empty input with spaces
                "12 34",  # Two pairs of digits
                " 12, 34 ",  # Comma separating valid pairs
                "abc",  # Completely invalid input
                "12.34",  # Invalid due to decimal
            ]


if __name__ == "__main__":
    unittest.main()
