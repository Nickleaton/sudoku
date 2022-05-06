import unittest
from typing import Type

from src.items.cell import Cell
from src.items.composed import Composed
from src.items.difference_pair import DifferencePair
from src.items.item import Item
from src.items.less_than_equal_difference_line import LessThanEqualDifferenceLine
from src.items.less_than_equal_difference_pair import LessThanEqualDifferencePair
from src.items.line import Line
from src.items.pair import Pair
from src.items.region import Region
from tests.items.test_line import TestLine


class TestLessThanEqualDifferenceLine(TestLine):

    @property
    def clazz(self):
        return LessThanEqualDifferenceLine

    @property
    def config(self) -> str:
        return f"LessThanEqualDifferenceLine: 11, 12, 13"

    @property
    def has_rule(self) -> bool:
        return True

    @property
    def representation(self) -> str:
        return (
            f"{self.clazz.__name__}"
            f"("
            f"Board(9, 9, 3, 3, None, None, None, None), "
            f"["
            f"Cell(Board(9, 9, 3, 3, None, None, None, None), 1, 1), "
            f"Cell(Board(9, 9, 3, 3, None, None, None, None), 1, 2), "
            f"Cell(Board(9, 9, 3, 3, None, None, None, None), 1, 3)"
            f"]"
            f")"
        )

    @property
    def expected_classes(self) -> set[Type[Item]]:
        return {Cell, Composed, LessThanEqualDifferenceLine, DifferencePair, Item, LessThanEqualDifferencePair, Line,
                Pair, Region}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
