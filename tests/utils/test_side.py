"""TestSide."""
import unittest

from src.utils.coord import Coord
from src.utils.cyclic import Cyclic
from src.utils.moves import Moves
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
        """Test if valid side value_list return True."""
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
        """Check that all possible Side value_list are returned."""
        self.assertEqual("TRBL", Side.choices())


    def test_direction(self):
        """Test direction calculation based on Cyclic value_list."""
        self.assertEqual(Moves.DOWN_RIGHT, Side.TOP.direction(Cyclic.CLOCKWISE))
        self.assertEqual(Moves.DOWN_LEFT, Side.RIGHT.direction(Cyclic.CLOCKWISE))
        self.assertEqual(Moves.UP_LEFT, Side.BOTTOM.direction(Cyclic.CLOCKWISE))
        self.assertEqual(Moves.UP_RIGHT, Side.LEFT.direction(Cyclic.CLOCKWISE))
        self.assertEqual(Moves.DOWN_LEFT, Side.TOP.direction(Cyclic.ANTICLOCKWISE))
        self.assertEqual(Moves.UP_LEFT, Side.RIGHT.direction(Cyclic.ANTICLOCKWISE))
        self.assertEqual(Moves.UP_RIGHT, Side.BOTTOM.direction(Cyclic.ANTICLOCKWISE))
        self.assertEqual(Moves.DOWN_RIGHT, Side.LEFT.direction(Cyclic.ANTICLOCKWISE))

    def test_order_direction(self):
        """Verify order direction for different Side and Order combinations."""
        self.assertEqual(Moves.DOWN, Side.TOP.order_direction(Order.INCREASING))
        self.assertEqual(Moves.UP, Side.TOP.order_direction(Order.DECREASING))
        self.assertEqual(Moves.LEFT, Side.RIGHT.order_direction(Order.INCREASING))
        self.assertEqual(Moves.RIGHT, Side.RIGHT.order_direction(Order.DECREASING))
        self.assertEqual(Moves.UP, Side.BOTTOM.order_direction(Order.INCREASING))
        self.assertEqual(Moves.DOWN, Side.BOTTOM.order_direction(Order.DECREASING))
        self.assertEqual(Moves.RIGHT, Side.LEFT.order_direction(Order.INCREASING))
        self.assertEqual(Moves.LEFT, Side.LEFT.order_direction(Order.DECREASING))

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


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
