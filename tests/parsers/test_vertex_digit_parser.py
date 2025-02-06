"""TestVertexDigitParser."""
import unittest
from typing import list, tuple

from src.parsers.vertex_digit_parser import VertexDigitParser
from tests.parsers.test_parser import TestParser


class TestVertexDigitParser(TestParser):
    """Test case for the VertexDigitParser class."""

    def setUp(self):
        """Set up the VertexDigitParser instance for testing."""
        super().setUp()
        self.parser: VertexDigitParser = VertexDigitParser()
        self.representation: str = 'VertexDigitParser()'
        self.empty_allowed = False
        self.valid_inputs: list[tuple[str, dict[str, dict[str, int] | int]]] = [
            ("12=3", {'Vertex': {'Cell': {'row': 1, 'col': 2}, 'Digit': 3}}),
            ("34=0", {'Vertex': {'Cell': {'row': 3, 'col': 4}, 'Digit': 0}}),
            ("56=7", {'Vertex': {'Cell': {'row': 5, 'col': 6}, 'Digit': 7}}),
            ("78=9", {'Vertex': {'Cell': {'row': 7, 'col': 8}, 'Digit': 9}}),
            ("90=1", {'Vertex': {'Cell': {'row': 9, 'col': 0}, 'Digit': 1}}),
        ]
        self.invalid_inputs: list[str] = [
            # Invalid input_types that should raise ParserError
            "1=3",  # One digit on the left side
            "123=4",  # More than two digits on the left side
            "12=start",  # Invalid number (not start digit)
            "34==5",  # Invalid due to double equals
            "56= ",  # Missing number
            "78=10",  # Invalid (more than one digit)
            "=9",  # Missing left side
            "12= ",  # Whitespace only after equals
            "12=5a",  # Invalid number (non-digit character)
        ]


if __name__ == "__main__":
    unittest.main()
