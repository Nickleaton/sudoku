import unittest
from typing import List, Tuple, Any

from src.parsers.cell_pairs_parser import CellPairsParser
from tests.parsers.test_parser import TestParser


class TestCellPairsParser(TestParser):
    """Test case for the CellPairParser class."""

    def setUp(self):
        """Sets up the CellPairParser instance for testing."""
        self.parser: CellPairsParser = CellPairsParser()
        self.representation: str = 'CellPairsParser()'

        self.valid_input: List[Tuple[str, Any]] = \
            [
                ("12=34", [[1, 2], [3, 4]]),
                ("31=32", [[3, 1], [3, 2]]),
                (" 12 = 34 ", [[1, 2], [3, 4]]),  # whitespace around '='
                ("12=34", [[1, 2], [3, 4]]),  # no spaces
                (" 12= 34 ", [[1, 2], [3, 4]]),  # mixed spaces
            ]
        self.invalid_input: List[str] = \
            [
                # Invalid inputs that should raise ParserError
                "123x56789",  # invalid due to non-digit character
                "12=34=56",  # invalid due to extra '='
                "12,34,5x",  # invalid due to non-digit character
                "12=34,56",  # invalid format, should only have one '='
                "12=34,",  # invalid due to empty second coordinate
                "=34",  # invalid due to missing first coordinate
                "12=34, ",  # trailing space after valid input should fail
                "  =34",  # invalid due to missing first coordinate
            ]


if __name__ == "__main__":
    unittest.main()
