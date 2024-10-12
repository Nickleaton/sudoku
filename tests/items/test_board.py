import unittest

from src.items.board import Board
from src.utils.coord import Coord


class TestBoard(unittest.TestCase):

    def setUp(self):
        self.board9x9 = Board(9, 9, 3, 3, 'a', 'b', 'c', 'd')
        self.board9x9_no_boxes = board = Board(9, 9, 0, 0, 'a', 'b', 'c', 'd')
        self.board4x4 = Board(4, 4)
        self.board8x8 = board = Board(8, 8, 2, 4, 'a', 'b', 'c', 'd')

    def test_construction_one(self):
        self.assertEqual(9, self.board9x9.board_columns)
        self.assertEqual(9, self.board9x9.board_rows)
        self.assertEqual(3, self.board9x9.box_columns)
        self.assertEqual(3, self.board9x9.box_rows)
        self.assertEqual('a', self.board9x9.reference)
        self.assertEqual('b', self.board9x9.video)
        self.assertEqual('c', self.board9x9.title)
        self.assertEqual('d', self.board9x9.author)

    def test_construction_two(self):
        self.assertEqual(8, self.board8x8.board_columns)
        self.assertEqual(8, self.board8x8.board_rows)
        self.assertEqual(4, self.board8x8.box_columns)
        self.assertEqual(2, self.board8x8.box_rows)
        self.assertEqual('a', self.board8x8.reference)
        self.assertEqual('b', self.board8x8.video)
        self.assertEqual('c', self.board8x8.title)
        self.assertEqual('d', self.board8x8.author)

    def test_yaml(self):
        yaml_string = (
            "Board:\n"
            "  Board: 8x8\n"
            "  Boxes: 2x4\n"
            "  Reference: a\n"
            "  Video: b\n"
            "  Title: c\n"
            "  Author: d\n"
        )
        self.assertEqual(yaml_string, self.board8x8.to_yaml())

    def test_repr(self):
        self.assertEqual("Board(8, 8, 2, 4, 'a', 'b', 'c', 'd')", repr(self.board8x8))

    def test_no_boxes(self):
        self.assertEqual(9, self.board9x9_no_boxes.board_columns)
        self.assertEqual(9, self.board9x9_no_boxes.board_rows)
        self.assertEqual(0, self.board9x9_no_boxes.box_columns)
        self.assertEqual(0, self.board9x9_no_boxes.box_rows)
        self.assertEqual('a', self.board9x9_no_boxes.reference)
        self.assertEqual('b', self.board9x9_no_boxes.video)
        self.assertEqual('c', self.board9x9_no_boxes.title)
        self.assertEqual('d', self.board9x9_no_boxes.author)

    def test_is_valid(self):
        self.assertTrue(self.board4x4.is_valid(1, 1))
        self.assertTrue(self.board4x4.is_valid(1, 4))
        self.assertTrue(self.board4x4.is_valid(4, 1))
        self.assertTrue(self.board4x4.is_valid(4, 4))
        self.assertFalse(self.board4x4.is_valid(0, 1))
        self.assertFalse(self.board4x4.is_valid(1, 0))
        self.assertFalse(self.board4x4.is_valid(9, 1))
        self.assertFalse(self.board4x4.is_valid(1, 9))

    def test_is_valid_coord(self):
        self.assertTrue(self.board4x4.is_valid_coordinate(Coord(1, 1)))
        self.assertTrue(self.board4x4.is_valid_coordinate(Coord(1, 4)))
        self.assertTrue(self.board4x4.is_valid_coordinate(Coord(4, 1)))
        self.assertTrue(self.board4x4.is_valid_coordinate(Coord(4, 4)))
        self.assertFalse(self.board4x4.is_valid_coordinate(Coord(0, 1)))
        self.assertFalse(self.board4x4.is_valid_coordinate(Coord(1, 0)))
        self.assertFalse(self.board4x4.is_valid_coordinate(Coord(9, 1)))
        self.assertFalse(self.board4x4.is_valid_coordinate(Coord(1, 9)))

    def test_box_index(self):
        self.assertEqual(1, self.board9x9.box_index(1, 1))
        self.assertEqual(1, self.board9x9.box_index(2, 2))
        self.assertEqual(1, self.board9x9.box_index(3, 3))
        self.assertEqual(2, self.board9x9.box_index(2, 5))
        self.assertEqual(3, self.board9x9.box_index(2, 8))
        self.assertEqual(5, self.board9x9.box_index(5, 5))
        self.assertEqual(6, self.board9x9.box_index(5, 9))
        self.assertEqual(9, self.board9x9.box_index(9, 9))


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
