"""TestSide."""
import unittest

from src.items.board import Board
from src.utils.coord import Coord
from src.utils.cyclic import Cyclic
from src.utils.direction import Direction
from src.utils.order import Order
from src.utils.side import Side


class TestSide(unittest.TestCase):
    """Test the Side class functionality."""

    def test_create(self):
        """Verify creation of valid Side instances."""
        self.assertEqual(Side.TOP, Side.create("T"))
        self.assertEqual(Side.RIGHT, Side.create("R"))
        self.assertEqual(Side.BOTTOM, Side.create("B"))
        self.assertEqual(Side.LEFT, Side.create("L"))

    def test_invalid(self):
        """Ensure ValueError is raised for invalid Side input."""
        with self.assertRaises(ValueError):
            Side.create("X")

    def test_valid(self):
        """Test if valid side values return True."""
        self.assertTrue(Side.valid('T'))
        self.assertTrue(Side.valid('R'))
        self.assertTrue(Side.valid('B'))
        self.assertTrue(Side.valid('L'))

    def test_horizontal_vertical_boundaries(self):
        """Verify horizontal and vertical properties of sides."""
        self.assertTrue(Side.TOP.vertical)
        self.assertFalse(Side.TOP.horizontal)
        self.assertTrue(Side.LEFT.horizontal)
        self.assertFalse(Side.LEFT.vertical)

    def test_values(self):
        """Check that all possible Side values are returned."""
        self.assertEqual("TRBL", Side.values())

    def test_marker_edge_cases(self):
        """Test marker method with edge cases on the board."""
        board = Board(9, 9)
        self.assertEqual(Coord(0, 0), Side.TOP.marker(board, 0))
        self.assertEqual(Coord(10, 9), Side.BOTTOM.marker(board, 9))

    def test_start_cell_edge_cases(self):
        """Test start_cell method with edge cases on the board."""
        board = Board(9, 9)
        self.assertEqual(Coord(1, 9), Side.TOP.start_cell(board, 9))
        self.assertEqual(Coord(9, 1), Side.BOTTOM.start_cell(board, 1))

    def test_direction(self):
        """Test direction calculation based on Cyclic values."""
        self.assertEqual(Direction.DOWN_RIGHT, Side.TOP.direction(Cyclic.CLOCKWISE))
        self.assertEqual(Direction.DOWN_LEFT, Side.RIGHT.direction(Cyclic.CLOCKWISE))
        self.assertEqual(Direction.UP_LEFT, Side.BOTTOM.direction(Cyclic.CLOCKWISE))
        self.assertEqual(Direction.UP_RIGHT, Side.LEFT.direction(Cyclic.CLOCKWISE))
        self.assertEqual(Direction.DOWN_LEFT, Side.TOP.direction(Cyclic.ANTICLOCKWISE))
        self.assertEqual(Direction.UP_LEFT, Side.RIGHT.direction(Cyclic.ANTICLOCKWISE))
        self.assertEqual(Direction.UP_RIGHT, Side.BOTTOM.direction(Cyclic.ANTICLOCKWISE))
        self.assertEqual(Direction.DOWN_RIGHT, Side.LEFT.direction(Cyclic.ANTICLOCKWISE))

    def test_order_direction(self):
        """Verify order direction for different Side and Order combinations."""
        self.assertEqual(Direction.DOWN, Side.TOP.order_direction(Order.INCREASING))
        self.assertEqual(Direction.UP, Side.TOP.order_direction(Order.DECREASING))
        self.assertEqual(Direction.LEFT, Side.RIGHT.order_direction(Order.INCREASING))
        self.assertEqual(Direction.RIGHT, Side.RIGHT.order_direction(Order.DECREASING))
        self.assertEqual(Direction.UP, Side.BOTTOM.order_direction(Order.INCREASING))
        self.assertEqual(Direction.DOWN, Side.BOTTOM.order_direction(Order.DECREASING))
        self.assertEqual(Direction.RIGHT, Side.LEFT.order_direction(Order.INCREASING))
        self.assertEqual(Direction.LEFT, Side.LEFT.order_direction(Order.DECREASING))

    def test_cell1(self):
        """Test marker method with various coordinates for a 9x9 board."""
        board = Board(9, 9)
        self.assertEqual(Coord(0, 5), Side.TOP.marker(board, 5))
        self.assertEqual(Coord(5, 10), Side.RIGHT.marker(board, 5))
        self.assertEqual(Coord(10, 5), Side.BOTTOM.marker(board, 5))
        self.assertEqual(Coord(5, 0), Side.LEFT.marker(board, 5))

    def test_cell2(self):
        """Test marker method with various coordinates for an 8x8 board."""
        board = Board(8, 8)
        self.assertEqual(Coord(0, 5), Side.TOP.marker(board, 5))
        self.assertEqual(Coord(5, 9), Side.RIGHT.marker(board, 5))
        self.assertEqual(Coord(9, 5), Side.BOTTOM.marker(board, 5))
        self.assertEqual(Coord(5, 0), Side.LEFT.marker(board, 5))

    def test_start_clockwise_1(self):
        """Test start method with CLOCKWISE rotation for a 9x9 board."""
        board = Board(9, 9)
        self.assertEqual(Coord(1, 6), Side.TOP.start(board, Cyclic.CLOCKWISE, 5))
        self.assertEqual(Coord(6, 9), Side.RIGHT.start(board, Cyclic.CLOCKWISE, 5))
        self.assertEqual(Coord(9, 4), Side.BOTTOM.start(board, Cyclic.CLOCKWISE, 5))
        self.assertEqual(Coord(4, 1), Side.LEFT.start(board, Cyclic.CLOCKWISE, 5))

    def test_start_anticlockwise_1(self):
        """Test start method with ANTICLOCKWISE rotation for a 9x9 board."""
        board = Board(9, 9)
        self.assertEqual(Coord(1, 3), Side.TOP.start(board, Cyclic.ANTICLOCKWISE, 4))
        self.assertEqual(Coord(3, 9), Side.RIGHT.start(board, Cyclic.ANTICLOCKWISE, 4))
        self.assertEqual(Coord(9, 5), Side.BOTTOM.start(board, Cyclic.ANTICLOCKWISE, 4))
        self.assertEqual(Coord(5, 1), Side.LEFT.start(board, Cyclic.ANTICLOCKWISE, 4))

    def test_start_clockwise_2(self):
        """Test start method with CLOCKWISE rotation for a 4x4 board."""
        board = Board(4, 4)
        self.assertEqual(Coord(1, 3), Side.TOP.start(board, Cyclic.CLOCKWISE, 2))
        self.assertEqual(Coord(3, 4), Side.RIGHT.start(board, Cyclic.CLOCKWISE, 2))
        self.assertEqual(Coord(4, 1), Side.BOTTOM.start(board, Cyclic.CLOCKWISE, 2))
        self.assertEqual(Coord(1, 1), Side.LEFT.start(board, Cyclic.CLOCKWISE, 2))

    def test_start_anticlockwise_2(self):
        """Test start method with ANTICLOCKWISE rotation for a 4x4 board."""
        board = Board(4, 4)
        self.assertEqual(Coord(1, 2), Side.TOP.start(board, Cyclic.ANTICLOCKWISE, 3))
        self.assertEqual(Coord(2, 4), Side.RIGHT.start(board, Cyclic.ANTICLOCKWISE, 3))
        self.assertEqual(Coord(4, 4), Side.BOTTOM.start(board, Cyclic.ANTICLOCKWISE, 3))
        self.assertEqual(Coord(4, 1), Side.LEFT.start(board, Cyclic.ANTICLOCKWISE, 3))

    def test_repr(self):
        """Verify string representation of each Side."""
        self.assertEqual('Side.TOP', repr(Side.TOP))
        self.assertEqual('Side.RIGHT', repr(Side.RIGHT))
        self.assertEqual('Side.BOTTOM', repr(Side.BOTTOM))
        self.assertEqual('Side.LEFT', repr(Side.LEFT))

    def test_vertical(self):
        """Test vertical property for each Side."""
        self.assertTrue(Side.TOP.vertical)
        self.assertTrue(Side.BOTTOM.vertical)
        self.assertFalse(Side.LEFT.vertical)
        self.assertFalse(Side.RIGHT.vertical)

    def test_horizontal(self):
        """Test horizontal property for each Side."""
        self.assertFalse(Side.TOP.horizontal)
        self.assertFalse(Side.BOTTOM.horizontal)
        self.assertTrue(Side.LEFT.horizontal)
        self.assertTrue(Side.RIGHT.horizontal)

    def test_order_offset(self):
        """Test order offset for each Side."""
        self.assertEqual(Coord(1, 0), Side.TOP.order_offset())
        self.assertEqual(Coord(0, -1), Side.RIGHT.order_offset())
        self.assertEqual(Coord(-1, 0), Side.BOTTOM.order_offset())
        self.assertEqual(Coord(0, 1), Side.LEFT.order_offset())

    def test_start_cell(self):
        """Test start_cell method for each Side."""
        board = Board(9, 9)
        self.assertEqual(Coord(1, 1), Side.TOP.start_cell(board, 1))
        self.assertEqual(Coord(9, 9), Side.RIGHT.start_cell(board, 9))
        self.assertEqual(Coord(9, 9), Side.BOTTOM.start_cell(board, 9))
        self.assertEqual(Coord(1, 1), Side.LEFT.start_cell(board, 1))


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
