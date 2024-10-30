import unittest
from typing import List, Tuple, Any

from src.parsers.vertex_digit_parser import VertexDigitParser
from tests.parsers.test_parser import TestParser


class TestVertexDigitParser(TestParser):
    """Test case for the VertexDigitParser class."""

    def setUp(self):
        """Sets up the VertexDigitParser instance for testing."""
        self.parser: VertexDigitParser = VertexDigitParser()
        self.representation: str = 'VertexDigitParser()'
        self.valid_input_result: List[Tuple[str, Any]] = [
            # Valid inputs for the Vertex Digit format
            (
                "12=3",
                [[1, 2], 3]
            ),
            (
                "34=0",
                [[3, 4], 0]
            ),
            (
                "56=7",
                [[5, 6], 7]
            ),
            (
                "78=9",
                [[7, 8], 9]
            ),
            (
                "90=1",
                [[9, 0], 1]
            ),
        ]
        self.valid_input_answer: List[Tuple[str, Any]] = [
            # Valid inputs for the Vertex Digit format
            (
                "12=3",
                {
                    'vertex': {'row': '1', 'column': '2'},
                    'digit': '3'
                }
            ),
            (
                "34=0",
                {
                    'vertex': {'row': '3', 'column': '4'},
                    'digit': '0'
                }
            ),
            (
                "56=7",
                {
                    'vertex': {'row': '5', 'column': '6'},
                    'digit': '7'
                }
            ),
            (
                "78=9",
                {
                    'vertex': {'row': '7', 'column': '8'},
                    'digit': '9'
                }
            ),
            (
                "90=1",
                {
                    'vertex': {'row': '9', 'column': '0'},
                    'digit': '1'
                }
            ),
        ]
        self.invalid_input: List[str] = [
            # Invalid inputs that should raise ParserError
            "1=3",  # One digit on the left side
            "123=4",  # More than two digits on the left side
            "12=a",  # Invalid value (not a digit)
            "34==5",  # Invalid due to double equals
            "56= ",  # Missing value
            "78=10",  # Invalid (more than one digit)
            "=9",  # Missing left side
            "12= ",  # Whitespace only after equals
            "12=5a",  # Invalid value (non-digit character)
        ]


if __name__ == "__main__":
    unittest.main()
