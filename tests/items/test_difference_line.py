import unittest
from typing import Type

from src.items.cell import Cell
from src.items.composed_item import ComposedItem
from src.items.difference_line import DifferenceLine
from src.items.item import Item
from src.items.line import Line
from src.items.region import Region
from tests.items.test_line import TestLine


class TestDifferenceLine(TestLine):

    @property
    def clazz(self):
        return DifferenceLine

    @property
    def config(self) -> str:
        return "DifferenceLine: 11, 12, 13"

    @property
    def expected_classes(self) -> set[Type[Item]]:
        return {Cell, ComposedItem, DifferenceLine, Item, Line, Region}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
