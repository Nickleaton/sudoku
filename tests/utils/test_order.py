import unittest

from src.utils.order import Order, OrderException


class TestOrder(unittest.TestCase):

    def test_create(self):
        self.assertEqual(Order.INCREASING, Order.create("I"))
        self.assertEqual(Order.DECREASING, Order.create("D"))
        with self.assertRaises(OrderException):
            Order.create('X')

    def test_valid(self):
        self.assertTrue(Order.valid('I'))
        self.assertTrue(Order.valid('D'))
        self.assertFalse(Order.valid('X'))

    def test_repr(self):
        self.assertEqual('Order.INCREASING', repr(Order.INCREASING))
        self.assertEqual('Order.DECREASING', repr(Order.DECREASING))

    def test_negate(self):
        self.assertEqual(Order.INCREASING, - Order.DECREASING)
        self.assertEqual(Order.DECREASING, - Order.INCREASING)


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
