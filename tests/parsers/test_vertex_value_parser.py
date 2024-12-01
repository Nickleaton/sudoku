"""TestVertexValueParser."""
import unittest
from typing import List, Tuple, Any

from src.parsers.vertex_value_parser import VertexValueParser
from tests.parsers.test_parser import TestParser


class TestVertexValueParser(TestParser):
    """Test case for the VertexValueParser class."""

    def setUp(self):
        """Set up the VertexValueParser instance for testing."""
        self.parser: VertexValueParser = VertexValueParser()
        self.representation: str = 'VertexValueParser()'
        self.example_format: str = 'rc=dd'
        self.valid_input_result: List[Tuple[str, Any]] = [
            # Valid input_types for the Vertex Value format
            (
                "12=123",
                [1, 2, 123]
            ),
            (
                "34=0",
                [3, 4, 0]
            ),
            (
                "56=789",
                [5, 6, 789]
            ),
            (
                "78=4567",
                [7, 8, 4567]
            ),
            (
                "90=1000",
                [9, 0, 1000]
            ),
        ]
        self.valid_input_answer: List[Tuple[str, Any]] = [
            # Valid input_types for the Vertex Value format
            (
                "12=123",
                {'row': '1', 'column': '2', 'value': '123'}
            ),
            (
                "34=0",
                {'row': '3', 'column': '4', 'value': '0'}
            ),
            (
                "56=789",
                {'row': '5', 'column': '6', 'value': '789'}
            ),
            (
                "78=4567",
                {'row': '7', 'column': '8', 'value': '4567'}
            ),
            (
                "90=1000",
                {'row': '9', 'column': '0', 'value': '1000'}
            ),
        ]

        self.invalid_input: List[str] = [
            # Invalid input_types that should raise ParserError
            "1=3",  # One digit on the left side
            "123=4",  # More than two digits on the left side
            "12=a",  # Invalid value (not a digit)
            "34==5",  # Invalid due to double equals
            "56= ",  # Missing value
            "=9",  # Missing left side
            "12= ",  # Whitespace only after equals
            "12=5a",  # Invalid value (non-digit character)
        ]


if __name__ == "__main__":
    unittest.main()

