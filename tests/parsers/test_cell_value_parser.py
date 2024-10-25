import unittest
from typing import List, Tuple, Any

from src.parsers.cell_value_parser import CellValueParser
from tests.parsers.test_parser import TestParser


class TestCellValueParser(TestParser):
    """Test case for the CellValueParser class."""

    def setUp(self):
        """Sets up the CellValueParser instance for testing."""
        self.parser = CellValueParser()
        self.valid_input: List[Tuple[str, Any]] = [
            # Valid inputs for the Cell Value format
            ("12=5", [[1, 2], 5]),
            ("34=10", [[3, 4], 10]),
            ("56=100", [[5, 6], 100]),
            ("78=42", [[7, 8], 42]),
            ("90=1", [[9, 0], 1]),
        ]

        self.invalid_input: List[str] = [
            # Invalid inputs that should raise ParserError
            "1=5",  # One digit on the left side
            "123=10",  # More than two digits on the left side
            "12=abc",  # Invalid value (not a digit)
            "34==10",  # Invalid due to double equals
            "56= ",  # Missing value
            "78=10.5",  # Invalid (non-integer value)
            "=100",  # Missing left side
            "12= ",  # Whitespace only after equals
            "12=5a",  # Invalid value (non-digit character)
        ]


if __name__ == "__main__":
    unittest.main()
