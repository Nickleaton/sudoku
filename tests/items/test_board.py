import unittest

from src.items.board import Board
from src.utils.coord import Coord


class TestBoard(unittest.TestCase):

    def test_construction_one(self):
        board = Board(9, 9, 3, 3, 'a', 'b', 'c', 'd')
        self.assertEqual(9, board.board_columns)
        self.assertEqual(9, board.board_rows)
        self.assertEqual(3, board.box_columns)
        self.assertEqual(3, board.box_rows)
        self.assertEqual('a', board.reference)
        self.assertEqual('b', board.video)
        self.assertEqual('c', board.title)
        self.assertEqual('d', board.author)

    def test_construction_two(self):
        board = Board(8, 8, 2, 4, 'a', 'b', 'c', 'd')
        self.assertEqual(8, board.board_columns)
        self.assertEqual(8, board.board_rows)
        self.assertEqual(4, board.box_columns)
        self.assertEqual(2, board.box_rows)
        self.assertEqual('a', board.reference)
        self.assertEqual('b', board.video)
        self.assertEqual('c', board.title)
        self.assertEqual('d', board.author)

    def test_yaml(self):
        board = Board(8, 8, 2, 4, 'a', 'b', 'c', 'd')
        yaml_string = (
            "Board:\n"
            "  Board: 8x8\n"
            "  Boxes: 2x4\n"
            "  Reference: a\n"
            "  Video: b\n"
            "  Title: c\n"
            "  Author: d\n"
        )
        self.assertEqual(yaml_string, board.to_yaml())

    def test_repr(self):
        board = Board(8, 8, 2, 4, 'a', 'b', 'c', 'd')
        self.assertEqual("Board(8, 8, 2, 4, 'a', 'b', 'c', 'd')", repr(board))

    def test_no_boxes(self):
        board = Board(9, 9, 0, 0, 'a', 'b', 'c', 'd')
        self.assertEqual(9, board.board_columns)
        self.assertEqual(9, board.board_rows)
        self.assertEqual(0, board.box_columns)
        self.assertEqual(0, board.box_rows)
        self.assertEqual('a', board.reference)
        self.assertEqual('b', board.video)
        self.assertEqual('c', board.title)
        self.assertEqual('d', board.author)

    def test_is_valid(self):
        board = Board(4, 4)
        self.assertTrue(board.is_valid(1, 1))
        self.assertTrue(board.is_valid(1, 4))
        self.assertTrue(board.is_valid(4, 1))
        self.assertTrue(board.is_valid(4, 4))
        self.assertFalse(board.is_valid(0, 1))
        self.assertFalse(board.is_valid(1, 0))
        self.assertFalse(board.is_valid(9, 1))
        self.assertFalse(board.is_valid(1, 9))

    def test_is_valid_coord(self):
        board = Board(4, 4)
        self.assertTrue(board.is_valid_coordinate(Coord(1, 1)))
        self.assertTrue(board.is_valid_coordinate(Coord(1, 4)))
        self.assertTrue(board.is_valid_coordinate(Coord(4, 1)))
        self.assertTrue(board.is_valid_coordinate(Coord(4, 4)))
        self.assertFalse(board.is_valid_coordinate(Coord(0, 1)))
        self.assertFalse(board.is_valid_coordinate(Coord(1, 0)))
        self.assertFalse(board.is_valid_coordinate(Coord(9, 1)))
        self.assertFalse(board.is_valid_coordinate(Coord(1, 9)))

        if __name__ == '__main__':  # pragma: no cover
            unittest.main()
