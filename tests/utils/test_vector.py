import unittest

from src.utils.coord import Coord
from src.utils.direction import Direction
from src.utils.vector import Vector


class TestLine(unittest.TestCase):

    def setUp(self) -> None:
        self.line_one = Vector(Coord(0, 0), Coord(1, 0))
        self.line_two = Vector(Coord(1, 0), Coord(2, 0))
        self.line_three = Vector(Coord(1, 0), Coord(1, 1))
        self.line_four = Vector(Coord(2, 2), Coord(2, 4))
        self.line_five = Vector(Coord(0, 0), Coord(-1, 0))
        self.zero = Vector(Coord(2, 2), Coord(2, 2))
        self.merged = Vector(Coord(0, 0), Coord(2, 0))

    def test_negative(self):
        self.assertEqual(self.line_one.direction, self.line_two.direction)

    def test_equal(self):
        self.assertEqual(self.line_one, self.line_one)
        self.assertNotEqual(self.line_one, self.line_two)
        self.assertNotEqual(self.line_one, self.line_three)
        self.assertNotEqual(self.line_one, self.line_four)

        self.assertNotEqual(self.line_two, self.line_one)
        self.assertEqual(self.line_two, self.line_two)
        self.assertNotEqual(self.line_two, self.line_three)
        self.assertNotEqual(self.line_two, self.line_four)

        self.assertNotEqual(self.line_three, self.line_one)
        self.assertNotEqual(self.line_three, self.line_two)
        self.assertEqual(self.line_three, self.line_three)
        self.assertNotEqual(self.line_three, self.line_four)

        self.assertNotEqual(self.line_four, self.line_one)
        self.assertNotEqual(self.line_four, self.line_two)
        self.assertNotEqual(self.line_four, self.line_three)
        self.assertEqual(self.line_four, self.line_four)

    def test_mergeable(self):
        self.assertTrue(self.line_one.mergeable(self.line_one))
        self.assertTrue(self.line_one.mergeable(self.line_two))
        self.assertFalse(self.line_one.mergeable(self.line_three))
        self.assertFalse(self.line_one.mergeable(self.line_four))

        self.assertTrue(self.line_two.mergeable(self.line_one))
        self.assertTrue(self.line_two.mergeable(self.line_two))
        self.assertFalse(self.line_two.mergeable(self.line_three))
        self.assertFalse(self.line_two.mergeable(self.line_four))

        self.assertFalse(self.line_three.mergeable(self.line_one))
        self.assertFalse(self.line_three.mergeable(self.line_two))
        self.assertTrue(self.line_three.mergeable(self.line_three))
        self.assertFalse(self.line_three.mergeable(self.line_four))

        self.assertFalse(self.line_four.mergeable(self.line_one))
        self.assertFalse(self.line_four.mergeable(self.line_two))
        self.assertFalse(self.line_four.mergeable(self.line_three))
        self.assertTrue(self.line_four.mergeable(self.line_four))

    def test_mergable_other_direction(self):
        self.assertTrue(self.line_one.mergeable(-self.line_one))
        self.assertTrue(self.line_one.mergeable(-self.line_two))
        self.assertFalse(self.line_one.mergeable(-self.line_three))
        self.assertFalse(self.line_one.mergeable(-self.line_four))

        self.assertTrue(self.line_two.mergeable(-self.line_one))
        self.assertTrue(self.line_two.mergeable(-self.line_two))
        self.assertFalse(self.line_two.mergeable(-self.line_three))
        self.assertFalse(self.line_two.mergeable(-self.line_four))

        self.assertFalse(self.line_three.mergeable(-self.line_one))
        self.assertFalse(self.line_three.mergeable(-self.line_two))
        self.assertTrue(self.line_three.mergeable(-self.line_three))
        self.assertFalse(self.line_three.mergeable(-self.line_four))

        self.assertFalse(self.line_four.mergeable(-self.line_one))
        self.assertFalse(self.line_four.mergeable(-self.line_two))
        self.assertFalse(self.line_four.mergeable(-self.line_three))
        self.assertTrue(self.line_four.mergeable(-self.line_four))

    def test_repr(self):
        self.assertEqual('Vector(Coord(0, 0), Coord(1, 0))', repr(self.line_one))
        self.assertEqual('Vector(Coord(1, 0), Coord(2, 0))', repr(self.line_two))
        self.assertEqual('Vector(Coord(1, 0), Coord(1, 1))', repr(self.line_three))
        self.assertEqual('Vector(Coord(2, 2), Coord(2, 4))', repr(self.line_four))

    def test_direction(self):
        self.assertEqual(Direction.CENTER, self.zero.direction)
        self.assertEqual(Direction.UP, self.line_one.direction)
        self.assertEqual(Direction.DOWN, -self.line_one.direction)
        self.assertEqual(Direction.LEFT, self.line_three.direction)
        self.assertEqual(Direction.RIGHT, -self.line_three.direction)

    def test_merge(self):
        self.assertEqual(self.merged, self.line_one.merge(self.line_two))
        self.assertEqual(self.merged, self.line_two.merge(self.line_one))
        self.assertEqual(self.merged, self.line_one.merge(-self.line_two))
        self.assertEqual(self.merged, -self.line_two.merge(self.line_one))
        self.assertEqual(self.line_one, self.line_one.merge(self.line_one))
        self.assertEqual(self.line_one, self.line_one.merge(-self.line_one))
        self.assertEqual(Vector(Coord(1, 0), Coord(-1, 0)), self.line_one.merge(self.line_five))
        with self.assertRaises(Exception):
            _ = self.line_one.merge(self.line_four)

    def test_add(self):
        v1 = Vector(Coord(1, 1), Coord(2, 1))
        v2 = Vector(Coord(2, 2), Coord(2, 0))
        self.assertEqual(Vector(Coord(3, 3), Coord(4, 1)), v1 + v2)
        c = Coord(2, 2)
        self.assertEqual(Vector(Coord(3, 3), Coord(4, 3)), v1 + c)
        with self.assertRaises(Exception):
            _ = v1 + "x"

    def test_comparison(self):
        v1 = Vector(Coord(1, 1), Coord(2, 1))
        v2 = Vector(Coord(2, 2), Coord(2, 0))
        v3 = Vector(Coord(1, 1), Coord(2, 0))
        self.assertTrue(v1 < v2)
        self.assertFalse(v2 < v1)
        self.assertTrue(v1 < v2)
        self.assertTrue(v2 > v1)
        self.assertTrue(v1 <= v1)
        self.assertTrue(v1 <= v2)
        self.assertFalse(v2 <= v1)
        self.assertFalse(v2 <= v1)


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
