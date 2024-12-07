"""TestComposed."""
import unittest
from typing import Type

from src.items.board import Board
from src.items.composed_item import ComposedItem
from src.items.item import Item
from tests.items.test_item import TestItem


class TestComposed(TestItem):
    """Test suite for the ComposedItem class."""

    def setUp(self) -> None:
        """Set up the Board and ComposedItem instance for testing."""
        super().setUp()
        self.item = ComposedItem(self.board, [])
        self.size = 0

    @property
    def clazz(self):
        """Return the ComposedItem class."""
        return ComposedItem

    def test_construction(self):
        """Test the construction of the ComposedItem."""
        self.assertEqual(self.size, len(self.item.items))

    def test_iteration(self):
        """Test the iteration over the items in the ComposedItem."""
        count = 0
        for _ in self.item:
            count += 1
        self.assertEqual(self.size, count)

    @property
    def config(self) -> str:
        """Return the configuration string for the ComposedItem."""
        return "ComposedItem:"

    @property
    def representation(self) -> str:
        """Return the string representation for the ComposedItem."""
        return "ComposedItem(Board(9, 9, 3, 3, None, None, None, None), [])"

    @property
    def has_rule(self) -> bool:
        """Indicates if the ComposedItem has a rule."""
        return False

    @property
    def expected_classes(self) -> set[Type[Item]]:
        """Return the expected classes that the ComposedItem should belong to."""
        return {Item, ComposedItem}

    def test_top(self):
        """Test getting the top item of the ComposedItem."""
        child = Item(self.board)
        self.item.add(child)
        self.assertEqual(self.item, self.item.top)
        self.assertEqual(self.item, child.top)

    def test_flatten(self) -> None:
        """Test flattening the ComposedItem and its child items."""
        expected = [self.item]
        for item in self.item.items:
            expected.extend(item.flatten())
        self.assertListEqual(expected, self.item.flatten())


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
