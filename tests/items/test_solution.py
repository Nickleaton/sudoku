import unittest

import oyaml as yaml

from src.items.board import Board
from src.items.solution import Solution


class TestSolution(unittest.TestCase):

    def setUp(self) -> None:
        self.board = Board(9, 9, 3, 3, None, None, None, None)
        data = [
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
        self.item = Solution(self.board, data)

    @property
    def representation(self) -> str:
        return (
            "Solution("
            "Board(9, 9, 3, 3, None, None, None, None),"
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
    def config(self) -> str:
        return (
            "Solution:\n"
            "  - '123456789'\n"
            "  - '123456789'\n"
            "  - '123456789'\n"
            "  - '123456789'\n"
            "  - '123456789'\n"
            "  - '123456789'\n"
            "  - '123456789'\n"
            "  - '123456789'\n"
            "  - '123456789'"
        )

    def test_create(self):
        config = yaml.load(self.config, Loader=yaml.SafeLoader)
        board = Board(9, 9, 3, 3, None, None, None, None)
        item = Solution(board, config['Solution'])
        self.assertIsNotNone(item)
        self.assertIsInstance(item, Solution)
        self.assertEqual(self.representation, repr(item))

    def test_repr(self):
        unittest.TestCase.maxDiff = None
        self.assertEqual(self.representation, repr(self.item))

    def test_set_get(self):
        self.assertEqual(1, self.item.get_value(1, 1))
        self.assertEqual(9, self.item.get_value(9, 9))
        self.item.set_value(1, 1, 8)
        self.item.set_value(9, 9, 8)
        self.assertEqual(8, self.item.get_value(1, 1))
        self.assertEqual(8, self.item.get_value(9, 9))


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
