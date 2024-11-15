"""TestVector."""

import unittest
from src.utils.coord import Coord
from src.utils.direction import Direction
from src.utils.vector import Vector, VectorException


class TestVector(unittest.TestCase):
    """Test the Vector class."""

    def setUp(self) -> None:
        """Set up test cases with sample vectors."""
        self.line_one = Vector(Coord(0, 0), Coord(1, 0))
        self.line_two = Vector(Coord(1, 0), Coord(2, 0))
        self.line_three = Vector(Coord(1, 0), Coord(1, 1))
        self.line_four = Vector(Coord(2, 2), Coord(2, 4))
        self.line_five = Vector(Coord(0, 0), Coord(-1, 0))
        self.zero = Vector(Coord(2, 2), Coord(2, 2))
        self.merged = Vector(Coord(0, 0), Coord(2, 0))

    def test_negative(self):
        """Test equality for vectors with the same direction."""
        self.assertEqual(self.line_one.direction, self.line_two.direction)

    def test_equal(self):
        """Test equality and inequality comparisons for vectors."""
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
        with self.assertRaises(VectorException):
            _ = self.zero == "xxxx"

    def test_vector_lt_invalid_comparison(self):
        """Test invalid comparison for less-than operation."""
        vector1 = Vector(Coord(1, 1), Coord(2, 2))
        with self.assertRaises(VectorException):
            _ = vector1 < "not a vector"

    def test_mergeable(self):
        """Test if vectors are mergeable."""
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
        """Test mergeable vectors in the opposite direction."""
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
        """Test the string representation of vectors."""
        self.assertEqual('Vector(Coord(0, 0), Coord(1, 0))', repr(self.line_one))
        self.assertEqual('Vector(Coord(1, 0), Coord(2, 0))', repr(self.line_two))
        self.assertEqual('Vector(Coord(1, 0), Coord(1, 1))', repr(self.line_three))
        self.assertEqual('Vector(Coord(2, 2), Coord(2, 4))', repr(self.line_four))

    def test_direction(self):
        """Test the direction of vectors."""
        self.assertEqual(Direction.CENTER, self.zero.direction)
        self.assertEqual(Direction.UP, self.line_one.direction)
        self.assertEqual(Direction.DOWN, -self.line_one.direction)
        self.assertEqual(Direction.LEFT, self.line_three.direction)
        self.assertEqual(Direction.RIGHT, -self.line_three.direction)

    def test_merge(self):
        """Test merging of vectors."""
        self.assertEqual(self.merged, self.line_one.merge(self.line_two))
        self.assertEqual(self.merged, self.line_two.merge(self.line_one))
        self.assertEqual(self.merged, self.line_one.merge(-self.line_two))
        self.assertEqual(self.merged, -self.line_two.merge(self.line_one))
        self.assertEqual(self.line_one, self.line_one.merge(self.line_one))
        self.assertEqual(self.line_one, self.line_one.merge(-self.line_one))
        self.assertEqual(Vector(Coord(1, 0), Coord(-1, 0)), self.line_one.merge(self.line_five))
        with self.assertRaises(VectorException):
            _ = self.line_one.merge(self.line_four)

    def test_add(self):
        """Test adding vectors and coordinates."""
        vector1 = Vector(Coord(1, 1), Coord(2, 1))
        vector2 = Vector(Coord(2, 2), Coord(2, 0))
        self.assertEqual(Vector(Coord(3, 3), Coord(4, 1)), vector1 + vector2)
        coord = Coord(2, 2)
        self.assertEqual(Vector(Coord(3, 3), Coord(4, 3)), vector1 + coord)
        with self.assertRaises(VectorException):
            _ = vector1 + "x"

    def test_comparison(self):
        """Test comparison operators for vectors."""
        vector1 = Vector(Coord(1, 1), Coord(2, 1))
        vector2 = Vector(Coord(2, 2), Coord(2, 0))
        vector3 = Vector(Coord(1, 1), Coord(2, 0))
        vector4 = Vector(Coord(1, 1), Coord(2, 1))
        self.assertTrue(vector1 < vector2)
        self.assertFalse(vector2 < vector1)
        self.assertTrue(vector1 < vector2)
        self.assertTrue(vector2 > vector1)
        self.assertTrue(vector1 <= vector4)
        self.assertTrue(vector1 <= vector2)
        self.assertFalse(vector2 <= vector1)
        self.assertFalse(vector2 <= vector1)
        self.assertFalse(vector1 < vector3)

    def test_vector_direction_center(self):
        """Test direction of vector when start and end points are the same."""
        start = Coord(1, 1)
        end = Coord(1, 1)  # Same as start to trigger CENTER
        vector = Vector(start, end)
        self.assertEqual(
            vector.direction,
            Direction.CENTER,
            "Expected direction to be CENTER for identical start and end coordinates."
        )


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
