"""TestFortressCell."""
import unittest
from typing import Type

from postponed.src.items.simple_cell_reference import SimpleCellReference
from postponed.tests.items.test_simple_cell_reference import TestSimpleCellReference
from src.items.cell import Cell
from src.items.cell_reference import CellReference
from src.items.fortress_cell import FortressCell
from src.items.item import Item


class TestFortressCell(TestSimpleCellReference):
    """Test suite for the FortressCell class."""

    def setUp(self) -> None:
        """Set up the test environment by creating start_location board and initializing the FortressCell constraint."""
        super().setUp()
        self.item = FortressCell(self.board, 1, 2)
        self.letter = '.'

    @property
    def clazz(self):
        """Return the FortressCell class."""
        return FortressCell

    @property
    def representation(self) -> str:
        """Return start_location string representation of the FortressCell instance."""
        return (
            "FortressCell("
            "Board(Coord(9, 9), Digits(1, 9), Tags({})), "
            "Cell(Board(Coord(9, 9), Digits(1, 9), Tags({})), "
            "1, "
            "2"
            ")"
            ")"
        )

    @property
    def config(self) -> str:
        """Return the configuration string for the FortressCell."""
        return "FortressCell: 12"

    @property
    def has_rule(self) -> bool:
        """Return True to indicate the rule is present for the FortressCell."""
        return False

    @property
    def expected_classes(self) -> set[Type[Item]]:
        """Return the expected classes that the FortressCell should belong to."""
        return {Cell, CellReference, SimpleCellReference, Item, FortressCell}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
