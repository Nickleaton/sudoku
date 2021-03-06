import unittest

from src.items.board import Board
from src.solvers.answer import Answer


class TestAnswer(unittest.TestCase):

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
        self.item = Answer(self.board, data)
        data = [
            "123456789",
            "123456789",
            "123456789",
            "123456789",
            "123456789",
            "123456789",
            "123456789",
            "123456789",
            "123456781"
        ]
        self.other = Answer(self.board, data)

    @property
    def representation(self) -> str:
        return (
            "Answer("
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

    def test_equality(self):
        self.assertEqual(self.item, self.item)
        self.assertNotEqual(self.item, self.other)
        with self.assertRaises(Exception):
            _ = self.item == '123'

    def test_string(self):
        text = ("Answer:\n"
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

        self.assertEqual(text, str(self.item))

    def test_standard_output(self):
        expected = (
            "+-------+-------+-------+\n"
            "| 1 2 3 | 4 5 6 | 7 8 9 |\n"
            "| 1 2 3 | 4 5 6 | 7 8 9 |\n"
            "| 1 2 3 | 4 5 6 | 7 8 9 |\n"
            "+-------+-------+-------+\n"
            "| 1 2 3 | 4 5 6 | 7 8 9 |\n"
            "| 1 2 3 | 4 5 6 | 7 8 9 |\n"
            "| 1 2 3 | 4 5 6 | 7 8 9 |\n"
            "+-------+-------+-------+\n"
            "| 1 2 3 | 4 5 6 | 7 8 9 |\n"
            "| 1 2 3 | 4 5 6 | 7 8 9 |\n"
            "| 1 2 3 | 4 5 6 | 7 8 9 |\n"
            "+-------+-------+-------+\n"
        )
        self.assertEqual(expected, self.item.standard_string())


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
