"""TestQuadruplesParser."""
import unittest
from typing import List, Tuple, Any

from src.parsers.quadruples_parser import QuadruplesParser
from tests.parsers.test_parser import TestParser


class TestQuadruplesParser(TestParser):
    """Test case for the QuadruplesParser class."""

    def setUp(self):
        """Set up the QuadruplesParser instance for testing."""
        self.parser: QuadruplesParser = QuadruplesParser()
        self.representation: str = "QuadruplesParser()"
        self.example_format: str = 'rc=dd??'
        self.valid_input_result: List[Tuple[str, Any]] = [
            # Valid quadruples format input_types
            (
                "12=123",
                [1, 2, '123']
            ),
            (
                "01=456",
                [0, 1, '456']
            ),
            (
                "99=???",
                [9, 9, '???']
            ),
            (
                "30=10",
                [3, 0, '10']
            ),
            (
                "15=??",
                [1, 5, '??']
            ),
            (
                "23=2",
                [2, 3, '2']
            ),
            (
                "88=0",
                [8, 8, '0']
            ),
            (
                "77=??5",
                [7, 7, '??5']
            ),
            (
                "22=12345",
                [2, 2, '12345']
            ),  # Longer right side is valid
        ]
        self.valid_input_answer: List[Tuple[str, Any]] = [
            # Valid quadruples format input_types
            (
                "12=123",
                {'row': '1', 'column': '2', 'values': ['1', '2', '3']}
            ),
            (
                "01=456",
                {'row': '0', 'column': '1', 'values': ['4', '5', '6']}
            ),
            (
                "99=???",
                {'row': '9', 'column': '9', 'values': ['?', '?', '?']}
            ),
            (
                "30=10",
                {'row': '3', 'column': '0', 'values': ['1', '0']}
            ),
            (
                "15=??",
                {'row': '1', 'column': '5', 'values': ['?', '?']}
            ),
            (
                "23=2",
                {'row': '2', 'column': '3', 'values': ['2']}
            ),
            (
                "88=0",
                {'row': '8', 'column': '8', 'values': ['0']}
            ),
            (
                "77=??5",
                {'row': '7', 'column': '7', 'values': ['?', '?', '5']}
            ),
            (
                "22=12345",
                {'row': '2', 'column': '2', 'values': ['1', '2', '3', '4', '5']}
            ),  # Longer right side is valid
        ]

        self.invalid_input: List[str] = [
            # Invalid input_types that should raise ParserError
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

