"""TestKnownCell."""
import unittest
from typing import Type

from src.items.board import Board
from src.items.cell import Cell
from src.items.cell_reference import CellReference
from src.items.item import Item
from src.items.known_cell import KnownCell
from tests.items.test_cell_reference import TestCellReference


class TestKnownCell(TestCellReference):
    """Test suite for the KnownCell class, inheriting from TestCellReference."""

    def setUp(self) -> None:
        """Set up the test case with a board and a KnownCell instance."""
        super().setUp()
        self.item = KnownCell(self.board, 1, 2, 9)

    @property
    def clazz(self):
        """Return the KnownCell class."""
        return KnownCell

    @property
    def representation(self) -> str:
        """Return a string representation of the KnownCell instance."""
        return ("KnownCell("
                "Board(9, 9, 3, 3, None, None, None, None), "
                "Cell(Board(9, 9, 3, 3, None, None, None, None), 1, 2), "
                "9"
                ")"
                )

    @property
    def config(self) -> str:
        """Return the configuration string for KnownCell."""
        return "KnownCell: 12=9"

    @property
    def has_rule(self) -> bool:
        """Return whether the KnownCell instance has a rule."""
        return False

    @property
    def expected_classes(self) -> set[Type[Item]]:
        """Return the expected classes that the KnownCell instance should belong to."""
        return {Cell, CellReference, Item, KnownCell}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
