"""TestBookKeeping."""
import unittest

from src.board.book_keeping_cell import BookKeepingCell
from src.utils.sudoku_exception import SudokuException


class TestBookKeepingCell(unittest.TestCase):
    """Test suite for the BookKeepingCell class."""

    def test_set_possible(self):
        """Test setting possible values for BookKeepingCell."""
        book = BookKeepingCell(9)
        book.set_possible([2, 4, 5])
        self.assertTrue(book.is_possible(2))
        self.assertFalse(book.is_possible(9))

    def test_set_impossible(self):
        """Test setting impossible values for BookKeepingCell."""
        book = BookKeepingCell(9)
        book.set_impossible([2, 4, 5])
        self.assertTrue(book.is_possible(3))
        self.assertFalse(book.is_possible(2))

    def test_set_odd(self):
        """Test setting only odd values as possible for BookKeepingCell."""
        book = BookKeepingCell(9)
        book.set_odd()
        self.assertTrue(book.is_possible(1))
        self.assertFalse(book.is_possible(2))

    def test_set_even(self):
        """Test setting only even values as possible for BookKeepingCell."""
        book = BookKeepingCell(9)
        book.set_even()
        self.assertFalse(book.is_possible(1))
        self.assertTrue(book.is_possible(2))

    def test_set_minimum(self):
        """Test setting the minimum possible value for BookKeepingCell."""
        book = BookKeepingCell(9)
        book.set_minimum(5)
        self.assertFalse(book.is_possible(1))
        self.assertTrue(book.is_possible(5))
        self.assertTrue(book.is_possible(9))

    def test_set_maximum(self):
        """Test setting the maximum possible value for BookKeepingCell."""
        book = BookKeepingCell(9)
        book.set_maximum(5)
        self.assertTrue(book.is_possible(5))
        self.assertFalse(book.is_possible(9))

    def test_set_range(self):
        """Test setting a range of possible values for BookKeepingCell."""
        book = BookKeepingCell(9)
        book.set_range(3, 6)
        self.assertFalse(book.is_possible(1))
        self.assertTrue(book.is_possible(5))
        self.assertFalse(book.is_possible(9))

    def test_fixed(self):
        """Test whether the BookKeepingCell is fixed (only one possible value)."""
        book = BookKeepingCell(9)
        self.assertFalse(book.fixed())
        book.set_possible([1])
        self.assertTrue(book.fixed())

    def test_len(self):
        """Test the length of BookKeepingCell based on possible values."""
        book = BookKeepingCell(9)
        self.assertEqual(len(book), 9)
        book.set_range(3, 6)
        self.assertEqual(len(book), 4)
        book.set_possible([5])
        self.assertEqual(len(book), 1)
        book.set_impossible([5])
        self.assertEqual(len(book), 0)

    def test_str(self):
        """Test the string representation of the BookKeepingCell object."""
        book = BookKeepingCell(9)
        self.assertEqual("123456789", str(book))
        book.set_range(3, 6)
        self.assertEqual("  3456   ", str(book))

    def test_repr(self):
        """Test the representation of the BookKeepingCell object."""
        book = BookKeepingCell(9)
        self.assertEqual("BookKeepingCell(9)", repr(book))

    def test_and(self):
        """Test the 'and' operation between two BookKeepingCell objects."""
        book1 = BookKeepingCell(9)
        book1.set_range(1, 5)
        book2 = BookKeepingCell(9)
        book2.set_range(5, 9)
        expected = BookKeepingCell(9)
        expected.set_possible([5])
        self.assertEqual(expected, book1 & book2)

    def test_or(self):
        """Test the 'or' operation between two BookKeepingCell objects."""
        book1 = BookKeepingCell(9)
        book1.set_range(4, 5)
        book2 = BookKeepingCell(9)
        book2.set_range(5, 6)
        expected = BookKeepingCell(9)
        expected.set_possible([4, 5, 6])
        self.assertEqual(expected, book1 | book2)

    def test_not(self):
        """Test the 'not' operation for BookKeepingCell."""
        book = BookKeepingCell(9)
        book.set_range(5, 9)
        expected = BookKeepingCell(9)
        expected.set_range(1, 4)
        self.assertEqual(expected, ~book)

    def test_eq(self):
        """Test equality comparison between BookKeepingCell objects."""
        book1 = BookKeepingCell(9)
        book1.set_range(5, 9)
        book2 = BookKeepingCell(9)
        book2.set_range(5, 9)
        book3 = BookKeepingCell(9)
        book3.set_range(4, 9)
        self.assertEqual(book1, book2)
        self.assertNotEqual(book1, book3)
        self.assertNotEqual(book2, book3)

    def test_invalid_digit_access(self):
        """Test accessing invalid digits in BookKeepingCell."""
        book = BookKeepingCell(9)
        with self.assertRaises(SudokuException):
            _ = book[0]
        with self.assertRaises(SudokuException):
            _ = book[10]
        with self.assertRaises(SudokuException):
            book[0] = True

    def test_unique(self):
        """Test whether the BookKeepingCell object represents a unique value."""
        book = BookKeepingCell(9)
        self.assertFalse(book.is_unique())
        book.set_minimum(5)
        self.assertFalse(book.is_unique())
        book.set_maximum(5)
        self.assertTrue(book.is_unique())

    def test_invalid_other_for_operations(self):
        """Test passing invalid objects to logical operations."""
        book = BookKeepingCell(9)
        with self.assertRaises(SudokuException):
            _ = book & "invalid"
        with self.assertRaises(SudokuException):
            _ = book | "invalid"
        with self.assertRaises(SudokuException):
            _ = book == "invalid"

    def test_large_bookkeeping(self):
        """Test behavior with a large maximum_digit value."""
        book = BookKeepingCell(1000)
        self.assertEqual(len(book), 1000)
        book.set_range(500, 600)
        self.assertEqual(len(book), 101)


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
