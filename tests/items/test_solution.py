from typing import Type

import oyaml as yaml

from src.items.board import Board
from src.items.cell import Cell
from src.items.cell_reference import CellReference
from src.items.composed_item import ComposedItem
from src.items.item import Item
from src.items.known_cell import KnownCell
from src.items.solution import Solution
from tests.items.test_composed import TestComposed


class TestSolution(TestComposed):

    def setUp(self) -> None:
        self.board = Board(9, 9, 3, 3, None, None, None, None)
        self.size = 81
        lines = [
            "123456789",
            "123456789",
            "123456789",
            "123456789",
            "123456789",
            "123456789",
            "123456789",
            "123456789",
            "123456789"
        ]

        self.item = Solution(self.board, lines)

    @property
    def clazz(self):
        return Solution

    @property
    def config(self) -> str:
        return (
            "Solution:\n"
            "  - 123456789\n"
            "  - 123456789\n"
            "  - 123456789\n"
            "  - 123456789\n"
            "  - 123456789\n"
            "  - 123456789\n"
            "  - 123456789\n"
            "  - 123456789\n"
            "  - 123456789\n"
        )

    @property
    def representation(self) -> str:
        return (
            "Solution(Board(9, 9, 3, 3, None, None, None, None), "
            "["
            "'123456789', "
            "'123456789', "
            "'123456789', "
            "'123456789', "
            "'123456789', "
            "'123456789', "
            "'123456789', "
            "'123456789', "
            "'123456789'"
            "]"
            ")"
        )

    @property
    def has_rule(self) -> bool:
        return False

    @property
    def expected_classes(self) -> set[Type[Item]]:
        return {Cell, CellReference, ComposedItem, Item, KnownCell, Solution}

    def test_to_dict(self) -> None:  # When changed to strict yaml, this will go
        config = yaml.load(self.config, Loader=yaml.SafeLoader)
        lines = [str(line) for line in config['Solution']]
        config = {'Solution': lines}
        item = Item.create(self.board, config)
        self.assertDictEqual(item.to_dict(), config)
