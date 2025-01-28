"""TestClonedRegion."""
import unittest
from typing import Type

from postponed.src.items.cloned_region import ClonedRegion
from src.items.cell import Cell
from src.items.item import Item
from tests.items.test_item import TestItem


class TestClonedRegion(TestItem):
    """Test suite for the ClonedRegion constraint in the Board."""

    def setUp(self) -> None:
        """Set up the Board and ClonedRegion instance for testing."""
        super().setUp()
        self.cells_1 = [Cell(self.board, 1, 1), Cell(self.board, 1, 2), Cell(self.board, 1, 3)]
        self.cells_2 = [Cell(self.board, 9, 9), Cell(self.board, 9, 8), Cell(self.board, 9, 7)]
        self.item = ClonedRegion(self.board, self.cells_1, self.cells_2)

    @property
    def clazz(self):
        """Return the ClonedRegion class."""
        return ClonedRegion

    @property
    def representation(self) -> str:
        """Return the string representation for the ClonedRegion constraint."""
        return (
            "ClonedRegion(Board(9, 9, {}), "
            "[Cell(Board(9, 9, {}), 1, 1), "
            "Cell(Board(9, 9, {}), 1, 2), "
            "Cell(Board(9, 9, {}), 1, 3)], "
            "[Cell(Board(9, 9, {}), 9, 9), "
            "Cell(Board(9, 9, {}), 9, 8), "
            "Cell(Board(9, 9, {}), 9, 7)]"
            ")"
        )

    @property
    def expected_classes(self) -> set[Type[Item]]:
        """Return the expected classes that the ClonedRegion constraint should belong to."""
        return {Cell, Item, ClonedRegion}

    @property
    def config(self) -> str:
        """Return the configuration string for the ClonedRegion constraint."""
        return "ClonedRegion: 11,12,13=99,98,97"

    @property
    def has_rule(self) -> bool:
        """Indicates if the ClonedRegion has start_location rule."""
        return True

    @property
    def inside(self) -> Cell:
        """Return start_location Cell that is inside the ClonedRegion."""
        return Cell.make(self.board, 1, 2)


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
