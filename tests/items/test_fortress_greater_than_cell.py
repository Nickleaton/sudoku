"""TestFortressGreaterThanCell."""
import unittest

from src.items.cell import Cell
from src.items.cell_reference import CellReference
from src.items.fortress_cell import FortressCell
from src.items.fortress_greater_than_cell import FortressGreaterThanCell
from src.items.item import Item
from src.items.simple_cell_reference import SimpleCellReference
from tests.items.test_fortress_cell import TestFortressCell


class TestFortressGreaterThanCell(TestFortressCell):
    """Test suite for the FortressCell class."""

    def setUp(self) -> None:
        """Set up the test environment by creating a board and initializing the FortressGreaterThanCell constraint."""
        super().setUp()
        self.item = FortressGreaterThanCell(self.board, 1, 2)
        self.letter = 'f'

    @property
    def clazz(self):
        """Return the FortressCell class."""
        return FortressGreaterThanCell

    @property
    def representation(self) -> str:
        """Return a string representation of the FortressGreaterThanCell instance."""
        return (
            "FortressGreaterThanCell("
            "Board(Coord(9, 9), Digits(1, 9), Tags({})), "
            "Cell(Board(Coord(9, 9), Digits(1, 9), Tags({})), "
            "1, "
            "2"
            ")"
            ")"
        )

    @property
    def config(self) -> str:
        """Return the configuration string for the FortressGreaterThanCell."""
        return "FortressGreaterThanCell: 12"

    @property
    def has_rule(self) -> bool:
        """Return True to indicate the rule is present for the FortressGreaterThanCell."""
        return True

    @property
    def expected_classes(self) -> set[type[Item]]:
        """Return the expected classes that the FortressCell should belong to."""
        return {Cell, CellReference, SimpleCellReference, Item, FortressCell, FortressGreaterThanCell}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
