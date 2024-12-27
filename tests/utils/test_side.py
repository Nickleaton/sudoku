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
        self.assertEqual(Side.top, Side.create("T"))
        self.assertEqual(Side.right, Side.create("R"))
        self.assertEqual(Side.bottom, Side.create("B"))
        self.assertEqual(Side.left, Side.create("L"))

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
        self.assertTrue(Side.top.vertical)
        self.assertFalse(Side.top.horizontal)
        self.assertTrue(Side.left.horizontal)
        self.assertFalse(Side.left.vertical)

    def test_values(self):
        """Check that all possible Side value_list are returned."""
        self.assertEqual("TRBL", Side.choices())


    def test_direction(self):
        """Test direction calculation based on Cyclic value_list."""
        self.assertEqual(Moves.down_right, Side.top.direction(Cyclic.clockwise))
        self.assertEqual(Moves.down_left, Side.right.direction(Cyclic.clockwise))
        self.assertEqual(Moves.up_left, Side.bottom.direction(Cyclic.clockwise))
        self.assertEqual(Moves.up_right, Side.left.direction(Cyclic.clockwise))
        self.assertEqual(Moves.down_left, Side.top.direction(Cyclic.anticlockwise))
        self.assertEqual(Moves.up_left, Side.right.direction(Cyclic.anticlockwise))
        self.assertEqual(Moves.up_right, Side.bottom.direction(Cyclic.anticlockwise))
        self.assertEqual(Moves.down_right, Side.left.direction(Cyclic.anticlockwise))

    def test_order_direction(self):
        """Verify order direction for different Side and Order combinations."""
        self.assertEqual(Moves.down, Side.top.order_direction(Order.increasing))
        self.assertEqual(Moves.up, Side.top.order_direction(Order.decreasing))
        self.assertEqual(Moves.left, Side.right.order_direction(Order.increasing))
        self.assertEqual(Moves.right, Side.right.order_direction(Order.decreasing))
        self.assertEqual(Moves.up, Side.bottom.order_direction(Order.increasing))
        self.assertEqual(Moves.down, Side.bottom.order_direction(Order.decreasing))
        self.assertEqual(Moves.right, Side.left.order_direction(Order.increasing))
        self.assertEqual(Moves.left, Side.left.order_direction(Order.decreasing))

    def test_repr(self):
        """Verify string representation of each Side."""
        self.assertEqual('Side.top', repr(Side.top))
        self.assertEqual('Side.right', repr(Side.right))
        self.assertEqual('Side.bottom', repr(Side.bottom))
        self.assertEqual('Side.left', repr(Side.left))

    def test_vertical(self):
        """Test vertical property for each Side."""
        self.assertTrue(Side.top.vertical)
        self.assertTrue(Side.bottom.vertical)
        self.assertFalse(Side.left.vertical)
        self.assertFalse(Side.right.vertical)

    def test_horizontal(self):
        """Test horizontal property for each Side."""
        self.assertFalse(Side.top.horizontal)
        self.assertFalse(Side.bottom.horizontal)
        self.assertTrue(Side.left.horizontal)
        self.assertTrue(Side.right.horizontal)

    def test_order_offset(self):
        """Test order offset for each Side."""
        self.assertEqual(Coord(1, 0), Side.top.order_offset())
        self.assertEqual(Coord(0, -1), Side.right.order_offset())
        self.assertEqual(Coord(-1, 0), Side.bottom.order_offset())
        self.assertEqual(Coord(0, 1), Side.left.order_offset())


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
