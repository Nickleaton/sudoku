import unittest

from src.utils.coord import Coord
from src.utils.coord_list import CoordList
from src.utils.vector import Vector
from src.utils.vector_list import VectorList, VectorListException


class TestVectorList(unittest.TestCase):

    def setUp(self) -> None:
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
        self.coords = CoordList(
            [
                Coord(1, 2),
                Coord(2, 3),
                Coord(4, 4),
            ]
        )

    def test_equality(self):
        self.assertEqual(self.vectors1, self.vectors1)
        self.assertNotEqual(self.vectors1, self.vectors2)
        self.assertNotEqual(self.vectors1, self.vectors3)
        with self.assertRaises(VectorListException):
            _ = self.vectors1 == "bad"

    def test_find(self):
        self.assertTrue(self.vectors1.find(Coord(1, 2)))
        self.assertTrue(self.vectors1.find(Coord(4, 4)))
        self.assertFalse(self.vectors1.find(Coord(5, 5)))

    def test_contains(self):
        self.assertTrue(Vector(Coord(1, 2), Coord(2, 3)) in self.vectors1)
        self.assertTrue(Vector(Coord(2, 3), Coord(4, 4)) in self.vectors1)
        self.assertTrue(Vector(Coord(4, 4), Coord(1, 2)) in self.vectors1)
        self.assertFalse(Vector(Coord(4, 4), Coord(5, 5)) in self.vectors1)

    def test_coords(self):
        self.assertEqual(self.coords, self.vectors1.coords)

    def test_repr(self):
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


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
