import unittest

from src.items.board import Board
from src.utils.coord import Coord
from src.utils.cyclic import Cyclic
from src.utils.direction import Direction
from src.utils.order import Order
from src.utils.side import Side


class TestSide(unittest.TestCase):

    def test_create(self):
        self.assertEqual(Side.TOP, Side.create("T"))
        self.assertEqual(Side.RIGHT, Side.create("R"))
        self.assertEqual(Side.BOTTOM, Side.create("B"))
        self.assertEqual(Side.LEFT, Side.create("L"))

    def test_valid(self):
        self.assertTrue(Side.valid('T'))
        self.assertTrue(Side.valid('R'))
        self.assertTrue(Side.valid('B'))
        self.assertTrue(Side.valid('L'))
        self.assertFalse(Side.valid('X'))

    def test_direction(self):
        self.assertEqual(Direction.DOWN_RIGHT, Side.TOP.direction(Cyclic.CLOCKWISE))
        self.assertEqual(Direction.DOWN_LEFT, Side.RIGHT.direction(Cyclic.CLOCKWISE))
        self.assertEqual(Direction.UP_LEFT, Side.BOTTOM.direction(Cyclic.CLOCKWISE))
        self.assertEqual(Direction.UP_RIGHT, Side.LEFT.direction(Cyclic.CLOCKWISE))
        self.assertEqual(Direction.DOWN_LEFT, Side.TOP.direction(Cyclic.ANTICLOCKWISE))
        self.assertEqual(Direction.UP_LEFT, Side.RIGHT.direction(Cyclic.ANTICLOCKWISE))
        self.assertEqual(Direction.UP_RIGHT, Side.BOTTOM.direction(Cyclic.ANTICLOCKWISE))
        self.assertEqual(Direction.DOWN_RIGHT, Side.LEFT.direction(Cyclic.ANTICLOCKWISE))

    def test_order_direction(self):
        self.assertEqual(Direction.DOWN, Side.TOP.order_direction(Order.INCREASING))
        self.assertEqual(Direction.UP, Side.TOP.order_direction(Order.DECREASING))
        self.assertEqual(Direction.LEFT, Side.RIGHT.order_direction(Order.INCREASING))
        self.assertEqual(Direction.RIGHT, Side.RIGHT.order_direction(Order.DECREASING))
        self.assertEqual(Direction.UP, Side.BOTTOM.order_direction(Order.INCREASING))
        self.assertEqual(Direction.DOWN, Side.BOTTOM.order_direction(Order.DECREASING))
        self.assertEqual(Direction.RIGHT, Side.LEFT.order_direction(Order.INCREASING))
        self.assertEqual(Direction.LEFT, Side.LEFT.order_direction(Order.DECREASING))

    def test_cell1(self):
        board = Board(9, 9)
        self.assertEqual(Coord(0, 5), Side.TOP.marker(board, 5))
        self.assertEqual(Coord(5, 10), Side.RIGHT.marker(board, 5))
        self.assertEqual(Coord(10, 5), Side.BOTTOM.marker(board, 5))
        self.assertEqual(Coord(5, 0), Side.LEFT.marker(board, 5))

    def test_cell2(self):
        board = Board(8, 8)
        self.assertEqual(Coord(0, 5), Side.TOP.marker(board, 5))
        self.assertEqual(Coord(5, 9), Side.RIGHT.marker(board, 5))
        self.assertEqual(Coord(9, 5), Side.BOTTOM.marker(board, 5))
        self.assertEqual(Coord(5, 0), Side.LEFT.marker(board, 5))

    def test_start_clockwise_1(self):
        board = Board(9, 9)
        self.assertEqual(Coord(1, 6), Side.TOP.start(board, Cyclic.CLOCKWISE, 5))
        self.assertEqual(Coord(6, 9), Side.RIGHT.start(board, Cyclic.CLOCKWISE, 5))
        self.assertEqual(Coord(9, 4), Side.BOTTOM.start(board, Cyclic.CLOCKWISE, 5))
        self.assertEqual(Coord(4, 1), Side.LEFT.start(board, Cyclic.CLOCKWISE, 5))

    def test_start_anticlockwise_1(self):
        board = Board(9, 9)
        self.assertEqual(Coord(1, 3), Side.TOP.start(board, Cyclic.ANTICLOCKWISE, 4))
        self.assertEqual(Coord(3, 9), Side.RIGHT.start(board, Cyclic.ANTICLOCKWISE, 4))
        self.assertEqual(Coord(9, 5), Side.BOTTOM.start(board, Cyclic.ANTICLOCKWISE, 4))
        self.assertEqual(Coord(5, 1), Side.LEFT.start(board, Cyclic.ANTICLOCKWISE, 4))

    def test_start_clockwise_2(self):
        board = Board(4, 4)
        self.assertEqual(Coord(1, 3), Side.TOP.start(board, Cyclic.CLOCKWISE, 2))
        self.assertEqual(Coord(3, 4), Side.RIGHT.start(board, Cyclic.CLOCKWISE, 2))
        self.assertEqual(Coord(4, 1), Side.BOTTOM.start(board, Cyclic.CLOCKWISE, 2))
        self.assertEqual(Coord(1, 1), Side.LEFT.start(board, Cyclic.CLOCKWISE, 2))

    def test_start_anticlockwise_2(self):
        board = Board(4, 4)
        self.assertEqual(Coord(1, 2), Side.TOP.start(board, Cyclic.ANTICLOCKWISE, 3))
        self.assertEqual(Coord(2, 4), Side.RIGHT.start(board, Cyclic.ANTICLOCKWISE, 3))
        self.assertEqual(Coord(4, 4), Side.BOTTOM.start(board, Cyclic.ANTICLOCKWISE, 3))
        self.assertEqual(Coord(4, 1), Side.LEFT.start(board, Cyclic.ANTICLOCKWISE, 3))

    def test_repr(self):
        self.assertEqual('Side.TOP', repr(Side.TOP))
        self.assertEqual('Side.RIGHT', repr(Side.RIGHT))
        self.assertEqual('Side.BOTTOM', repr(Side.BOTTOM))
        self.assertEqual('Side.LEFT', repr(Side.LEFT))

    def test_vertical(self):
        self.assertTrue(Side.TOP.vertical)
        self.assertTrue(Side.BOTTOM.vertical)
        self.assertFalse(Side.LEFT.vertical)
        self.assertFalse(Side.RIGHT.vertical)

    def test_horizontal(self):
        self.assertFalse(Side.TOP.horizontal)
        self.assertFalse(Side.BOTTOM.horizontal)
        self.assertTrue(Side.LEFT.horizontal)
        self.assertTrue(Side.RIGHT.horizontal)

if __name__ == '__main__':  # pragma: no cover
    unittest.main()
