"""TestQuadruplesParser."""
import unittest
from typing import Any

from src.parsers.quadruples_parser import QuadruplesParser
from tests.parsers.test_parser import TestParser


class TestQuadruplesParser(TestParser):
    """Test case for the QuadruplesParser class."""

    def setUp(self):
        """Set up the QuadruplesParser instance for testing."""
        super().setUp()
        self.parser: QuadruplesParser = QuadruplesParser()
        self.representation: str = "QuadruplesParser()"
        self.empty_allowed = False
        self.valid_inputs: list[tuple[str, Any]] = [
            # Valid quadruples format input_types
            ("12=123", {'Quad': {'Vertex': {'row': 1, 'col': 2}, 'Values': [1, 2, 3]}}),
            ("01=456", {'Quad': {'Vertex': {'row': 0, 'col': 1}, 'Values': [4, 5, 6]}}),
            ("30=10", {'Quad': {'Vertex': {'row': 3, 'col': 0}, 'Values': [1, 0]}}),
            ("23=2", {'Quad': {'Vertex': {'row': 2, 'col': 3}, 'Values': [2]}}),
            ("88=0", {'Quad': {'Vertex': {'row': 8, 'col': 8}, 'Values': [0]}}),
        ]

        self.invalid_inputs: list[str] = [
            # Invalid input_types that should raise ParserError
            "123=456",  # More than two digits on the left
            "12=4a",  # Non-digit character on the right
            "1=23",  # Less than two digits on the left
            "12=",  # No right side
            "=45",  # No left side
            "12=4 5",  # Invalid due to space on the right side
            "12=??=10",  # Multiple '=' signs
            "value2=5",  # Non-digit character on the left
            "11=  ",  # Right side contains only spaces
            " 12=12",  # Leading space on left side
            "22 = 22",  # Spaces around the equals sign
            "12= ",  # Right side is empty after '='
            "12==123",  # Invalid due to double equals
            "22=12345",
        ]


if __name__ == "__main__":
    unittest.main()
