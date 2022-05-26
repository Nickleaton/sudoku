import unittest
from typing import Type

from src.items.cell import Cell
from src.items.composed_item import ComposedItem
from src.items.item import Item
from src.items.line import Line
from src.items.max_arrow import MaxArrow
from src.items.region import Region
from tests.items.test_line import TestLine


class TestMaxArrow(TestLine):

    @property
    def clazz(self):
        return MaxArrow

    @property
    def config(self) -> str:
        return "MaxArrow: 11, 12, 13"

    @property
    def has_rule(self) -> bool:
        return True

    @property
    def expected_classes(self) -> set[Type[Item]]:
        return {MaxArrow, Cell, ComposedItem, Item, Line, Region}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
