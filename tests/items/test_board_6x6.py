import unittest

from src.items.board import Board
from src.utils.coord import Coord


class TestBoard6x6(unittest.TestCase):

    def setUp(self):
        self.board = Board(6, 6, 2, 3, 'a', 'b', 'c', 'd')
        self.rows = [1, 2, 3, 4, 5, 6]
        self.columns = [1, 2, 3, 4, 5, 6]
        self.bad_rows = [0, 7]
        self.bad_columns = [0, 7]

    @staticmethod
    def get_box_number(row: int, col: int) -> int:
        box_row = (row - 1) // 2  # Divide by 2 for rows
        box_col = (col - 1) // 3  # Divide by 3 for columns
        return box_row * 2 + box_col + 1

    def test_construction(self):
        self.assertEqual(6, self.board.board_columns)
        self.assertEqual(6, self.board.board_rows)
        self.assertEqual(3, self.board.box_columns)
        self.assertEqual(2, self.board.box_rows)
        self.assertEqual('a', self.board.reference)
        self.assertEqual('b', self.board.video)
        self.assertEqual('c', self.board.title)
        self.assertEqual('d', self.board.author)

    def test_yaml(self):
        yaml_string = (
            "Board:\n"
            "  Board: 6x6\n"
            "  Boxes: 2x3\n"
            "  Reference: a\n"
            "  Video: b\n"
            "  Title: c\n"
            "  Author: d\n"
        )
        self.assertEqual(yaml_string, self.board.to_yaml())

    def test_high_mid_low(self):
        self.assertListEqual(self.board.low, [1, 2])
        self.assertListEqual(self.board.mid, [3, 4])
        self.assertListEqual(self.board.high, [5, 6])

    def test_modulo(self):
        self.assertEqual(self.board.mod0, [3, 6])
        self.assertEqual(self.board.mod1, [1, 4])
        self.assertEqual(self.board.mod2, [2, 5])

    def test_repr(self):
        self.assertEqual("Board(6, 6, 2, 3, 'a', 'b', 'c', 'd')", repr(self.board))

    def test_is_valid(self):
        for row in self.rows:
            for column in self.columns:
                self.assertTrue(self.board.is_valid(row, column))
        for row in self.bad_rows:
            for column in self.bad_columns:
                self.assertFalse(self.board.is_valid(row, column))

    def test_is_valid_coord(self):
        for row in self.rows:
            for column in self.columns:
                self.assertTrue(self.board.is_valid_coordinate(Coord(row, column)))
        for row in self.bad_rows:
            for column in self.bad_columns:
                self.assertFalse(self.board.is_valid_coordinate(Coord(row, column)))

    def test_box_index(self):
        for row in self.rows:
            for column in self.columns:
                self.assertEqual(TestBoard6x6.get_box_number(row, column), self.board.box_index(row, column))

    def test_prime(self):
        self.assertEqual([2, 3, 5], self.board.primes)


if __name__ == '__main__':  # pragma: no cover
    unittest.main()