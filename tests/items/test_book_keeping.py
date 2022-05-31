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

    def test_and(self):
        book1 = BookKeeping(9)
        book1.set_range(1, 5)
        book2 = BookKeeping(9)
        book2.set_range(5, 9)
        expected = BookKeeping(9)
        expected.set_possible([5])
        self.assertEqual(expected, book1 & book2)

    def test_or(self):
        book1 = BookKeeping(9)
        book1.set_range(4, 5)
        book2 = BookKeeping(9)
        book2.set_range(5, 6)
        expected = BookKeeping(9)
        expected.set_possible([4, 5, 6])
        self.assertEqual(expected, book1 | book2)

    def test_not(self):
        book = BookKeeping(9)
        book.set_range(5, 9)
        expected = BookKeeping(9)
        expected.set_range(1, 4)
        self.assertEqual(expected, ~book)

    def test_eq(self):
        book1 = BookKeeping(9)
        book1.set_range(5, 9)
        book2 = BookKeeping(9)
        book2.set_range(5, 9)
        book3 = BookKeeping(9)
        book3.set_range(4, 9)
        self.assertEqual(book1, book2)
        self.assertNotEqual(book1, book3)
        self.assertNotEqual(book2, book3)


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
