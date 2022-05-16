import unittest
from typing import Type

from src.items.between import Between
from src.items.cell import Cell
from src.items.composed import Composed
from src.items.item import Item
from src.items.line import Line
from src.items.region import Region
from tests.items.test_line import TestLine


class TestBetween(TestLine):

    @property
    def clazz(self):
        return Between

    @property
    def config(self) -> str:
        return "Between: 11, 12, 13"

    @property
    def has_rule(self) -> bool:
        return True

    @property
    def expected_classes(self) -> set[Type[Item]]:
        return {Between, Cell, Composed, Item, Line, Region}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
