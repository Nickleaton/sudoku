import unittest

from src.utils.angle import Angle, AngleException


class TestAngle(unittest.TestCase):

    def test_angle(self):
        theta = Angle(0.0)
        self.assertEqual(Angle(0.0), theta)

        theta = Angle(360.0)
        self.assertEqual(Angle(0.0), theta)

        theta = Angle(-180.0)
        self.assertEqual(Angle(180.0), theta)

    def test_add(self):
        theta = Angle(45.0)
        self.assertEqual(Angle(90.0), theta + theta)

    def test_sub(self):
        theta = Angle(45.0)
        self.assertEqual(Angle(0.0), theta - theta)

    def test_mul(self):
        theta = Angle(45.0)
        self.assertEqual(Angle(90.0), theta * 2.0)

    def test_opposite(self):
        theta = Angle(10)
        self.assertEqual(Angle(190.0), theta.opposite)

    def test_transform(self):
        theta = Angle(10.0)
        self.assertEqual("rotate(10.0)", theta.transform)
        theta = Angle(0.0)
        self.assertEqual("", theta.transform)

    def test_repr(self):
        theta = Angle(10.0)
        self.assertEqual("Angle(10.0)", str(theta))

    def test_compare(self):
        theta = Angle(10.0)
        beta = Angle(20.0)
        self.assertEqual(theta, theta)
        self.assertNotEqual(theta, beta)
        self.assertLess(theta, beta)
        self.assertLessEqual(theta, theta)
        self.assertGreater(beta, theta)
        with self.assertRaises(AngleException):
            _ = theta == "xxx"
        with self.assertRaises(AngleException):
            _ = theta < "xxx"
        with self.assertRaises(AngleException):
            _ = theta <= "xxx"


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
