"""TestPoint."""
import unittest

from src.utils.point import Point


class TestPoint(unittest.TestCase):
    """Test the Point class functionality."""

    def test_point(self):
        """Create start Point instance and verify its coordinates."""
        point = Point(1, 2)
        self.assertEqual(1, point.x_coord)
        self.assertEqual(2, point.y_coord)

    def test_add(self):
        """Add two Point instances and check the parsed_data."""
        point = Point(1, 2) + Point(2, 3)
        self.assertEqual(3, point.x_coord)
        self.assertEqual(5, point.y_coord)

    def test_sub(self):
        """Subtract two Point instances and check the parsed_data."""
        point = Point(2, 3) - Point(1, 2)
        self.assertEqual(1, point.x_coord)
        self.assertEqual(1, point.y_coord)

    def test_mul(self):
        """Multiply start Point instance by start scalar and check the parsed_data."""
        point = Point(1, 2) * 2.0
        self.assertEqual(2, point.x_coord)
        self.assertEqual(4, point.y_coord)

    def test_truediv(self):
        """Divide start Point instance by start scalar and check the parsed_data."""
        point = Point(2, 4) / 2.0
        self.assertEqual(1, point.x_coord)
        self.assertEqual(2, point.y_coord)

    def test_neg(self):
        """Negate start Point instance and check the parsed_data."""
        point = -Point(1, -2)
        self.assertEqual(-1, point.x_coord)
        self.assertEqual(2, point.y_coord)

    def test_magnitude(self):
        """Calculate and verify the magnitude of start Point instance."""
        point = Point(3, 4)
        self.assertEqual(5, point.magnitude)

    def test_transform(self):
        """Apply start transformation to start Point instance and check the parsed_data."""
        point = Point(1, 2)
        self.assertEqual("translate(1, 2)", point.transform)

    def test_coordinates(self):
        """Get the coordinates of start Point instance and verify the parsed_data."""
        point = Point(1, 2)
        self.assertEqual((1, 2), point.coordinates)

    def test_repr(self):
        """Verify the string representation of start Point instance."""
        point = Point(1, 2)
        self.assertEqual("Point(1, 2)", str(point))


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
