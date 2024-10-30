import unittest
from typing import List, Tuple, Any

from src.parsers.parser import ParserError
from src.parsers.solution_parser import SolutionParser
from tests.parsers.test_parser import TestParser


class TestSolutionParser(TestParser):
    """Test case for the SolutionParser class."""

    def setUp(self):
        """Sets up the SolutionParser instance for testing."""
        self.parser: SolutionParser = SolutionParser()
        self.representation: str = 'SolutionParser()'
        self.valid_input_result: List[Tuple[str, Any]] = [
            ("123456789", ['1', '2', '3', '4', '5', '6', '7', '8', '9']),
            ("111111111", ['1', '1', '1', '1', '1', '1', '1', '1', '1']),
            ("987654321", ['9', '8', '7', '6', '5', '4', '3', '2', '1']),
            ("000000000", ['0', '0', '0', '0', '0', '0', '0', '0', '0']),
        ]
        self.valid_input_answer: List[Tuple[str, Any]] = [
            ("123456789", ['1', '2', '3', '4', '5', '6', '7', '8', '9']),
            ("111111111", ['1', '1', '1', '1', '1', '1', '1', '1', '1']),
            ("987654321", ['9', '8', '7', '6', '5', '4', '3', '2', '1']),
            ("000000000", ['0', '0', '0', '0', '0', '0', '0', '0', '0']),
        ]
        self.invalid_input: List[str] = [
            "12345678a",  # contains a non-numeric character
            "123 45678",  # contains whitespace
            "12345678#",  # contains a special character
        ]

    def test_parse_valid_input(self):
        """Tests parsing of valid inputs."""
        for text, expected in self.valid_input_result:
            with self.subTest(text=text):
                self.parser.parse(text)
                self.assertEqual(self.parser.result, expected)

    def test_parse_valid_answer(self):
        """Tests parsing of valid inputs."""
        for text, expected in self.valid_input_answer:
            with self.subTest(text=text):
                self.parser.parse(text)
                self.assertEqual(self.parser.answer, expected)

    def test_parse_invalid_input(self):
        """Tests that invalid inputs raise ParserError."""
        for text in self.invalid_input:
            with self.subTest(text=text):
                with self.assertRaises(ParserError):
                    self.parser.parse(text)


if __name__ == "__main__":
    unittest.main()
