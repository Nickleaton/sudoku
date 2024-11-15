"""TestDirection."""
import unittest
from itertools import product

from src.utils.angle import Angle
from src.utils.coord import Coord
from src.utils.direction import Direction


class TestDirection(unittest.TestCase):
    """Test the Direction class."""

    def test_sum_of_directions(self):
        """Test the sum of direction angles."""
        theta = Angle(0.0)
        for direction in Direction:
            theta += direction.angle
        self.assertEqual(Angle(180.0), theta)

    def test_sum_of_offsets(self):
        """Test the sum of direction offsets."""
        offset = Coord(0, 0)
        for direction in Direction:
            offset += direction.offset
        self.assertEqual(Coord(0, 0), offset)

    def test_pairs(self):
        """Test pairs of directions with opposite angles."""
        for direction1, direction2 in product(Direction, Direction):
            if direction1.angle - direction2.angle != Angle(180.0):
                continue
            if Direction.CENTER in [direction1, direction2]:
                continue
            self.assertEqual(Coord(0, 0), direction1.offset + direction2.offset)

    def test_sum_of_directions_by_location(self):
        """Test the sum of direction angles by location."""
        theta = Angle(0.0)
        for location in Direction.locations():
            direction = Direction.direction(location)
            theta += direction.angle
        self.assertEqual(Angle(180.0), theta)

    def test_chess(self):
        """Test if kings are the union of diagonals and orthogonals."""
        self.assertListEqual(sorted(Direction.kings()), sorted(Direction.diagonals() + Direction.orthogonals()))

    def test_value(self):
        """Test if direction location matches expected value."""
        for location in Direction.locations():
            direction = Direction.direction(location)
            self.assertEqual(location, direction.location)

    def test_negative(self):
        """Test the negative direction mapping."""
        self.assertEqual(Direction.UP, - Direction.DOWN)
        self.assertEqual(Direction.UP_RIGHT, - Direction.DOWN_LEFT)
        self.assertEqual(Direction.RIGHT, - Direction.LEFT)
        self.assertEqual(Direction.DOWN_RIGHT, - Direction.UP_LEFT)
        self.assertEqual(Direction.DOWN, - Direction.UP)
        self.assertEqual(Direction.DOWN_LEFT, - Direction.UP_RIGHT)
        self.assertEqual(Direction.LEFT, - Direction.RIGHT)
        self.assertEqual(Direction.UP_LEFT, - Direction.DOWN_RIGHT)

    def test_parallel(self):
        """Test if directions are parallel."""
        for direction1, direction2 in product(Direction, Direction):
            if direction1 == direction2:
                self.assertTrue(direction1.parallel(direction2))
            elif direction1 == -direction2:
                self.assertTrue(direction1.parallel(direction2))
            else:
                self.assertFalse(direction1.parallel(direction2))

    def test_orthogonals(self):
        """Test the orthogonal directions."""
        expected_orthogonals = [
            Coord(-1, 0), # LEFT
            Coord(0, 1),   # DOWN
            Coord(1, 0),   # RIGHT
            Coord(0, -1)  # UP
        ]
        self.assertListEqual(Direction.orthogonals(), expected_orthogonals)

    def test_diagonals(self):
        """Test the diagonal directions."""
        expected_diagonals = [
            Coord(-1, -1),  # UP_LEFT
            Coord(-1, 1),   # UP_RIGHT
            Coord(1, 1),    # DOWN_RIGHT
            Coord(1, -1)    # DOWN_LEFT
        ]
        self.assertListEqual(Direction.diagonals(), expected_diagonals)

    def test_kings(self):
        """Test the king movement directions."""
        expected_kings = [
            Coord(-1, -1),  # UP_LEFT
            Coord(-1, 0),   # UP
            Coord(-1, 1),   # UP_RIGHT
            Coord(0, -1),   # LEFT
            Coord(0, 1),    # RIGHT
            Coord(1, -1),   # DOWN_LEFT
            Coord(1, 0),    # DOWN
            Coord(1, 1)     # DOWN_RIGHT
        ]
        self.assertListEqual(Direction.kings(), expected_kings)

    def test_knights(self):
        """Test the knight movement directions."""
        expected_knights = [
            Coord(-1, -2), Coord(1, -2), Coord(-2, -1), Coord(-2, 1),
            Coord(-1, 2), Coord(1, 2), Coord(2, 1), Coord(2, -1)
        ]
        self.assertListEqual(Direction.knights(), expected_knights)

    def test_all_but_center(self):
        """Test all directions except for the center."""
        expected_all_but_center = [
            Coord(-1, -1), Coord(-1, 0), Coord(-1, 1),  # UP_LEFT, UP, UP_RIGHT
            Coord(0, -1), Coord(0, 1),                   # LEFT, RIGHT
            Coord(1, -1), Coord(1, 0), Coord(1, 1)       # DOWN_LEFT, DOWN, DOWN_RIGHT
        ]
        self.assertListEqual(Direction.all_but_center(), expected_all_but_center)

    def test_all(self):
        """Test all directions including center."""
        expected_all = [
            Coord(-1, -1), Coord(-1, 0), Coord(-1, 1),  # UP_LEFT, UP, UP_RIGHT
            Coord(0, -1), Coord(0, 0), Coord(0, 1),     # LEFT, CENTER, RIGHT
            Coord(1, -1), Coord(1, 0), Coord(1, 1)      # DOWN_LEFT, DOWN, DOWN_RIGHT
        ]
        self.assertListEqual(Direction.all(), expected_all)


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
