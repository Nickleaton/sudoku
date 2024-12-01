"""TestParser."""
import re
import unittest
from typing import Any, Tuple, List

from src.parsers.mock_parser import MockParser
from src.parsers.parser import ParserError, Parser


class TestParser(unittest.TestCase):
    """Test case for the Parser abstract base class."""

    def setUp(self):
        """Set up the MockParser instance for testing."""
        self.parser: Parser = MockParser()  # Instantiate the MockParser
        self.valid_input_result: List[Tuple[str, Any]] = []
        self.valid_input_answer: List[Tuple[str, Any]] = []
        self.invalid_input: List[str] = []
        self.representation = 'MockParser()'
        self.example_format: str | None = ""

    def test_register(self):
        """Test the parser is registered in the Parser register."""
        self.assertIn(self.parser.__class__.__name__, Parser.classes)
        self.assertEqual(Parser.classes[self.parser.__class__.__name__], self.parser.__class__)

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
        """Tests parsing invalid input_types raises ParserError."""
        for input_text in self.invalid_input:
            with self.assertRaises(ParserError) as _:
                self.parser.parse(input_text)
            self.assertIsNone(self.parser.result)

    def test_repr(self):
        """Tests the __repr__ method."""
        self.assertEqual(repr(self.parser), self.representation)

    def test_valid_answer(self):
        """Text Valid Answers from the given list."""
        for text, output in self.valid_input_answer:
            self.parser.parse(text)
            self.assertEqual(self.parser.answer, output)

    def test_example_format(self):
        """Text example format works."""
        self.assertEqual(self.parser.example_format, self.example_format)

    def test_help(self):
        """Test here is help for the parser."""
        self.assertIsNotNone(self.parser.help())

    def test_raise_error(self):
        """Test error cases."""
        with self.assertRaises(ParserError):
            self.parser.raise_error()
        self.parser.result = 'xxx'
        self.parser.answer = 'xxx'
        try:
            self.parser.raise_error()
        except ParserError as e:
            self.assertIsNone(self.parser.result)
            self.assertIsNone(self.parser.answer)
            self.assertEqual(
                str(e),
                f"{self.parser.__class__.__name__} expects valid input in the format '{self.parser.example_format}'."
            )

    def test_token(self):
        """Test Token is available."""
        self.assertIsNotNone(self.parser.token)


if __name__ == '__main__':  # pragma: no cover
    unittest.main()

