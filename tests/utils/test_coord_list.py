import unittest

from src.utils.coord import Coord
from src.utils.coord_list import CoordList, CoordListException


class TestCoordList(unittest.TestCase):

    def setUp(self) -> None:
        self.coords1 = CoordList(
            [
                Coord(1, 2),
                Coord(2, 3),
                Coord(4, 5)
            ]
        )
        self.coords2 = CoordList(
            [
                Coord(1, 2),
                Coord(2, 3),
                Coord(4, 7)
            ]
        )
        self.coords3 = CoordList(
            [
                Coord(1, 2),
                Coord(2, 3),
            ]
        )

    def test_iteration(self):
        i = 0
        for _ in self.coords1:
            i += 1
        self.assertEqual(i, len(self.coords1))

    def test_contains(self):
        self.assertTrue(Coord(1, 2) in self.coords1)
        self.assertTrue(Coord(2, 3) in self.coords1)
        self.assertTrue(Coord(4, 5) in self.coords1)
        self.assertFalse(Coord(0, 0) in self.coords1)

    def test_equality(self):
        self.assertEqual(self.coords1, self.coords1)
        self.assertNotEqual(self.coords1, self.coords2)
        self.assertNotEqual(self.coords1, self.coords3)
        with self.assertRaises(CoordListException):
            _ = self.coords1 == "xxx"

    def test_len(self):
        self.assertEqual(3, len(self.coords1))

    def test_repr(self):
        res = (
            "CoordList"
            "("
            "["
            "Coord(1, 2), "
            "Coord(2, 3), "
            "Coord(4, 5)"
            "]"
            ")"
        )
        self.assertEqual(res, repr(self.coords1))


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
