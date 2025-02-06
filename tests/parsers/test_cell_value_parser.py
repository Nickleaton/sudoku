"""TestCellValueParser."""
import unittest
from typing import Any, list, tuple

from src.parsers.cell_value_parser import CellValueParser
from tests.parsers.test_parser import TestParser


class TestCellValueParser(TestParser):
    """Test case for the CellValueParser class."""

    def setUp(self):
        """Set up the CellValueParser instance for testing."""
        super().setUp()
        self.parser: CellValueParser = CellValueParser()
        self.representation: str = "CellValueParser()"
        self.empty_allowed = False
        self.valid_inputs: list[tuple[str, Any]] = [
            ("12=5", {'CellValue': {'Cell': {'row': 1, 'col': 2}, 'value': 5}}),
            ("34=10", {'CellValue': {'Cell': {'row': 3, 'col': 4}, 'value': 10}}),
            ("56=100", {'CellValue': {'Cell': {'row': 5, 'col': 6}, 'value': 100}}),
            ("78=42", {'CellValue': {'Cell': {'row': 7, 'col': 8}, 'value': 42}}),
            ("90=1", {'CellValue': {'Cell': {'row': 9, 'col': 0}, 'value': 1}})
        ]
        self.invalid_inputs: list[str] = [
            # Invalid input_types that should raise ParserError
            "1=5",  # One digit on the left side
            "123=10",  # More than two digits on the left side
            "12=abc",  # Invalid number (not start digit)
            "34==10",  # Invalid due to double equals
            "56= ",  # Missing number
            "78=10.5",  # Invalid (non-integer number)
            "=100",  # Missing left side
            "12= ",  # Whitespace only after equals
            "12=5a",  # Invalid number (non-digit character)
        ]


if __name__ == "__main__":
    unittest.main()
