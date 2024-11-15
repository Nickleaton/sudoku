"""TestBookKeeping."""
import unittest

from src.items.book_keeping import BookKeeping


class TestBookKeeping(unittest.TestCase):
    """Test suite for the BookKeeping class."""

    def test_set_possible(self):
        """Test setting possible values for BookKeeping."""
        book = BookKeeping(9)
        book.set_possible([2, 4, 5])
        self.assertTrue(book.is_possible(2))
        self.assertFalse(book.is_possible(9))

    def test_set_impossible(self):
        """Test setting impossible values for BookKeeping."""
        book = BookKeeping(9)
        book.set_impossible([2, 4, 5])
        self.assertTrue(book.is_possible(3))
        self.assertFalse(book.is_possible(2))

    def test_set_odd(self):
        """Test setting only odd values as possible for BookKeeping."""
        book = BookKeeping(9)
        book.set_odd()
        self.assertTrue(book.is_possible(1))
        self.assertFalse(book.is_possible(2))

    def test_set_even(self):
        """Test setting only even values as possible for BookKeeping."""
        book = BookKeeping(9)
        book.set_even()
        self.assertFalse(book.is_possible(1))
        self.assertTrue(book.is_possible(2))

    def test_set_minimum(self):
        """Test setting the minimum possible value for BookKeeping."""
        book = BookKeeping(9)
        book.set_minimum(5)
        self.assertFalse(book.is_possible(1))
        self.assertTrue(book.is_possible(5))
        self.assertTrue(book.is_possible(9))

    def test_set_maximum(self):
        """Test setting the maximum possible value for BookKeeping."""
        book = BookKeeping(9)
        book.set_maximum(5)
        self.assertTrue(book.is_possible(5))
        self.assertFalse(book.is_possible(9))

    def test_set_range(self):
        """Test setting a range of possible values for BookKeeping."""
        book = BookKeeping(9)
        book.set_range(3, 6)
        self.assertFalse(book.is_possible(1))
        self.assertTrue(book.is_possible(5))
        self.assertFalse(book.is_possible(9))

    def test_fixed(self):
        """Test whether the BookKeeping is fixed (only one possible value)."""
        book = BookKeeping(9)
        self.assertFalse(book.fixed())
        book.set_possible([1])
        self.assertTrue(book.fixed())

    def test_str(self):
        """Test the string representation of the BookKeeping object."""
        book = BookKeeping(9)
        self.assertEqual("123456789", str(book))
        book.set_range(3, 6)
        self.assertEqual("  3456   ", str(book))

    def test_repr(self):
        """Test the representation of the BookKeeping object."""
        book = BookKeeping(9)
        self.assertEqual("BookKeeping(9)", repr(book))

    def test_and(self):
        """Test the 'and' operation between two BookKeeping objects."""
        book1 = BookKeeping(9)
        book1.set_range(1, 5)
        book2 = BookKeeping(9)
        book2.set_range(5, 9)
        expected = BookKeeping(9)
        expected.set_possible([5])
        self.assertEqual(expected, book1 & book2)

    def test_or(self):
        """Test the 'or' operation between two BookKeeping objects."""
        book1 = BookKeeping(9)
        book1.set_range(4, 5)
        book2 = BookKeeping(9)
        book2.set_range(5, 6)
        expected = BookKeeping(9)
        expected.set_possible([4, 5, 6])
        self.assertEqual(expected, book1 | book2)

    def test_not(self):
        """Test the 'not' operation for BookKeeping."""
        book = BookKeeping(9)
        book.set_range(5, 9)
        expected = BookKeeping(9)
        expected.set_range(1, 4)
        self.assertEqual(expected, ~book)

    def test_eq(self):
        """Test equality comparison between BookKeeping objects."""
        book1 = BookKeeping(9)
        book1.set_range(5, 9)
        book2 = BookKeeping(9)
        book2.set_range(5, 9)
        book3 = BookKeeping(9)
        book3.set_range(4, 9)
        self.assertEqual(book1, book2)
        self.assertNotEqual(book1, book3)
        self.assertNotEqual(book2, book3)

    def test_unique(self):
        """Test whether the BookKeeping object represents a unique value."""
        book = BookKeeping(9)
        self.assertFalse(book.is_unique())
        book.set_minimum(5)
        self.assertFalse(book.is_unique())
        book.set_maximum(5)
        self.assertTrue(book.is_unique())


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
