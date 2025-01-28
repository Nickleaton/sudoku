"""TestVertexDigitParser."""
import unittest
from typing import List, Tuple, Any

from src.parsers.vertex_digit_parser import VertexDigitParser
from tests.parsers.test_parser import TestParser


class TestVertexDigitParser(TestParser):
    """Test case for the VertexDigitParser class."""

    def setUp(self):
        """Set up the VertexDigitParser instance for testing."""
        self.parser: VertexDigitParser = VertexDigitParser()
        self.representation: str = 'VertexDigitParser()'
        self.example_format: str = 'rc=d'
        self.valid_input_result: List[Tuple[str, Any]] = [
            # Valid input_types for the Vertex Digits format
            (
                "12=3",
                [1, 2, 3]
            ),
            (
                "34=0",
                [3, 4, 0]
            ),
            (
                "56=7",
                [5, 6, 7]
            ),
            (
                "78=9",
                [7, 8, 9]
            ),
            (
                "90=1",
                [9, 0, 1]
            ),
        ]
        self.valid_input_answer: List[Tuple[str, Any]] = [
            # Valid input_types for the Vertex Digits format
            (
                "12=3",
                {
                    'row': '1',
                    'column': '2',
                    'digit': '3'
                }
            ),
            (
                "34=0",
                {
                    'row': '3',
                    'column': '4',
                    'digit': '0'
                }
            ),
            (
                "56=7",
                {
                    'row': '5',
                    'column': '6',
                    'digit': '7'
                }
            ),
            (
                "78=9",
                {
                    'row': '7',
                    'column': '8',
                    'digit': '9'
                }
            ),
            (
                "90=1",
                {
                    'row': '9',
                    'column': '0',
                    'digit': '1'
                }
            ),
        ]
        self.invalid_input: List[str] = [
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
