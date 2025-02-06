"""TestVertexValueParser."""
import unittest

from src.parsers.vertex_value_parser import VertexValueParser
from tests.parsers.test_parser import TestParser


class TestVertexValueParser(TestParser):
    """Test case for the VertexValueParser class."""

    def setUp(self):
        """Set up the VertexValueParser instance for testing."""
        super().setUp()
        self.parser: VertexValueParser = VertexValueParser()
        self.representation: str = 'VertexValueParser()'
        self.empty_allowed = False
        self.valid_inputs: list[tuple[str, Dict[str, dict[str, int] | int]]] = [
            # Valid input_types for the Vertex Value format
            ("12=123", {'Vertex': {'Cell': {'row': 1, 'col': 2}, 'Value': 123}}),
            ("34=0", {'Vertex': {'Cell': {'row': 3, 'col': 4}, 'Value': 0}}),
            ("56=789", {'Vertex': {'Cell': {'row': 5, 'col': 6}, 'Value': 789}}),
            ("78=4567", {'Vertex': {'Cell': {'row': 7, 'col': 8}, 'Value': 4567}}),
            ("90=1000", {'Vertex': {'Cell': {'row': 9, 'col': 0}, 'Value': 1000}}),
        ]
        self.invalid_inputs: list[str] = [
            # Invalid input_types that should raise ParserError
            "1=3",  # One digit on the left side
            "123=4",  # More than two digits on the left side
            "12=start",  # Invalid number (not start digit)
            "34==5",  # Invalid due to double equals
            "56= ",  # Missing number
            "=9",  # Missing left side
            "12= ",  # Whitespace only after equals
            "12=5a",  # Invalid number (non-digit character)
        ]


if __name__ == "__main__":
    unittest.main()
