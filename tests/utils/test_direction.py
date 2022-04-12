import unittest
from itertools import product

from src.utils.angle import Angle
from src.utils.coord import Coord
from src.utils.direction import Direction


class TestDirection(unittest.TestCase):

    def test_sum_of_directions(self):
        theta = Angle(0.0)
        for direction in Direction:
            theta += direction.angle
        self.assertEqual(Angle(180.0), theta)

    def test_sum_of_offsets(self):
        offset = Coord(0, 0)
        for direction in Direction:
            offset += direction.offset
        self.assertEqual(Coord(0, 0), offset)

    def test_pairs(self):
        for direction1, direction2 in product(Direction, Direction):
            if direction1.angle - direction2.angle != Angle(180.0):
                continue
            if (direction1 == Direction.CENTER) or (direction2 == Direction.CENTER):
                continue
            self.assertEqual(Coord(0, 0), direction1.offset + direction2.offset)

    def test_sum_of_directions_by_location(self):
        theta = Angle(0.0)
        for location in Direction.locations():
            direction = Direction.direction(location)
            theta += direction.angle
        self.assertEqual(Angle(180.0), theta)

    def test_chess(self):
        self.assertListEqual(Direction.kings(), Direction.diagonals() + Direction.orthogonals())

    def test_value(self):
        for location in Direction.locations():
            direction = Direction.direction(location)
            self.assertEqual(location, direction.location)

    def test_negative(self):
        self.assertEqual(Direction.UP, - Direction.DOWN)
        self.assertEqual(Direction.UPRIGHT, - Direction.DOWNLEFT)
        self.assertEqual(Direction.RIGHT, - Direction.LEFT)
        self.assertEqual(Direction.DOWNRIGHT, - Direction.UPLEFT)
        self.assertEqual(Direction.DOWN, - Direction.UP)
        self.assertEqual(Direction.DOWNLEFT, - Direction.UPRIGHT)
        self.assertEqual(Direction.LEFT, - Direction.RIGHT)
        self.assertEqual(Direction.UPLEFT, - Direction.DOWNRIGHT)

    def test_parallel(self):
        for direction1, direction2 in product(Direction, Direction):
            if direction1 == direction2:
                self.assertTrue(direction1.parallel(direction2))
            elif direction1 == -direction2:
                self.assertTrue(direction1.parallel(direction2))
            else:
                self.assertFalse(direction1.parallel(direction2))


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
