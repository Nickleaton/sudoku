"""TestCellParser."""
import unittest
from typing import Any

from src.parsers.cell_parser import CellParser
from tests.parsers.test_parser import TestParser


class TestCellParser(TestParser):
    """Test case for the CellParser class."""

    def setUp(self):
        """Set up the CellParser instance for testing."""
        super().setUp()
        self.parser: CellParser = CellParser()
        self.representation: str = "CellParser()"
        self.empty_allowed = False
        self.valid_inputs: list[tuple[str, Any]] = \
            [
                ("12", {'Cell': {"row": 1, "col": 2}}),
                ("01", {'Cell': {"row": 0, "col": 1}}),
                ("99", {'Cell': {"row": 9, "col": 9}}),
            ]
        self.invalid_inputs: list[str] = \
            [
                # Invalid input_types that should raise ParserError
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
