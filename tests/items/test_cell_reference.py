"""TestCellReference."""
import unittest
from typing import Type

from src.items.board import Board
from src.items.cell import Cell
from src.items.cell_reference import CellReference
from src.items.item import Item
from tests.items.test_item import TestItem


class TestCellReference(TestItem):
    """Test suite for the CellReference item in the Board."""

    def setUp(self) -> None:
        """Set up the Board and CellReference instance for testing."""
        super().setUp()
        self.item = CellReference(self.board, 1, 2)

    @property
    def clazz(self):
        """Return the CellReference class."""
        return CellReference

    @property
    def representation(self) -> str:
        """Return the string representation for the CellReference item."""
        return (
            "CellReference"
            "("
            "Board(9, 9, 3, 3, None, None, None, None), "
            "Cell(Board(9, 9, 3, 3, None, None, None, None), "
            "1, "
            "2"
            ")"
            ")"
        )

    @property
    def config(self) -> str:
        """Return the configuration string for the CellReference item."""
        return "CellReference: 12"

    @property
    def has_rule(self) -> bool:
        """Indicates if the CellReference has a rule."""
        return False

    @property
    def expected_classes(self) -> set[Type[Item]]:
        """Return the expected classes that the CellReference item should belong to."""
        return {Cell, CellReference, Item}

    def test_flatten(self) -> None:
        """Test the flatten method of the CellReference."""
        self.assertListEqual([self.item, self.item.cell], self.item.flatten())


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
