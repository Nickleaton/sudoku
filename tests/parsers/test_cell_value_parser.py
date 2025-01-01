"""TestCellValueParser."""
import unittest
from typing import List, Tuple, Any

from src.parsers.cell_value_parser import CellValueParser
from tests.parsers.test_parser import TestParser


class TestCellValueParser(TestParser):
    """Test case for the CellValueParser class."""

    def setUp(self):
        """Set up the CellValueParser instance for testing."""
        self.parser: CellValueParser = CellValueParser()
        self.representation: str = "CellValueParser()"
        self.example_format: str = 'rc=dd'
        self.valid_input_result: List[Tuple[str, Any]] = [
            # Valid input_types for the Cell Value format
            (
                "12=5",
                [1, 2, 5]
            ),
            (
                "34=10",
                [3, 4, 10]
            ),
            (
                "56=100",
                [5, 6, 100]
            ),
            (
                "78=42",
                [7, 8, 42]
            ),
            (
                "90=1",
                [9, 0, 1]
            ),
        ]
        self.valid_input_answer: List[Tuple[str, Any]] = [
            # Valid input_types for the Cell Value format
            (
                "12=5",
                {'row': '1', 'column': '2', 'number': '5'}
            ),
            (
                "34=10",
                {'row': '3', 'column': '4', 'number': '10'}
            ),
            (
                "56=100",
                {'row': '5', 'column': '6', 'number': '100'}
            ),
            (
                "78=42",
                {'row': '7', 'column': '8', 'number': '42'}
            ),
            (
                "90=1",
                {'row': '9', 'column': '0', 'number': '1'}
            )
        ]
        self.invalid_input: List[str] = [
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
