import unittest
from typing import Any

from src.utils.coord import Coord, CoordException


class TestCoord(unittest.TestCase):

    def test_cell(self):
        cell = Coord(1, 2)
        self.assertEqual(1, cell.row)
        self.assertEqual(2, cell.column)

    def test_add(self):
        cell = Coord(1, 2) + Coord(2, 3)
        self.assertEqual(3, cell.row)
        self.assertEqual(5, cell.column)

    def test_sub(self):
        cell = Coord(2, 3) - Coord(1, 2)
        self.assertEqual(1, cell.row)
        self.assertEqual(1, cell.column)

    def test_mul(self):
        cell = Coord(1, 2) * 2.0
        self.assertEqual(2, cell.row)
        self.assertEqual(4, cell.column)
        cell1 = Coord(1, 2)
        result = cell1 * cell1
        self.assertEqual(1, result.row)
        self.assertEqual(4, result.column)
        with self.assertRaises(CoordException):
            _ = cell1 * "number"

    def test_truediv(self):
        cell = Coord(2, 4) / 2.0
        self.assertEqual(1, cell.row)
        self.assertEqual(2, cell.column)

    def test_neg(self):
        cell = -Coord(1, -2)
        self.assertEqual(-1, cell.row)
        self.assertEqual(2, cell.column)

    def test_eq(self):
        self.assertTrue(Coord(1, 2) == Coord(1, 2))

    def test_ne(self):
        self.assertTrue(Coord(2, 2) != Coord(1, 2))

    def test_lt(self):
        self.assertTrue(Coord(1, 2) < Coord(2, 2))
        self.assertTrue(Coord(1, 2) < Coord(1, 3))
        self.assertFalse(Coord(1, 2) < Coord(1, 2))

    def test_middle(self):
        coord = Coord.middle(Coord(1, 1), Coord(1, 2))
        self.assertEqual(1, coord.row)
        self.assertEqual(1.5, coord.column)

    def test_point(self):
        cell = Coord(1, 2)
        self.assertEqual(100, cell.point.y)
        self.assertEqual(200, cell.point.x)

    def test_center(self):
        cell = Coord(1, 1)
        self.assertEqual(1.5, cell.center.row)
        self.assertEqual(1.5, cell.center.column)

    def test_top_right(self):
        cell = Coord(1, 1)
        self.assertEqual(1, cell.top_right.row)
        self.assertEqual(2, cell.top_right.column)

    def test_top_left(self):
        cell = Coord(1, 1)
        self.assertEqual(1, cell.top_left.row)
        self.assertEqual(1, cell.top_left.column)

    def test_bottom_right(self):
        cell = Coord(1, 1)
        self.assertEqual(2, cell.bottom_right.row)
        self.assertEqual(2, cell.bottom_right.column)

    def test_bottom_left(self):
        cell = Coord(1, 1)
        self.assertEqual(2, cell.bottom_left.row)
        self.assertEqual(1, cell.bottom_left.column)

    def test_repr(self):
        cell = Coord(1, 2)
        self.assertEqual("Coord(1, 2)", str(cell))

    def test_compare(self):
        coord1 = Coord(1, 2)
        coord2 = Coord(2, 1)
        coord3 = Coord(1, 3)
        self.assertEqual(coord1, coord1)
        self.assertNotEqual(coord1, coord2)
        self.assertLess(coord1, coord2)
        self.assertLess(coord1, coord3)
        self.assertLess(coord3, coord2)
        self.assertGreater(coord2, coord1)
        self.assertFalse(coord2 < coord1)
        with self.assertRaises(CoordException):
            _ = coord1 == 'xxx'
        with self.assertRaises(CoordException):
            _ = coord1 < 'xxx'

    @staticmethod
    def check_yaml(yaml: Any) -> int:
        errors = Coord.validate(yaml)
        # print(repr(yaml))
        # print("\n    ".join(errors))
        return len(errors)

    def test_validate(self):
        self.assertEqual(0, TestCoord.check_yaml([1, 1]))
        self.assertEqual(1, TestCoord.check_yaml([1, 2, 3]))
        self.assertEqual(1, TestCoord.check_yaml("xxx"))
        self.assertEqual(1, TestCoord.check_yaml(['x', 1]))
        self.assertEqual(1, TestCoord.check_yaml([1, 'y']))


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
