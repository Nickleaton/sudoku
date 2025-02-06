"""TestCelllistParser."""
import unittest
from typing import Any

from src.parsers.cell_list_parser import CelllistParser
from tests.parsers.test_parser import TestParser


class TestCelllistParser(TestParser):
    """Test case for the CelllistParser class."""

    def setUp(self):
        """Set up the CelllistParser instance for testing."""
        super().setUp()
        self.parser: CelllistParser = CelllistParser()
        self.representation: str = 'CelllistParser()'
        self.empty_allowed: bool = False
        self.valid_inputs: list[tuple[str, Any]] = \
            [
                (
                    "12",
                    {
                        'Celllist': [
                            {'Cell': {'row': 1, 'col': 2}}
                        ]
                    }
                ),
                (
                    "12,34,56",
                    {
                        'Celllist': [
                            {'Cell': {'row': 1, 'col': 2}},
                            {'Cell': {'row': 3, 'col': 4}},
                            {'Cell': {'row': 5, 'col': 6}}
                        ]
                    }
                ),
                (
                    "01,02,03",
                    {
                        'Celllist': [
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
