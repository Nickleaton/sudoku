"""TestCellListParser."""
import unittest
from typing import Any

from src.parsers.cell_list_parser import CellListParser
from tests.parsers.test_parser import TestParser


class TestCellListParser(TestParser):
    """Test case for the CellListParser class."""

    def setUp(self):
        """Set up the CellListParser instance for testing."""
        super().setUp()
        self.parser: CellListParser = CellListParser()
        self.representation: str = 'CellListParser()'
        self.empty_allowed = False
        self.valid_inputs: list[Tuple[str, Any]] = \
            [
                (
                    "12",
                    {
                        'CellList': [
                            {'Cell': {'row': 1, 'col': 2}}
                        ]
                    }
                ),
                (
                    "12,34,56",
                    {
                        'CellList': [
                            {'Cell': {'row': 1, 'col': 2}},
                            {'Cell': {'row': 3, 'col': 4}},
                            {'Cell': {'row': 5, 'col': 6}}
                        ]
                    }
                ),
                (
                    "01,02,03",
                    {
                        'CellList': [
                            {'Cell': {'row': 0, 'col': 1}},
                            {'Cell': {'row': 0, 'col': 2}},
                            {'Cell': {'row': 0, 'col': 3}}
                        ]
                    }
                )
            ]
        self.invalid_inputs: list[str] = \
            [
                "123,56789",
                "12,34,5x",  # invalid due to non-digit character
                "12,34,,56",  # invalid due to empty coordinate
            ]


if __name__ == "__main__":
    unittest.main()
