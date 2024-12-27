"""TestOrder."""
import unittest

from src.utils.order import Order


class TestOrder(unittest.TestCase):
    """Test the Order class functionality."""

    def test_create(self):
        """Create an Order instance and verify its value_list."""
        self.assertEqual(Order.increasing, Order("I"))
        self.assertEqual(Order.decreasing, Order("D"))
        self.assertEqual(Order.unordered, Order("U"))
        with self.assertRaises(ValueError):
            Order('X')

    def test_valid(self):
        """Check if the provided order number is valid."""
        self.assertTrue(Order.valid('I'))
        self.assertTrue(Order.valid('D'))
        self.assertTrue(Order.valid('U'))
        self.assertFalse(Order.valid('X'))

    def test_repr(self):
        """Verify the string representation of Order instances."""
        self.assertEqual('Order.increasing', repr(Order.increasing))
        self.assertEqual('Order.decreasing', repr(Order.decreasing))
        self.assertEqual('Order.unordered', repr(Order.unordered))

    def test_negate(self):
        """Negate Order instances and check the results."""
        self.assertEqual(Order.increasing, - Order.decreasing)
        self.assertEqual(Order.decreasing, - Order.increasing)
        self.assertEqual(Order.unordered, - Order.unordered)


if __name__ == '__main__':
    unittest.main()
