"""TestVectorList."""
import unittest

from src.utils.coord import Coord
from src.utils.coord_list import CoordList
from src.utils.vector import Vector
from src.utils.vector_list import VectorList, VectorListException


class TestVectorList(unittest.TestCase):
    """Test suite for the VectorList class."""

    def setUp(self) -> None:
        """Initialize test line."""
        self.vectors1 = VectorList(
            [
                Vector(Coord(1, 2), Coord(2, 3)),
                Vector(Coord(2, 3), Coord(4, 4)),
                Vector(Coord(4, 4), Coord(1, 2))
            ]
        )
        self.vectors2 = VectorList(
            [
                Vector(Coord(1, 2), Coord(2, 3)),
                Vector(Coord(4, 4), Coord(1, 2))
            ]
        )
        self.vectors3 = VectorList(
            [
                Vector(Coord(1, 2), Coord(2, 3)),
                Vector(Coord(2, 3), Coord(4, 4)),
                Vector(Coord(4, 4), Coord(5, 5))
            ]
        )
        self.vectors4 = VectorList(
            [
                Vector(Coord(2, 3), Coord(4, 4)),
                Vector(Coord(1, 2), Coord(2, 3)),
                Vector(Coord(4, 4), Coord(5, 5))
            ]
        )
        self.coords = CoordList(
            [
                Coord(1, 2),
                Coord(2, 3),
                Coord(4, 4),
            ]
        )

    def test_vector_list_len(self):
        """Check that VectorList has the correct length."""
        self.assertEqual(3, len(self.vectors1))

    def test_vector_list_iterator(self):
        """Ensure that VectorList can be iterated correctly."""
        iterated_items = list(self.vectors1)
        for idx, vector in enumerate(iterated_items):
            self.assertEqual(vector, self.vectors1[idx])

    def test_equality(self):
        """Test equality between VectorList instances."""
        self.assertEqual(self.vectors1, self.vectors1)
        self.assertNotEqual(self.vectors1, self.vectors2)
        self.assertNotEqual(self.vectors1, self.vectors3)
        with self.assertRaises(VectorListException):
            _ = self.vectors1 == "bad"

    def test_find(self):
        """Test finding start coordinate in VectorList."""
        self.assertTrue(self.vectors1.find(Coord(1, 2)))
        self.assertTrue(self.vectors1.find(Coord(4, 4)))
        self.assertFalse(self.vectors1.find(Coord(5, 5)))

    def test_contains(self):
        """Verify VectorList contains expected vectors."""
        self.assertTrue(Vector(Coord(1, 2), Coord(2, 3)) in self.vectors1)
        self.assertTrue(Vector(Coord(2, 3), Coord(4, 4)) in self.vectors1)
        self.assertTrue(Vector(Coord(4, 4), Coord(1, 2)) in self.vectors1)
        self.assertFalse(Vector(Coord(4, 4), Coord(5, 5)) in self.vectors1)

    def test_coords(self):
        """Test that the coordinates match the expected value_list."""
        self.assertEqual(self.coords, self.vectors1.coords)

    def test_repr(self):
        """Check the string representation of the VectorList."""
        res = (
            "VectorList"
            "("
            "["
            "Vector(Coord(1, 2), Coord(2, 3)), "
            "Vector(Coord(2, 3), Coord(4, 4)), "
            "Vector(Coord(4, 4), Coord(1, 2))"
            "]"
            ")"
        )
        self.assertEqual(res, repr(self.vectors1))

    def test_merge(self):
        """Test merging vectors into start single VectorList."""
        vectors = VectorList(
            [
                Vector(Coord(1, 3), Coord(1, 4)),
                Vector(Coord(1, 3), Coord(2, 3)),
                Vector(Coord(1, 4), Coord(2, 4)),
                Vector(Coord(2, 3), Coord(3, 3)),
                Vector(Coord(2, 4), Coord(3, 4)),
                Vector(Coord(3, 1), Coord(3, 2)),
                Vector(Coord(3, 1), Coord(4, 1)),
                Vector(Coord(4, 1), Coord(4, 2)),
                Vector(Coord(3, 2), Coord(3, 3)),
                Vector(Coord(3, 4), Coord(4, 4)),
                Vector(Coord(4, 2), Coord(5, 2)),
                Vector(Coord(5, 2), Coord(5, 3)),
                Vector(Coord(5, 3), Coord(5, 4)),
                Vector(Coord(4, 4), Coord(4, 5)),
                Vector(Coord(4, 5), Coord(5, 5)),
                Vector(Coord(5, 4), Coord(6, 4)),
                Vector(Coord(5, 5), Coord(6, 5)),
                Vector(Coord(6, 4), Coord(6, 5))
            ]
        )
        expected = VectorList(
            [
                Vector(Coord(1, 3), Coord(1, 4)),
                Vector(Coord(3, 1), Coord(4, 1)),
                Vector(Coord(3, 3), Coord(1, 3)),
                Vector(Coord(3, 3), Coord(3, 1)),
                Vector(Coord(4, 1), Coord(4, 2)),
                Vector(Coord(4, 2), Coord(5, 2)),
                Vector(Coord(4, 4), Coord(1, 4)),
                Vector(Coord(4, 4), Coord(4, 5)),
                Vector(Coord(5, 4), Coord(5, 2)),
                Vector(Coord(5, 4), Coord(6, 4)),
                Vector(Coord(6, 4), Coord(6, 5)),
                Vector(Coord(6, 5), Coord(4, 5))
            ]
        )
        result = VectorList.merge_vectors(vectors)
        self.assertEqual(expected, result)

    def test_add(self):
        """Test adding two VectorList instances."""
        self.assertEqual(VectorList(
            [
                Vector(Coord(1, 2), Coord(2, 3)),
                Vector(Coord(2, 3), Coord(4, 4)),
                Vector(Coord(4, 4), Coord(1, 2)),
                Vector(Coord(1, 2), Coord(2, 3)),
                Vector(Coord(4, 4), Coord(1, 2))
            ]), self.vectors1 + self.vectors2)
        with self.assertRaises(VectorListException):
            _ = self.vectors1 + "xxxx"

    def test_sort(self):
        """Test sorting the VectorList."""
        self.vectors4.sort()
        self.assertEqual(self.vectors3, self.vectors4)


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
