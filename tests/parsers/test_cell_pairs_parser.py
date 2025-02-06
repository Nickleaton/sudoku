"""TestCellPairsParser."""
import unittest

from src.parsers.cell_pairs_parser import CellPairsParser
from tests.parsers.test_parser import TestParser


class TestCellPairsParser(TestParser):
    """Test case for the CellPairParser class."""

    def setUp(self):
        """Set up the CellPairParser instance for testing."""
        super().setUp()
        self.parser: CellPairsParser = CellPairsParser()
        self.representation: str = 'CellPairsParser()'
        self.empty_allowed = False
        self.valid_inputs: list[tuple[str, dict[str, dict[str, dict[str, int] | int]]]] = [
            ('51-61', {'CellPair': {'Cell1': {'row': 5, 'col': 1}, 'Cell2': {'row': 6, 'col': 1}}}),
            ('12-34', {'CellPair': {'Cell1': {'row': 1, 'col': 2}, 'Cell2': {'row': 3, 'col': 4}}}),
            ('31-32', {'CellPair': {'Cell1': {'row': 3, 'col': 1}, 'Cell2': {'row': 3, 'col': 2}}}),
            ('12-34', {'CellPair': {'Cell1': {'row': 1, 'col': 2}, 'Cell2': {'row': 3, 'col': 4}}}),
        ]

        self.invalid_inputs: list[str] = \
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
