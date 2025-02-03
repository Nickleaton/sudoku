import unittest

from src.utils.coord import Coord
from src.utils.direction import Direction


class TestDirection(unittest.TestCase):
    """Test the Direction class."""

    def test_create(self):
        """Test creating Direction instances from string input."""
        self.assertEqual(Direction.UP_LEFT, Direction.create("UL"))
        self.assertEqual(Direction.UP, Direction.create("U"))
        self.assertEqual(Direction.DOWN_RIGHT, Direction.create("DR"))
        with self.assertRaises(ValueError):
            Direction.create('XX')

    def test_to_coord(self):
        """Test the coordinate offset for each Direction."""
        self.assertEqual(Direction.UP_LEFT.coord, Coord(-1, -1))
        self.assertEqual(Direction.UP.coord, Coord(-1, 0))
        self.assertEqual(Direction.RIGHT.coord, Coord(0, 1))
        self.assertEqual(Direction.DOWN.coord, Coord(1, 0))
        self.assertEqual(Direction.DOWN_RIGHT.coord, Coord(1, 1))

    def test_repr(self):
        """Test the string representation of Direction instances."""
        self.assertEqual('Direction.UP_LEFT', repr(Direction.UP_LEFT))
        self.assertEqual('Direction.UP', repr(Direction.UP))
        self.assertEqual('Direction.DOWN_RIGHT', repr(Direction.DOWN_RIGHT))


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
