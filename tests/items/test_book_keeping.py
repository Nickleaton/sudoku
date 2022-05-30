import unittest

from src.items.book_keeping import BookKeeping


class TestBookKeeping(unittest.TestCase):

    def test_set_possible(self):
        book = BookKeeping(9)
        book.set_possible([2, 4, 5])
        self.assertTrue(book.is_possible(2))
        self.assertFalse(book.is_possible(9))

    def test_set_impossible(self):
        book = BookKeeping(9)
        book.set_impossible([2, 4, 5])
        self.assertTrue(book.is_possible(3))
        self.assertFalse(book.is_possible(2))

    def test_set_odd(self):
        book = BookKeeping(9)
        book.set_odd()
        self.assertTrue(book.is_possible(1))
        self.assertFalse(book.is_possible(2))

    def test_set_even(self):
        book = BookKeeping(9)
        book.set_even()
        self.assertFalse(book.is_possible(1))
        self.assertTrue(book.is_possible(2))

    def test_set_minimum(self):
        book = BookKeeping(9)
        book.set_minimum(5)
        self.assertFalse(book.is_possible(1))
        self.assertTrue(book.is_possible(5))
        self.assertTrue(book.is_possible(9))

    def test_set_maximum(self):
        book = BookKeeping(9)
        book.set_maximum(5)
        self.assertTrue(book.is_possible(5))
        self.assertFalse(book.is_possible(9))

    def test_set_range(self):
        book = BookKeeping(9)
        book.set_range(3, 6)
        self.assertFalse(book.is_possible(1))
        self.assertTrue(book.is_possible(5))
        self.assertFalse(book.is_possible(9))

    def test_fixed(self):
        book = BookKeeping(9)
        self.assertFalse(book.fixed())
        book.set_possible([1])
        self.assertTrue(book.fixed())

    def test_str(self):
        book = BookKeeping(9)
        self.assertEqual("123456789", str(book))
        book.set_range(3, 6)
        self.assertEqual("  3456   ", str(book))

    def test_repr(self):
        book = BookKeeping(9)
        self.assertEqual("BookKeeping(9)", repr(book))


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
