"""TestCellListParser."""
import unittest
from typing import List, Tuple, Any

from src.parsers.cell_list_parser import CellListParser
from tests.parsers.test_parser import TestParser


class TestCellListParser(TestParser):
    """Test case for the CellListParser class."""

    def setUp(self):
        """Set up the CellListParser instance for testing."""
        self.parser: CellListParser = CellListParser()
        self.representation: str = 'CellListParser()'
        self.example_format: str = 'rc,rc,...'
        self.valid_input_result: List[Tuple[str, Any]] = \
            [
                (
                    "12",
                    [[1, 2]]
                ),
                (
                    "12,34,56",
                    [[1, 2], [3, 4], [5, 6]]
                ),
                (
                    " 12 , 34 , 56 ",
                    [[1, 2], [3, 4], [5, 6]]
                ),
                (
                    "12,34,56",
                    [[1, 2], [3, 4], [5, 6]]
                ),
                (
                    "   12  , 34  ,  56   ",
                    [[1, 2], [3, 4], [5, 6]]
                ),
                (
                    "01,02,03",
                    [[0, 1], [0, 2], [0, 3]]
                ),
            ]
        self.valid_input_answer: List[Tuple[str, Any]] = \
            [
                (
                    "12",
                    [{'row': '1', 'column': '2'}]
                ),
                (
                    "12,34,56",
                    [{'row': '1', 'column': '2'}, {'row': '3', 'column': '4'}, {'row': '5', 'column': '6'}]
                ),
                (
                    " 12 , 34 , 56 ",
                    [{'row': '1', 'column': '2'}, {'row': '3', 'column': '4'}, {'row': '5', 'column': '6'}]
                ),
                (
                    "12,34,56",
                    [{'row': '1', 'column': '2'}, {'row': '3', 'column': '4'}, {'row': '5', 'column': '6'}]
                ),
                (
                    "   12  , 34  ,  56   ",
                    [{'row': '1', 'column': '2'}, {'row': '3', 'column': '4'}, {'row': '5', 'column': '6'}]
                ),
                (
                    "01,02,03",
                    [{'row': '0', 'column': '1'}, {'row': '0', 'column': '2'}, {'row': '0', 'column': '3'}]
                ),
            ]
        self.invalid_input: List[str] = \
            [
                "123x56789",
                "123,56789",
                "12,34,5x",  # invalid due to non-digit character
                "12,34,,56",  # invalid due to empty coordinate
            ]


if __name__ == "__main__":
    unittest.main()
