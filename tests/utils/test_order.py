import unittest

from src.utils.order import Order


class TestOrder(unittest.TestCase):

    def test_create(self):
        self.assertEqual(Order.INCREASING, Order("I"))
        self.assertEqual(Order.DECREASING, Order("D"))
        self.assertEqual(Order.UNORDERED, Order("U"))
        with self.assertRaises(ValueError):
            Order('X')

    def test_valid(self):
        self.assertTrue(Order.valid('I'))
        self.assertTrue(Order.valid('D'))
        self.assertTrue(Order.valid('U'))
        self.assertFalse(Order.valid('X'))

    def test_repr(self):
        self.assertEqual('Order.INCREASING', repr(Order.INCREASING))
        self.assertEqual('Order.DECREASING', repr(Order.DECREASING))
        self.assertEqual('Order.UNORDERED', repr(Order.UNORDERED))

    def test_negate(self):
        self.assertEqual(Order.INCREASING, - Order.DECREASING)
        self.assertEqual(Order.DECREASING, - Order.INCREASING)
        self.assertEqual(Order.UNORDERED, - Order.UNORDERED)


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
