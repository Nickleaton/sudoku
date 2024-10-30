import re
import unittest
from typing import Any, Tuple, List

from src.parsers.mock_parser import MockParser
from src.parsers.parser import ParserError, Parser


class TestParser(unittest.TestCase):
    """Test case for the Parser abstract base class."""

    def setUp(self):
        """Sets up the MockParser instance for testing."""
        self.parser: Parser = MockParser()  # Instantiate the MockParser
        self.valid_input_result: List[Tuple[str, Any]] = []
        self.valid_input_answer: List[Tuple[str, Any]] = []
        self.invalid_input: List[str] = []
        self.representation = 'MockParser()'

    def test_parse_empty_input(self):
        """Tests parsing an empty input string."""
        input_text = ""
        with self.assertRaises(ParserError):
            self.parser.parse(input_text)

    def test_regular_expression_attribute(self):
        """Tests that the regular_expression attribute is correctly compiled."""
        self.assertIsInstance(self.parser.regular_expression, re.Pattern)

    def test_parse_valid_input_result(self):
        """Tests parsing a valid comma-separated list of digits."""
        for text, output in self.valid_input_result:
            self.parser.parse(text)
            self.assertEqual(self.parser.result, output)

    def test_invalid_input(self):
        """Tests parsing invalid inputs raises ParserError."""
        for input_text in self.invalid_input:
            with self.assertRaises(ParserError) as _:
                self.parser.parse(input_text)
            self.assertIsNone(self.parser.result)

    def test_repr(self):
        """Tests the __repr__ method."""
        self.assertEqual(repr(self.parser), self.representation)

    def test_valid_answer(self):
        for text, output in self.valid_input_answer:
            self.parser.parse(text)
            self.assertEqual(self.parser.answer, output)


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
