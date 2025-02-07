"""TestVector."""
import unittest

from src.utils.coord import Coord
from src.utils.moves import Moves
from src.utils.vector import Vector, VectorError


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
        """Test negation of vectors."""
        self.assertEqual(-self.line_one, Vector(Coord(1, 0), Coord(0, 0)))
        self.assertEqual(-self.line_two, Vector(Coord(2, 0), Coord(1, 0)))

    def test_equal(self):
        """Test equality and inequality of vectors."""
        self.assertEqual(self.line_one, self.line_one)
        self.assertNotEqual(self.line_one, self.line_two)
        self.assertNotEqual(self.line_one, self.line_three)
        self.assertEqual(self.line_four, self.line_four)
        with self.assertRaises(VectorError):
            _ = self.zero == "invalid"

    def test_mergeable(self):
        """Test if vectors are mergeable."""
        self.assertTrue(self.line_one.mergeable(self.line_two))
        self.assertFalse(self.line_one.mergeable(self.line_three))
        self.assertTrue(self.line_two.mergeable(self.line_one))
        self.assertFalse(self.line_four.mergeable(self.line_three))

    def test_mergeable_opposite_direction(self):
        """Test mergeable vectors in the opposite direction."""
        self.assertTrue(self.line_one.mergeable(-self.line_two))
        self.assertFalse(self.line_three.mergeable(-self.line_four))

    def test_repr(self):
        """Test the string representation of vectors."""
        self.assertEqual(repr(self.line_one), 'Vector(Coord(0, 0), Coord(1, 0))')
        self.assertEqual(repr(self.line_two), 'Vector(Coord(1, 0), Coord(2, 0))')

    def test_is_horizontal(self):
        """Test if the vector is horizontal."""
        self.assertTrue(self.line_one.is_horizontal)
        self.assertFalse(self.line_three.is_horizontal)
        self.assertFalse(self.line_four.is_horizontal)

    def test_is_vertical(self):
        """Test if the vector is vertical."""
        self.assertFalse(self.line_one.is_vertical)
        self.assertTrue(self.line_three.is_vertical)
        self.assertTrue(self.line_four.is_vertical)

    def test_direction(self):
        """Test the overall direction of vectors."""
        self.assertEqual(self.line_one.direction, Moves.down)
        self.assertEqual(self.line_three.direction, Moves.right)
        self.assertEqual(-self.line_one.direction, Moves.up)
        self.assertEqual(self.zero.direction, Moves.center)

    def test_merge(self):
        """Test merging of vectors with various conditions."""

        test_data = (
            # (name, vector1_start, vector1_end, vector2_start, vector2_end, expected_result, should_raise)
            (
                "Test Case 1: Same start, parallel",
                Coord(0, 0), Coord(2, 2),
                Coord(0, 0), Coord(3, 3),
                Vector(Coord(2, 2), Coord(3, 3)),
                False
            ),
            (
                "Test Case 2: Same start, not parallel",
                Coord(0, 0), Coord(2, 2),
                Coord(0, 0), Coord(1, 2),
                None,
                True
            ),
            (
                "Test Case 3: Start of self == end of other, parallel",
                Coord(0, 0), Coord(2, 2),
                Coord(3, 3), Coord(0, 0),
                Vector(Coord(2, 2), Coord(3, 3)),
                False
            ),
            (
                "Test Case 4: Start of self == end of other, not parallel",
                Coord(0, 0), Coord(2, 2),
                Coord(2, 2), Coord(3, 1),
                None,
                True
            ),
            (
                "Test Case 5: End of self == start of other, parallel",
                Coord(0, 0), Coord(2, 2),
                Coord(2, 2), Coord(3, 3),
                Vector(Coord(0, 0), Coord(3, 3)),
                False
            ),
            (
                "Test Case 6: End of self == start of other, not parallel",
                Coord(0, 0), Coord(2, 2),
                Coord(2, 2), Coord(4, 1),
                None,
                True
            ),
            (
                "Test Case 7: Same end, parallel",
                Coord(0, 0), Coord(2, 2),
                Coord(1, 1), Coord(2, 2),
                Vector(Coord(0, 0), Coord(1, 1)),
                False
            ),
            (
                "Test Case 8: Same end, not parallel",
                Coord(0, 0), Coord(2, 2),
                Coord(1, 1), Coord(2, 3),
                None,
                True
            ),
        )

        for name, start1, end1, start2, end2, expected, should_raise in test_data:
            vector1 = Vector(start1, end1)
            vector2 = Vector(start2, end2)
            with self.subTest(name=name):
                if should_raise:
                    with self.assertRaises(VectorError):
                        vector1.merge(vector2)
                else:
                    result = vector1.merge(vector2)
                    self.assertEqual(result, expected)

        # Test that merging a vector with itself doesn't modify it
        with self.subTest(name="Test merge with same vector"):
            self.assertEqual(self.line_one, self.line_one.merge(self.line_one))

        # Test for vectors that cannot merge
        with self.subTest(name="Test merge that raises VectorError"):
            with self.assertRaises(VectorError):
                _ = self.line_one.merge(self.line_four)

    def test_add(self):
        """Test adding vectors and coordinates."""
        vector1 = Vector(Coord(1, 1), Coord(2, 1))
        vector2 = Vector(Coord(2, 2), Coord(3, 2))
        self.assertEqual(vector1 + vector2, Vector(Coord(3, 3), Coord(5, 3)))
        coord = Coord(1, 1)
        self.assertEqual(vector1 + coord, Vector(Coord(2, 2), Coord(3, 2)))
        with self.assertRaises(VectorError):
            _ = vector1 + "invalid"

    def test_comparison(self):
        """Test comparison operators for vectors."""
        vector1 = Vector(Coord(1, 1), Coord(2, 1))
        vector2 = Vector(Coord(2, 2), Coord(3, 2))
        self.assertTrue(vector1 < vector2)
        self.assertFalse(vector2 < vector1)
        self.assertTrue(vector1 <= vector2)
        # test with same vector, to make sure test is handled
        # noqa: R0124
        self.assertTrue(vector1 <= vector1)  # pylint: disable=comparison-with-itself
        self.assertFalse(vector2 <= vector1)
        with self.assertRaises(VectorError):
            _ = self.zero < "invalid"  # type: ignore

    def test_vector_direction_center(self):
        """Test direction of vector when start and end points are the same."""
        vector = Vector(Coord(1, 1), Coord(1, 1))
        self.assertEqual(vector.direction, Moves.center)


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
