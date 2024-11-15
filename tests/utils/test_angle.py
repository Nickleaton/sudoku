"""TestAngle."""
import math
import unittest

from src.utils.angle import Angle, AngleException


class TestAngle(unittest.TestCase):
    """Test the Angle class."""

    def test_angle(self):
        """Test initialization and normalization of angles."""
        theta = Angle(0.0)
        self.assertEqual(Angle(0.0), theta)

        theta = Angle(360.0)
        self.assertEqual(Angle(0.0), theta)

        theta = Angle(-180.0)
        self.assertEqual(Angle(180.0), theta)

        # Test angles greater than 360 and negative angles
        theta = Angle(720.0)
        self.assertEqual(Angle(0.0), theta)

        theta = Angle(359.9)
        self.assertEqual(Angle(359.9), theta)

        theta = Angle(-359.9)
        self.assertEqual(Angle(0.1), theta)

    def test_add(self):
        """Test angle addition and normalization."""
        theta = Angle(45.0)
        self.assertEqual(Angle(90.0), theta + theta)

        # Test addition with normalization (360 degrees)
        theta = Angle(350.0)
        self.assertEqual(Angle(30.0), theta + Angle(40.0))

    def test_sub(self):
        """Test angle subtraction and normalization."""
        theta = Angle(45.0)
        self.assertEqual(Angle(0.0), theta - theta)

        # Test subtraction with normalization (negative angle wraparound)
        theta = Angle(10.0)
        self.assertEqual(Angle(350.0), theta - Angle(20.0))

    def test_mul(self):
        """Test angle multiplication and wraparound."""
        theta = Angle(45.0)
        self.assertEqual(Angle(90.0), theta * 2.0)

        # Test multiplication with wraparound
        theta = Angle(180.0)
        self.assertEqual(Angle(360.0), theta * 2.0)  # Should normalize to 0

    def test_opposite(self):
        """Test opposite angle (should add 180 degrees)."""
        theta = Angle(10)
        self.assertEqual(Angle(190.0), theta.opposite)

        # Test opposite with normalization (angle > 180 should wraparound)
        theta = Angle(180)
        self.assertEqual(Angle(0.0), theta.opposite)

    def test_transform(self):
        """Test transform string generation."""
        theta = Angle(10.0)
        self.assertEqual("rotate(10.0)", theta.transform)
        theta = Angle(0.0)
        self.assertEqual("", theta.transform)

        # Test transform with large angle (should still be correct)
        theta = Angle(370.0)
        self.assertEqual("rotate(10.0)", theta.transform)

    def test_repr(self):
        """Test the __repr__ method."""
        theta = Angle(10.0)
        self.assertEqual("Angle(10.0)", str(theta))

    def test_compare(self):
        """Test comparisons (==, !=, <, <=, >, >=)."""
        theta = Angle(10.0)
        beta = Angle(20.0)
        self.assertEqual(theta, theta)
        self.assertNotEqual(theta, beta)
        self.assertLess(theta, beta)
        self.assertLessEqual(theta, theta)
        self.assertGreater(beta, theta)

        # Test invalid comparison
        with self.assertRaises(AngleException):
            _ = theta == "xxx"
        with self.assertRaises(AngleException):
            _ = theta < "xxx"
        with self.assertRaises(AngleException):
            _ = theta <= "xxx"

    def test_edge_case(self):
        """Test very small and very large angles (should normalize correctly)."""
        # Test very small angle close to 0
        theta = Angle(0.0001)
        self.assertEqual(Angle(0.0001), theta)

        # Test very large angle (should normalize correctly)
        theta = Angle(359.9999)
        self.assertEqual(Angle(359.9999), theta)

    def test_degrees_property(self):
        """Test getting and setting degrees and normalization."""
        theta = Angle(45.0)
        self.assertEqual(theta.degrees, 45.0)

        # Set angle using degrees
        theta.degrees = 90.0
        self.assertEqual(theta.degrees, 90.0)

        # Test normalization
        theta.degrees = 360.0
        self.assertEqual(theta.degrees, 0.0)

        # Test negative angle normalization
        theta.degrees = -45.0
        self.assertEqual(theta.degrees, 315.0)

    def test_radians_property(self):
        """Test getting and setting radians and normalization."""
        theta = Angle(45.0)
        self.assertAlmostEqual(theta.radians, math.radians(45.0), places=6)

        # Set angle using radians
        theta.radians = math.radians(90.0)
        self.assertAlmostEqual(theta.radians, math.radians(90.0), places=6)

        # Test normalization by setting radians
        theta.radians = math.radians(720.0)
        self.assertAlmostEqual(theta.radians, 0.0, places=6)

        # Test negative angle normalization by setting radians
        theta.radians = math.radians(-45.0)
        self.assertAlmostEqual(theta.radians, math.radians(315.0), places=6)


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
