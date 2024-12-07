"""TestPencilMarkCell."""
import unittest
from typing import Type

from src.items.board import Board
from src.items.cell import Cell
from src.items.cell_reference import CellReference
from src.items.item import Item
from src.items.pencil_mark import PencilMarkCell
from tests.items.test_cell_reference import TestCellReference


class TestPencilMarkCell(TestCellReference):
    """Test suite for the PencilMarkCell class."""

    def setUp(self) -> None:
        """Set up a test instance of PencilMarkCell."""
        super().setUp()
        self.item = PencilMarkCell(self.board, 1, 2, [2, 4, 6, 8])

    @property
    def clazz(self):
        """Return the PencilMarkCell class."""
        return PencilMarkCell

    @property
    def representation(self) -> str:
        """Return the string representation of PencilMarkCell."""
        return (
            "PencilMarkCell(Board(9, 9, 3, 3, None, None, None, None), "
            "Cell(Board(9, 9, 3, 3, None, None, None, None), 1, 2), "
            "[2, 4, 6, 8]"
            ")"
        )

    @property
    def config(self) -> str:
        """Return the configuration string for PencilMarkCell."""
        return "PencilMarkCell: 12=2468"

    @property
    def has_rule(self) -> bool:
        """Return whether PencilMarkCell has an associated rule."""
        return True

    @property
    def expected_classes(self) -> set[Type[Item]]:
        """Return the expected classes that the PencilMarkCell instance should belong to."""
        return {Cell, CellReference, Item, PencilMarkCell}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
