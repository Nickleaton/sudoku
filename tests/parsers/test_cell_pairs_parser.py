"""TestCellPairsParser."""
import unittest
from typing import List, Tuple, Any

from src.parsers.cell_pairs_parser import CellPairsParser
from tests.parsers.test_parser import TestParser


class TestCellPairsParser(TestParser):
    """Test case for the CellPairParser class."""

    def setUp(self):
        """Set up the CellPairParser instance for testing."""
        self.parser: CellPairsParser = CellPairsParser()
        self.representation: str = 'CellPairsParser()'
        self.example_format: str = 'r1c1=r2c2'
        self.valid_input_result: List[Tuple[str, Any]] = \
            [
                (
                    "51-61",
                    [5, 1, 6, 1]
                ),
                (
                    "12-34",
                    [1, 2, 3, 4]
                ),
                (
                    "31-32",
                    [3, 1, 3, 2]
                ),
                (
                    " 12 - 34 ",
                    [1, 2, 3, 4]
                ),  # whitespace around '-'
                (
                    "12-34",
                    [1, 2, 3, 4]
                ),  # no spaces
                (
                    " 12- 34 ",
                    [1, 2, 3, 4]
                ),  # mixed spaces
            ]
        self.valid_input_answer = \
            [
                (
                    '51-61',
                    {'cell1': {'row': 5, 'column': 1}, 'cell2': {'row': 6, 'column': 1}}
                ),
                (
                    '12-34',
                    {'cell1': {'row': 1, 'column': 2}, 'cell2': {'row': 3, 'column': 4}}
                ),
                (
                    '31-32',
                    {'cell1': {'row': 3, 'column': 1}, 'cell2': {'row': 3, 'column': 2}}
                ),
                (
                    ' 12 - 34 ',
                    {'cell1': {'row': 1, 'column': 2}, 'cell2': {'row': 3, 'column': 4}}
                ),  # whitespace around '-'
                (
                    '12-34',
                    {'cell1': {'row': 1, 'column': 2}, 'cell2': {'row': 3, 'column': 4}}
                ),  # no spaces
                (
                    ' 12- 34 ',
                    {'cell1': {'row': 1, 'column': 2}, 'cell2': {'row': 3, 'column': 4}}
                ),  # mixed spaces
            ]
        self.invalid_input: List[str] = \
            [
                # Invalid input_types that should raise ParserError
                "123x56789",  # invalid due to non-digit character
                "12-34-56",  # invalid due to extra '-'
                "12,34,5x",  # invalid due to non-digit character
                "12-34,56",  # invalid format, should only have one '-'
                "12-34,",  # invalid due to empty second coordinate
                "-34",  # invalid due to missing first coordinate
                "12-34, ",  # trailing space after valid input should fail
                "  -34",  # invalid due to missing first coordinate

            ]


if __name__ == "__main__":
    unittest.main()
