import unittest

from src.utils.coord import Coord
from src.utils.matrix import R000, R090, R180, R270, FHOR, FVER, MatrixException


class TestMatrix(unittest.TestCase):

    def test_rotation_r000(self):
        self.assertEqual(R000, R000.compose(R000))
        self.assertEqual(R090, R000.compose(R090))
        self.assertEqual(R180, R000.compose(R180))
        self.assertEqual(R270, R000.compose(R270))

    def test_rotation_r090(self):
        self.assertEqual(R090, R090.compose(R000))
        self.assertEqual(R180, R090.compose(R090))
        self.assertEqual(R270, R090.compose(R180))
        self.assertEqual(R000, R090.compose(R270))

    def test_rotation_r180(self):
        self.assertEqual(R180, R180.compose(R000))
        self.assertEqual(R270, R180.compose(R090))
        self.assertEqual(R000, R180.compose(R180))
        self.assertEqual(R090, R180.compose(R270))

    def test_rotation_r270(self):
        self.assertEqual(R270, R270.compose(R000))
        self.assertEqual(R000, R270.compose(R090))
        self.assertEqual(R090, R270.compose(R180))
        self.assertEqual(R180, R270.compose(R270))

    def test_flips(self):
        self.assertEqual(R000, FHOR.compose(FHOR))
        self.assertEqual(FHOR, FHOR.compose(R000))
        self.assertEqual(R000, FVER.compose(FVER))
        self.assertEqual(FVER, FVER.compose(R000))

    def test_transforms(self):
        x = Coord(1, 1)
        self.assertEqual(Coord(1, 1), R000.transform(x))
        self.assertEqual(Coord(-1, 1), R090.transform(x))
        self.assertEqual(Coord(-1, -1), R180.transform(x))
        self.assertEqual(Coord(1, -1), R270.transform(x))
        self.assertEqual(Coord(1, -1), FVER.transform(x))
        self.assertEqual(Coord(-1, 1), FHOR.transform(x))

    @staticmethod
    def alpha(w: int, x: int, y: int, z: int) -> int:
        if w == 1 and x == 1 and y == 1 and z == 1:
            return 0
        return x

    @staticmethod
    def beta(beta: int, x: int, y: int, z: int) -> int:
        if beta == 1 and x == 1 and y == 1 and z == 1:
            return 0
        return y

    def test_alpha(self):
        self.assertEqual(0, TestMatrix.alpha(0, 0, 0, 1), 'a1')
        self.assertEqual(0, TestMatrix.alpha(0, 0, 1, 1), 'a2')
        self.assertEqual(1, TestMatrix.alpha(0, 1, 0, 1), 'a3')
        self.assertEqual(1, TestMatrix.alpha(0, 1, 1, 1), 'a4')
        self.assertEqual(0, TestMatrix.alpha(1, 0, 0, 1), 'a5')
        self.assertEqual(0, TestMatrix.alpha(1, 0, 1, 1), 'a6')
        self.assertEqual(1, TestMatrix.alpha(1, 1, 0, 1), 'a7')
        self.assertEqual(0, TestMatrix.alpha(1, 1, 1, 1), 'a8')

    def test_beta(self):
        self.assertEqual(0, TestMatrix.beta(0, 0, 0, 1), 'b1')
        self.assertEqual(1, TestMatrix.beta(0, 0, 1, 1), 'b2')
        self.assertEqual(0, TestMatrix.beta(0, 1, 0, 1), 'b3')
        self.assertEqual(1, TestMatrix.beta(0, 1, 1, 1), 'b4')
        self.assertEqual(0, TestMatrix.beta(1, 0, 0, 1), 'b5')
        self.assertEqual(1, TestMatrix.beta(1, 0, 1, 1), 'b6')
        self.assertEqual(0, TestMatrix.beta(1, 1, 0, 1), 'b7')
        self.assertEqual(0, TestMatrix.beta(1, 1, 1, 1), 'b8')

    def test_eq(self):
        self.assertEqual(R000, R000)
        self.assertNotEqual(R000, R090)
        with self.assertRaises(MatrixException):
            _ = R000 == 'xxxx'

    def test_repr(self):
        self.assertEqual("Matrix('R000', 1, 0, 0, 1)", repr(R000))
        self.assertEqual("Matrix('R090', 0, -1, 1, 0)", repr(R090))
        self.assertEqual("Matrix('R180', -1, 0, 0, -1)", repr(R180))
        self.assertEqual("Matrix('R270', 0, 1, -1, 0)", repr(R270))
        self.assertEqual("Matrix('FHOR', -1, 0, 0, 1)", repr(FHOR))
        self.assertEqual("Matrix('FVER', 1, 0, 0, -1)", repr(FVER))


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
