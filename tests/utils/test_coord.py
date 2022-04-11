import unittest

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
        a = Coord(1, 2)
        b = Coord(2, 1)
        c = Coord(1, 3)
        self.assertEqual(a, a)
        self.assertNotEqual(a, b)
        self.assertLess(a, b)
        self.assertLess(a, c)
        self.assertLess(c, b)
        self.assertGreater(b, a)
        self.assertFalse(b < a)


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
