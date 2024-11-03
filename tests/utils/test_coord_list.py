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

    def test_add_new_coord(self):
        new_coord = Coord(3, 4)
        self.coords1.add(new_coord)
        self.assertIn(new_coord, self.coords1)
        self.assertEqual(len(self.coords1), 4)  # Ensure length increased

    def test_add_duplicate_coord(self):
        existing_coord = Coord(1, 2)
        initial_length = len(self.coords1)
        self.coords1.add(existing_coord)  # Try adding duplicate
        self.assertEqual(len(self.coords1), initial_length)  # Length should not change

    def test_sorting_after_addition(self):
        self.coords1.add(Coord(0, 0))
        self.assertEqual(self.coords1.items[0], Coord(0, 0))  # First item should be (0, 0)
        self.assertEqual(len(self.coords1), 4)

    def test_empty_initialization(self):
        empty_coords = CoordList([])
        self.assertEqual(len(empty_coords), 0)
        self.assertEqual(repr(empty_coords), "CoordList([])")

    def test_equality_with_different_types(self):
        with self.assertRaises(CoordListException):
            _ = self.coords1 == 123  # Should raise exception

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
