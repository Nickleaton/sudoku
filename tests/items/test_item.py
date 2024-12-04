"""TestItem."""
import unittest
from typing import Type

import oyaml as yaml

from src.items.board import Board
from src.items.item import Item
from src.solvers.pulp_solver import PulpSolver


class TestItem(unittest.TestCase):
    """Test suite for the Item class."""

    def setUp(self) -> None:
        """Set up the test case with a board and an Item instance."""
        self.board = Board(9, 9, 3, 3, None, None, None, None)
        self.item = Item(self.board)

    @property
    def clazz(self):
        """Return the Item class."""
        return Item

    def test_clazz(self):
        """Test that the class of the item matches the expected class."""
        self.assertEqual(self.item.__class__, self.clazz)

    def test_top(self):
        """Test that the top item of the item is itself."""
        self.assertEqual(self.item.top, self.item)

    def test_register(self):
        """Test that the item is properly registered in the Item classes registry."""
        self.assertIn(self.item.__class__.__name__, Item.classes)
        self.assertEqual(Item.classes[self.item.__class__.__name__], self.item.__class__)

    @property
    def config(self) -> str:
        """Return the configuration string for Item."""
        return "Item:"

    def test_create(self) -> None:
        """Test creating an Item instance from a configuration string."""
        config = yaml.load(self.config, Loader=yaml.SafeLoader)
        if self.item.__class__.__name__ == 'Item':
            return
        item = Item.create(self.board, config)
        self.assertIsNotNone(item)
        self.assertIsInstance(item, self.clazz)
        self.assertIsInstance(self.item, self.clazz)
        self.assertEqual(self.representation, repr(item))

    def test_name(self) -> None:
        """Test that the item has a valid name."""
        self.assertIsNotNone(self.item.name)
        self.assertTrue(self.item.name.startswith(f"{self.clazz.__name__}_"))

    @property
    def representation(self) -> str:
        """Return a string representation of the Item instance."""
        return f"Item({self.board!r})"

    def test_repr(self):
        """Test the string representation of the Item instance."""
        if self.representation != repr(self.item):
            print (f"{self.representation} != {self.item!r}")
        print()
        print()
        print(self.representation)
        print(repr(self.item))
        print()
        self.assertEqual(self.representation, repr(self.item))

    @property
    def str_representation(self) -> str:
        """Return the string representation of the Item."""
        return self.representation

    def test_str(self):
        """Test the string conversion of the Item instance."""
        unittest.TestCase.maxDiff = None
        self.assertEqual(self.str_representation, str(self.item))

    def test_to_svg(self):
        """Test the to_svg method of the Item instance."""
        self.assertIsNone(self.item.svg())

    def test_tags(self):
        """Test that the Item instance has a set of tags."""
        self.assertIsInstance(self.item.tags, set)

    @property
    def has_rule(self) -> bool:
        """Return whether the item has a rule."""
        return False

    def test_rules(self) -> None:
        """Test the sorting and unique rules of the item."""
        self.assertIsNotNone(self.item.sorted_unique_rules)
        if self.has_rule:
            self.assertGreaterEqual(len(self.item.sorted_unique_rules), 1)
        else:
            self.assertEqual(len(self.item.sorted_unique_rules), 0)

    def test_sorted_unique_rules(self) -> None:
        """Test that the sorted unique rules are less than or equal to the total rules."""
        rules = self.item.rules
        sorted_unique = self.item.sorted_unique_rules
        self.assertLessEqual(len(sorted_unique), len(rules))

    def test_glyphs(self):
        """Test that the glyphs method returns a list."""
        self.assertIsInstance(self.item.glyphs(), list)

    @property
    def expected_classes(self) -> set[Type[Item]]:
        """Return the expected classes that the Item should belong to."""
        return {Item}

    def test_used_classes(self) -> None:
        """Test that the used classes of the Item match the expected classes."""
        expected_names = sorted([cls.__name__ for cls in self.expected_classes])
        used_names = sorted([cls.__name__ for cls in self.item.used_classes])
        if expected_names != used_names:  # pragma: no cover
            print(self.__class__.__name__)
            print(f"{{{', '.join(expected_names)}}}")
            print(f"{{{', '.join(used_names)}}}")
            print()
        self.assertCountEqual(expected_names, used_names)

    def test_walk(self):
        """Test the walk method of the Item instance."""
        count = 1
        for _ in self.item.walk():
            count += 1
        self.assertGreaterEqual(count, 1)

    def test_add_constraint(self) -> None:
        """Test adding a constraint to the Item."""
        solver = PulpSolver(self.board, 'test')
        self.item.add_constraint(solver)

    def test_to_dict(self) -> None:
        """Test the to_dict method of the Item instance."""
        config = yaml.load(self.config, Loader=yaml.SafeLoader)
        if "Item" in config:
            item = self.item
        else:
            item = Item.create(self.board, config)
        self.assertDictEqual(item.to_dict(), config)

    def test_css(self) -> None:
        """Test the css method of the Item instance."""
        self.assertIsNotNone(self.item.css())

    def test_flatten(self) -> None:
        """Test the flatten method of the Item instance."""
        self.assertListEqual([self.item], self.item.flatten())

    def test_schema(self) -> None:
        """Test the schema method of the Item instance."""
        self.assertIsNotNone(self.item.schema())
        # self.assertIsInstance(self.item.schema(), dict)


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
