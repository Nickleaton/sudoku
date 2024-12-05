"""TestCellPairEqualValueParser."""
import unittest
from typing import List, Tuple, Any
from src.parsers.cell_pair_equal_value_parser import CellPairEqualValueParser
from src.parsers.parser import ParserError
from tests.parsers.test_parser import TestParser


class TestCellPairEqualValueParser(TestParser):
    """Test case for the CellPairEqualValueParser class."""

    def setUp(self):
        """Set up the CellPairEqualValueParser instance for testing."""
        self.parser: CellPairEqualValueParser = CellPairEqualValueParser()
        self.representation: str = 'CellPairEqualValueParser()'
        self.example_format: str = 'r1c1-r2c2=dd'
        self.valid_input_result: List[Tuple[str, Any]] = \
            [
                (
                    "51-61=5",
                    [5, 1, 6, 1, 5]
                ),
                (
                    "12-34=10",
                    [1, 2, 3, 4, 10]
                ),
                (
                    "31-32=7",
                    [3, 1, 3, 2, 7]
                ),
                (
                    " 12 - 34 = 15 ",
                    [1, 2, 3, 4, 15]
                ),  # whitespace around '='
                (
                    "12-34=5",
                    [1, 2, 3, 4, 5]
                ),  # no spaces
                (
                    " 12- 34 = 20 ",
                    [1, 2, 3, 4, 20]
                ),  # mixed spaces
            ]
        self.valid_input_answer = \
            [
                (
                    "51-61=5",
                    {"row1": '5', "column1": '1', "row2": '6', "column2": '1', "value": '5'}
                ),
                (
                    "12-34=10",
                    {"row1": '1', "column1": '2', "row2": '3', "column2": '4', "value": '10'}
                ),
                (
                    "31-32=7",
                    {"row1": '3', "column1": '1', "row2": '3', "column2": '2', "value": '7'}
                ),
                (
                    " 12 - 34 = 15 ",
                    {"row1": '1', "column1": '2', "row2": '3', "column2": '4', "value": '15'}
                ),  # whitespace around '='
                (
                    "12-34=5",
                    {"row1": '1', "column1": '2', "row2": '3', "column2": '4', "value": '5'}
                ),  # no spaces
                (
                    " 12- 34 = 20 ",
                    {"row1": '1', "column1": '2', "row2": '3', "column2": '4', "value": '20'}
                ),  # mixed spaces
            ]
        self.invalid_input: List[str] = \
            [
                # Invalid input_types that should raise ParserError
                "123x56789=5",  # invalid due to non-digit character
                "12-34-56=5",  # invalid due to extra '-'
                "12,34,5x=5",  # invalid due to non-digit character
                "12-34,56=5",  # invalid format, should only have one '-'
                "12-34,=5",  # invalid due to empty second coordinate
                "-34=5",  # invalid due to missing first coordinate
                "12-34, =5",  # trailing space after valid input should fail
                "  -34=5",  # invalid due to missing first coordinate
                "12-34=5x",  # invalid due to non-digit character in value
            ]

    def test_parse_valid_input(self):
        """Test parsing valid input strings."""
        for input_str, expected_result in self.valid_input_result:
            with self.subTest(input_str=input_str):
                self.parser.parse(input_str)
                self.assertEqual(self.parser.result, expected_result)

    def test_answer_valid_input(self):
        """Test generating the expected data from valid input."""
        for input_str, expected_answer in self.valid_input_answer:
            with self.subTest(input_str=input_str):
                self.parser.parse(input_str)
                self.assertEqual(self.parser.answer, expected_answer)

    def test_parse_invalid_input(self):
        """Test handling invalid input strings."""
        for input_str in self.invalid_input:
            with self.subTest(input_str=input_str):
                with self.assertRaises(ParserError):
                    self.parser.parse(input_str)

if __name__ == "__main__":
    unittest.main()

