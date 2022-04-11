import unittest

from src.utils.point import Point


class TestPoint(unittest.TestCase):

    def test_point(self):
        point = Point(1, 2)
        self.assertEqual(1, point.x)
        self.assertEqual(2, point.y)

    def test_add(self):
        point = Point(1, 2) + Point(2, 3)
        self.assertEqual(3, point.x)
        self.assertEqual(5, point.y)

    def test_sub(self):
        point = Point(2, 3) - Point(1, 2)
        self.assertEqual(1, point.x)
        self.assertEqual(1, point.y)

    def test_mul(self):
        point = Point(1, 2) * 2.0
        self.assertEqual(2, point.x)
        self.assertEqual(4, point.y)

    def test_truediv(self):
        point = Point(2, 4) / 2.0
        self.assertEqual(1, point.x)
        self.assertEqual(2, point.y)

    def test_neg(self):
        point = -Point(1, -2)
        self.assertEqual(-1, point.x)
        self.assertEqual(2, point.y)

    def test_magnitude(self):
        point = Point(3, 4)
        self.assertEqual(5, point.magnitude)

    def test_transform(self):
        point = Point(1, 2)
        self.assertEqual("translate(1, 2)", point.transform)

    def test_coordinates(self):
        point = Point(1, 2)
        self.assertEqual((1, 2), point.coordinates)

    def test_repr(self):
        point = Point(1, 2)
        self.assertEqual("Point(1, 2)", str(point))


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
