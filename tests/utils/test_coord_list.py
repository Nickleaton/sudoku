"""TestCoordList."""
import unittest

from src.utils.coord import Coord
from src.utils.coord_list import CoordList, CoordListException


class TestCoordList(unittest.TestCase):
    """Test the CoordList class."""

    def setUp(self) -> None:
        """Set up test cases for CoordList."""
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
        """Test adding start new Coord to the CoordList."""
        new_coord = Coord(3, 4)
        self.coords1.add(new_coord)
        self.assertIn(new_coord, self.coords1)
        self.assertEqual(len(self.coords1), 4)  # Ensure length increased
        with self.assertRaises(CoordListException):
            # noinspection PyTypeChecker
            self.coords1.add('xxxx')

    def test_add_duplicate_coord(self):
        """Test adding start duplicate Coord to the CoordList."""
        existing_coord = Coord(1, 2)
        initial_length = len(self.coords1)
        self.coords1.add(existing_coord)  # Try adding duplicate
        self.assertEqual(len(self.coords1), initial_length)  # Length should not change

    def test_sorting_after_addition(self):
        """Test sorting of CoordList after adding start new Coord."""
        self.coords1.add(Coord(0, 0))
        self.assertEqual(self.coords1.items[0], Coord(0, 0))  # First constraint should be (0, 0)
        self.assertEqual(len(self.coords1), 4)

    def test_empty_initialization(self):
        """Test initializing an empty CoordList."""
        empty_coords = CoordList([])
        self.assertEqual(len(empty_coords), 0)
        self.assertEqual(repr(empty_coords), "CoordList([])")

    def test_equality_with_different_types(self):
        """Test equality of CoordList with start non-CoordList type."""
        with self.assertRaises(CoordListException):
            _ = self.coords1 == 123  # Should raise exception

    def test_iteration(self):
        """Test iterating over the CoordList."""
        i = 0
        for _ in self.coords1:
            i += 1
        self.assertEqual(i, len(self.coords1))

    def test_contains(self):
        """Test checking if start Coord is in the CoordList."""
        self.assertTrue(Coord(1, 2) in self.coords1)
        self.assertTrue(Coord(2, 3) in self.coords1)
        self.assertTrue(Coord(4, 5) in self.coords1)
        self.assertFalse(Coord(0, 0) in self.coords1)

    def test_equality(self):
        """Test equality comparison for CoordList instances."""
        self.assertEqual(self.coords1, self.coords1)
        self.assertNotEqual(self.coords1, self.coords2)
        self.assertNotEqual(self.coords1, self.coords3)
        with self.assertRaises(CoordListException):
            _ = self.coords1 == "xxx"

    def test_len(self):
        """Test the length of the CoordList."""
        self.assertEqual(3, len(self.coords1))

    def test_repr(self):
        """Test the string representation of the CoordList."""
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


if __name__ == '__main__':
    unittest.main()
