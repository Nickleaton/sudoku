import unittest
from typing import List, Tuple, Any

from src.parsers.cell_list_parser import CellListParser
from tests.parsers.test_parser import TestParser


class TestCellListParser(TestParser):
    """Test case for the CellListParser class."""

    def setUp(self):
        """Sets up the CellListParser instance for testing."""
        self.parser: CellListParser = CellListParser()
        self.representation: str = 'CellListParser()'
        self.valid_input: List[Tuple[str, Any]] = \
            [
                ("12", [[1, 2]]),
                ("12,34,56", [[1, 2], [3, 4], [5, 6]]),
                (" 12 , 34 , 56 ", [[1, 2], [3, 4], [5, 6]]),
                ("12,34,56", [[1, 2], [3, 4], [5, 6]]),
                ("   12  , 34  ,  56   ", [[1, 2], [3, 4], [5, 6]]),
                ("01,02,03", [[0, 1], [0, 2], [0, 3]]),
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
