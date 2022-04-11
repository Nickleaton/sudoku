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
    def config(self):
        return "Item:"

    def test_create(self):
        if self.item.__class__.__name__ == 'Item':
            return
        config = yaml.load(self.config, Loader=yaml.SafeLoader)
        board = Board(9, 9, 3, 3, None, None, None, None)
        item = Item.create(self.item.__class__.__name__, board, config[self.item.__class__.__name__])
        self.assertIsNotNone(item)
        self.assertIsInstance(item, self.item.__class__)
        self.assertEqual(self.representation, repr(item))

    def test_name(self):
        self.assertIsNotNone(self.item.name)

    @property
    def representation(self) -> str:
        return "Item((Board(9, 9, 3, 3, None, None, None, None))"

    def test_repr(self):
        unittest.TestCase.maxDiff = None
        self.assertEqual(self.representation, repr(self.item))

    def xxx_test_as_yaml(self): # TODO
        print('-' * 80)
        print(self.config)
        print(self.item.to_yaml)
        self.assertEqual(self.config, self.item.to_yaml)

    def test_to_svg(self):
        self.assertIsNone(self.item.svg())

    def test_tags(self):
        self.assertIsInstance(self.item.tags, set)

    @property
    def has_rule(self) -> bool:
        return False

    def test_rules(self):
        self.assertIsNotNone(self.item.sorted_unique_rules)
        if self.has_rule:
            self.assertGreaterEqual(len(self.item.sorted_unique_rules), 1)
        else:
            self.assertEqual(len(self.item.sorted_unique_rules), 0)

    def test_sorted_unique_rules(self):
        rules = self.item.rules
        sorted_unique = self.item.sorted_unique_rules
        self.assertLessEqual(len(sorted_unique), len(rules))

    def test_glyphs(self):
        self.assertIsInstance(self.item.glyphs, list)

    @property
    def expected_classes(self) -> set[Type[Item]]:
        return {Item}

    def test_used_classes(self):
        # print(self.__class__.__name__)
        # expected_names = sorted([cls.__name__ for cls in self.expected_classes])
        # used_names = sorted([cls.__name__ for cls in self.item.used_classes])
        # print(f"{{{', '.join(expected_names)}}}")
        # print(f"{{{', '.join(used_names)}}}")
        # print()
        self.assertEqual(self.expected_classes, self.item.used_classes)

    def test_add_variables(self):
        solver = PulpSolver(self.board)
        self.item.add_variables(self.board, solver)

    def test_add_constraint(self):
        solver = PulpSolver(self.board)
        self.item.add_variables(self.board, solver)
        self.item.add_constraint(solver)


if __name__ == '__main__':  # pragma: no cover
    unittest.main()