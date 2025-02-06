"""TestCellPairEqualValueParser."""
import unittest

from src.parsers.cell_pair_equal_value_parser import CellPairEqualValueParser
from tests.parsers.test_parser import TestParser


class TestCellPairEqualValueParser(TestParser):
    """Test case for the CellPairEqualValueParser class."""

    def setUp(self):
        """Set up the CellPairEqualValueParser instance for testing."""
        super().setUp()
        self.parser: CellPairEqualValueParser = CellPairEqualValueParser()
        self.representation: str = 'CellPairEqualValueParser()'
        self.empty_allowed: bool = False
        self.valid_inputs: list[tuple[str, dict[str, dict[str, dict[str, int] | int]]]] = [
            (
                '51-61=5',
                {
                    'CellPairValue': {
                        'Cell1': {'row': 5, 'col': 1},
                        'Cell2': {'row': 6, 'col': 1},
                        'Value': 5
                    }
                }
            ),
            (
                '12-34=10',
                {
                    'CellPairValue': {
                        'Cell1': {'row': 1, 'col': 2},
                        'Cell2': {'row': 3, 'col': 4},
                        'Value': 10
                    }
                }
            ),
            (
                '31-32=7',
                {
                    'CellPairValue': {
                        'Cell1': {'row': 3, 'col': 1},
                        'Cell2': {'row': 3, 'col': 2},
                        'Value': 7
                    }
                }
            ),
            (
                '12-34=5',
                {
                    'CellPairValue': {
                        'Cell1': {'row': 1, 'col': 2},
                        'Cell2': {'row': 3, 'col': 4},
                        'Value': 5
                    }
                }
            ),
        ]

        self.invalid_inputs: list[str] = \
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


if __name__ == "__main__":
    unittest.main()
