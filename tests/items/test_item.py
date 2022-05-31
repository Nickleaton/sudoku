import re
import unittest
from typing import Type

import oyaml as yaml

from src.items.board import Board
from src.items.item import Item
from src.solvers.pulp_solver import PulpSolver


class TestItem(unittest.TestCase):

    def setUp(self) -> None:
        self.board = Board(9, 9, 3, 3, None, None, None, None)
        self.item = Item(self.board)

    @property
    def clazz(self):
        return Item

    def test_clazz(self):
        self.assertEqual(self.item.__class__, self.clazz)

    def test_top(self):
        self.assertEqual(self.item.top, self.item)

    @property
    def config(self) -> str:
        return "Item:"

    def test_create(self) -> None:
        if self.item.__class__.__name__ == 'Item':
            return
        config = yaml.load(self.config, Loader=yaml.SafeLoader)
        item = Item.create(self.board, config)
        self.assertIsNotNone(item)
        self.assertIsInstance(item, self.clazz)
        self.assertIsInstance(self.item, self.clazz)
        self.assertEqual(self.representation, repr(item))

    def test_name(self) -> None:
        self.assertIsNotNone(self.item.name)

    @property
    def representation(self) -> str:
        return "Item((Board(9, 9, 3, 3, None, None, None, None))"

    def test_repr(self):
        unittest.TestCase.maxDiff = None
        self.assertEqual(self.representation, repr(self.item))

    @property
    def str_representation(self) -> str:
        return self.representation

    def test_str(self):
        unittest.TestCase.maxDiff = None
        self.assertEqual(self.str_representation, str(self.item))

    def test_to_svg(self):
        self.assertIsNone(self.item.svg())

    def test_tags(self):
        self.assertIsInstance(self.item.tags, set)

    @property
    def has_rule(self) -> bool:
        return False

    def test_rules(self) -> None:
        self.assertIsNotNone(self.item.sorted_unique_rules)
        if self.has_rule:
            self.assertGreaterEqual(len(self.item.sorted_unique_rules), 1)
        else:
            self.assertEqual(len(self.item.sorted_unique_rules), 0)

    def test_sorted_unique_rules(self) -> None:
        rules = self.item.rules
        sorted_unique = self.item.sorted_unique_rules
        self.assertLessEqual(len(sorted_unique), len(rules))

    def test_glyphs(self):
        self.assertIsInstance(self.item.glyphs, list)

    @property
    def expected_classes(self) -> set[Type[Item]]:
        return {Item}

    def test_used_classes(self) -> None:
        if self.expected_classes != self.item.used_classes:  # pragma: no cover
            print(self.__class__.__name__)
            expected_names = sorted([cls.__name__ for cls in self.expected_classes])
            used_names = sorted([cls.__name__ for cls in self.item.used_classes])
            print(f"{{{', '.join(expected_names)}}}")
            print(f"{{{', '.join(used_names)}}}")
            print()
        self.assertEqual(self.expected_classes, self.item.used_classes)

    def test_add_constraint(self) -> None:
        solver = PulpSolver(self.board, 'test', "output/logs")
        self.item.add_constraint(solver, None, re.compile("Solution"))

    def test_add_bookkeeping_contraint(self) -> None:
        solver = PulpSolver(self.board, 'test', "output/logs")
        self.item.add_bookkeeping_contraint(solver, None, re.compile("Solution"))

    def test_bookkeeping(self) -> None:
        self.item.bookkeeping()

    def test_to_dict(self) -> None:
        config = yaml.load(self.config, Loader=yaml.SafeLoader)
        if "Item" in config:
            item = self.item
        else:
            item = Item.create(self.board, config)
        self.assertDictEqual(item.to_dict(), config)

    def test_css(self) -> None:
        self.assertIsNotNone(self.item.css())


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
