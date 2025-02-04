"""TestParser."""
import unittest
from typing import Any

from src.parsers.none_parser import NoneParser
from src.parsers.parser import Parser
from src.utils.sudoku_exception import SudokuError


class TestParser(unittest.TestCase):
    """Base test case for parser classes."""

    def setUp(self):
        """Set up the NoneParser instance for testing."""
        super().setUp()
        self.parser: Parser = NoneParser()
        self.valid_inputs: list[tuple[str, Any]] = []
        self.invalid_inputs: list[str] = []
        self.representation: str = 'NoneParser()'
        self.empty_allowed: bool = True

    def test_register(self):
        """Test the parser is registered in the Parser register."""
        self.assertIn(self.parser.__class__.__name__, Parser.classes)
        self.assertEqual(Parser.classes[self.parser.__class__.__name__], self.parser.__class__)

    def test_representation(self) -> None:
        """Test the string representation of the parser."""

        self.assertEqual(repr(self.parser), self.representation)

    def test_parse_empty_input(self):
        """Tests parsing an empty input string."""
        if self.empty_allowed:
            self.assertEqual({}, self.parser.parse(''))
        else:
            with self.assertRaises(SudokuError):
                _ = self.parser.parse('')

    def test_valid_inputs(self) -> None:
        """Test that valid inputs are parsed correctly."""
        for text, expected in self.valid_inputs:
            with self.subTest(text=text):
                self.assertEqual(expected, self.parser.parse(text))

    def test_invalid_inputs(self) -> None:
        """Test that invalid inputs raise an exception."""
        for text in self.invalid_inputs:
            with self.subTest(text=text):
                print()
                print("Invalid input:", text)
                print()
                with self.assertRaises(SudokuError):
                    _ = self.parser.parse(text)

    def test_help(self):
        """Test here is help for the parser."""
        self.assertIsNotNone(self.parser.help())

    def test_token(self):
        """Test Token is available."""
        self.assertIsNotNone(self.parser.token)


if __name__ == "__main__":
    unittest.main()
