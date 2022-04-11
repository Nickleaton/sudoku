import unittest
from typing import Type

from src.items.arrow import Arrow
from src.items.cell import Cell
from src.items.composed import Composed
from src.items.item import Item
from src.items.line import Line
from src.items.region import Region
from tests.items.test_line import TestLine


class TestArrow(TestLine):

    @property
    def clazz(self):
        return Arrow

    @property
    def has_rule(self) -> bool:
        return True

    @property
    def expected_classes(self) -> set[Type[Item]]:
        return {Arrow, Cell, Composed, Item, Line, Region}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
