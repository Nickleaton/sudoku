import unittest

from src.utils.coord import Coord
from src.utils.direction import Direction


class TestDirection(unittest.TestCase):
    """Test the Direction class."""

    def test_create(self):
        """Test creating Direction instances from string input."""
        self.assertEqual(Direction.up_left, Direction.create("UL"))
        self.assertEqual(Direction.up, Direction.create("U"))
        self.assertEqual(Direction.down_right, Direction.create("DR"))
        with self.assertRaises(ValueError):
            Direction.create('XX')

    def test_to_coord(self):
        """Test the coordinate offset for each Direction."""
        self.assertEqual(Direction.up_left.coord, Coord(-1, -1))
        self.assertEqual(Direction.up.coord, Coord(-1, 0))
        self.assertEqual(Direction.right.coord, Coord(0, 1))
        self.assertEqual(Direction.down.coord, Coord(1, 0))
        self.assertEqual(Direction.down_right.coord, Coord(1, 1))

    def test_repr(self):
        """Test the string representation of Direction instances."""
        self.assertEqual('Direction.up_left', repr(Direction.up_left))
        self.assertEqual('Direction.up', repr(Direction.up))
        self.assertEqual('Direction.down_right', repr(Direction.down_right))


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
