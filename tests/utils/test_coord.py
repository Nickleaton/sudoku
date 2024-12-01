"""TestCoord."""
import unittest
from typing import Any

from src.utils.coord import Coord, CoordException


class TestCoord(unittest.TestCase):
    """Test the Coord class."""

    def test_transform(self):
        """Test the transform method of the Coord class."""
        cell = Coord(1, 2)
        self.assertEqual("translate(200, 100)", cell.transform)

    def test_cell(self):
        """Test the row and column attributes of the Coord class."""
        cell = Coord(1, 2)
        self.assertEqual(1, cell.row)
        self.assertEqual(2, cell.column)

    def test_add(self):
        """Test adding two Coord instances."""
        cell = Coord(1, 2) + Coord(2, 3)
        self.assertEqual(3, cell.row)
        self.assertEqual(5, cell.column)

    def test_sub(self):
        """Test subtracting two Coord instances."""
        cell = Coord(2, 3) - Coord(1, 2)
        self.assertEqual(1, cell.row)
        self.assertEqual(1, cell.column)

    def test_mul(self):
        """Test multiplying a Coord instance by a scalar or another Coord."""
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
        """Test dividing a Coord instance by a scalar."""
        cell = Coord(2, 4) / 2.0
        self.assertEqual(1, cell.row)
        self.assertEqual(2, cell.column)

    def test_neg(self):
        """Test negating a Coord instance."""
        cell = -Coord(1, -2)
        self.assertEqual(-1, cell.row)
        self.assertEqual(2, cell.column)

    def test_eq(self):
        """Test equality comparison between two Coord instances."""
        self.assertTrue(Coord(1, 2) == Coord(1, 2))

    def test_ne(self):
        """Test inequality comparison between two Coord instances."""
        self.assertTrue(Coord(2, 2) != Coord(1, 2))

    def test_lt(self):
        """Test less-than comparison between two Coord instances."""
        self.assertTrue(Coord(1, 2) < Coord(2, 2))
        self.assertTrue(Coord(1, 2) < Coord(1, 3))
        self.assertFalse(Coord(1, 2) < Coord(1, 2))

    def test_middle(self):
        """Test finding the middle point between two Coord instances."""
        coord = Coord.middle(Coord(1, 1), Coord(1, 2))
        self.assertEqual(1, coord.row)
        self.assertEqual(1.5, coord.column)

    def test_point(self):
        """Test the point representation of a Coord instance."""
        cell = Coord(1, 2)
        self.assertEqual(100, cell.point.y)
        self.assertEqual(200, cell.point.x)

    def test_center(self):
        """Test the center point of a Coord instance."""
        cell = Coord(1, 1)
        self.assertEqual(1.5, cell.center.row)
        self.assertEqual(1.5, cell.center.column)

    def test_corners(self):
        """Test the corner points of a Coord instance."""
        cell = Coord(1, 1)
        self.assertEqual(1, cell.top_right.row)
        self.assertEqual(2, cell.top_right.column)
        self.assertEqual(1, cell.top_left.row)
        self.assertEqual(1, cell.top_left.column)
        self.assertEqual(2, cell.bottom_right.row)
        self.assertEqual(2, cell.bottom_right.column)
        self.assertEqual(2, cell.bottom_left.row)
        self.assertEqual(1, cell.bottom_left.column)

    def test_repr(self):
        """Test the string representation of a Coord instance."""
        cell = Coord(1, 2)
        self.assertEqual("Coord(1, 2)", str(cell))

    def test_compare(self):
        """Test comparison operators for Coord instances."""
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
        """Validate the given YAML and return the number of errors."""
        errors = Coord.validate(yaml)
        return len(errors)

    def test_validate(self):
        """Test the validation of various YAML input_types."""
        self.assertEqual(0, TestCoord.check_yaml([1, 1]))
        self.assertEqual(1, TestCoord.check_yaml([1, 2, 3]))
        self.assertEqual(1, TestCoord.check_yaml("xxx"))
        self.assertEqual(1, TestCoord.check_yaml(['x', 1]))
        self.assertEqual(1, TestCoord.check_yaml([1, 'y']))


if __name__ == '__main__':
    unittest.main()
