"""TestPoint."""
import unittest

from src.utils.point import Point


class TestPoint(unittest.TestCase):
    """Test the Point class functionality."""

    def test_point(self):
        """Create a Point instance and verify its coordinates."""
        point = Point(1, 2)
        self.assertEqual(1, point.x)
        self.assertEqual(2, point.y)

    def test_add(self):
        """Add two Point instances and check the result."""
        point = Point(1, 2) + Point(2, 3)
        self.assertEqual(3, point.x)
        self.assertEqual(5, point.y)

    def test_sub(self):
        """Subtract two Point instances and check the result."""
        point = Point(2, 3) - Point(1, 2)
        self.assertEqual(1, point.x)
        self.assertEqual(1, point.y)

    def test_mul(self):
        """Multiply a Point instance by a scalar and check the result."""
        point = Point(1, 2) * 2.0
        self.assertEqual(2, point.x)
        self.assertEqual(4, point.y)

    def test_truediv(self):
        """Divide a Point instance by a scalar and check the result."""
        point = Point(2, 4) / 2.0
        self.assertEqual(1, point.x)
        self.assertEqual(2, point.y)

    def test_neg(self):
        """Negate a Point instance and check the result."""
        point = -Point(1, -2)
        self.assertEqual(-1, point.x)
        self.assertEqual(2, point.y)

    def test_magnitude(self):
        """Calculate and verify the magnitude of a Point instance."""
        point = Point(3, 4)
        self.assertEqual(5, point.magnitude)

    def test_transform(self):
        """Apply a transformation to a Point instance and check the result."""
        point = Point(1, 2)
        self.assertEqual("translate(1, 2)", point.transform)

    def test_coordinates(self):
        """Get the coordinates of a Point instance and verify the result."""
        point = Point(1, 2)
        self.assertEqual((1, 2), point.coordinates)

    def test_repr(self):
        """Verify the string representation of a Point instance."""
        point = Point(1, 2)
        self.assertEqual("Point(1, 2)", str(point))


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
