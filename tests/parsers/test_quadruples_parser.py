import unittest
from typing import List, Tuple, Any

from src.parsers.quadruples_parser import QuadruplesParser
from tests.parsers.test_parser import TestParser


class TestQuadruplesParser(TestParser):
    """Test case for the QuadruplesParser class."""

    def setUp(self):
        """Sets up the QuadruplesParser instance for testing."""
        self.parser = QuadruplesParser()
        self.valid_input: List[Tuple[str, Any]] = [
            # Valid quadruples format inputs
            ("12=123", [12, '123']),
            ("01=456", [1, '456']),
            ("99=???", [99, '???']),
            ("30=10", [30, '10']),
            ("15=??", [15, '??']),
            ("23=2", [23, '2']),
            ("88=0", [88, '0']),
            ("77=??5", [77, '??5']),
            ("22=12345", [22, '12345']),  # Longer right side is valid
        ]

        self.invalid_input: List[str] = [
            # Invalid inputs that should raise ParserError
            "123=456",  # More than two digits on the left
            "12=4a",  # Non-digit character on the right
            "1=23",  # Less than two digits on the left
            "12=",  # No right side
            "=45",  # No left side
            "12=4 5",  # Invalid due to space on the right side
            "12=??=10",  # Multiple '=' signs
            "x2=5",  # Non-digit character on the left
            "11=  ",  # Right side contains only spaces
            " 12=12",  # Leading space on left side
            "22 = 22",  # Spaces around the equals sign
            "12= ",  # Right side is empty after '='
            "12==123",  # Invalid due to double equals
        ]


if __name__ == "__main__":
    unittest.main()
