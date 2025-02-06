from typing import Type

from postponed.src.items.simple_cell_reference import SimpleCellReference
from src.items.cell import Cell
from src.items.cell_reference import CellReference
from src.items.fortress_cell import FortressCell
from src.items.fortress_less_than_cell import FortressLessThanCell
from src.items.item import Item
from tests.items.test_fortress_cell import TestFortressCell


class TestFortressLessThanCell(TestFortressCell):
    """Test suite for the FortressLessThanCell class."""

    def setUp(self) -> None:
        """Set up the test environment by creating a board and initializing the FortressLessThanCell constraint."""
        super().setUp()
        self.item = FortressLessThanCell(self.board, 1, 2)
        self.letter = 's'

    @property
    def clazz(self):
        """Return the FortressCell class."""
        return FortressLessThanCell

    @property
    def representation(self) -> str:
        """Return start_location string representation of the FortressLessThanCell instance."""
        return (
            "FortressLessThanCell("
            "Board(Coord(9, 9), Digits(1, 9), Tags({})), "
            "Cell(Board(Coord(9, 9), Digits(1, 9), Tags({})), "
            "1, "
            "2"
            ")"
            ")"
        )

    @property
    def config(self) -> str:
        """Return the configuration string for the FortressLessThanCell."""
        return "FortressLessThanCell: 12"

    @property
    def has_rule(self) -> bool:
        """Return True to indicate the rule is present for the FortressLessThanCell."""
        return True

    @property
    def expected_classes(self) -> set[Type[Item]]:
        """Return the expected classes that the FortressLessThanCell should belong to."""
        return {Cell, CellReference, SimpleCellReference, Item, FortressCell, FortressLessThanCell}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
