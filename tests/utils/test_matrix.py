import unittest

from src.utils.coord import Coord
from src.utils.matrix import ROTATE_000, ROTATE_090, ROTATE_180, ROTATE_270, FLIP_HORIZONTAL, FLIP_VERTICAL, MatrixException


class TestMatrix(unittest.TestCase):

    def test_rotation_r000(self):
        self.assertEqual(ROTATE_000, ROTATE_000.compose(ROTATE_000))
        self.assertEqual(ROTATE_090, ROTATE_000.compose(ROTATE_090))
        self.assertEqual(ROTATE_180, ROTATE_000.compose(ROTATE_180))
        self.assertEqual(ROTATE_270, ROTATE_000.compose(ROTATE_270))

    def test_rotation_r090(self):
        self.assertEqual(ROTATE_090, ROTATE_090.compose(ROTATE_000))
        self.assertEqual(ROTATE_180, ROTATE_090.compose(ROTATE_090))
        self.assertEqual(ROTATE_270, ROTATE_090.compose(ROTATE_180))
        self.assertEqual(ROTATE_000, ROTATE_090.compose(ROTATE_270))

    def test_rotation_r180(self):
        self.assertEqual(ROTATE_180, ROTATE_180.compose(ROTATE_000))
        self.assertEqual(ROTATE_270, ROTATE_180.compose(ROTATE_090))
        self.assertEqual(ROTATE_000, ROTATE_180.compose(ROTATE_180))
        self.assertEqual(ROTATE_090, ROTATE_180.compose(ROTATE_270))

    def test_rotation_r270(self):
        self.assertEqual(ROTATE_270, ROTATE_270.compose(ROTATE_000))
        self.assertEqual(ROTATE_000, ROTATE_270.compose(ROTATE_090))
        self.assertEqual(ROTATE_090, ROTATE_270.compose(ROTATE_180))
        self.assertEqual(ROTATE_180, ROTATE_270.compose(ROTATE_270))

    def test_flips(self):
        self.assertEqual(ROTATE_000, FLIP_HORIZONTAL.compose(FLIP_HORIZONTAL))
        self.assertEqual(FLIP_HORIZONTAL, FLIP_HORIZONTAL.compose(ROTATE_000))
        self.assertEqual(ROTATE_000, FLIP_VERTICAL.compose(FLIP_VERTICAL))
        self.assertEqual(FLIP_VERTICAL, FLIP_VERTICAL.compose(ROTATE_000))

    def test_transforms(self):
        x = Coord(1, 1)
        self.assertEqual(Coord(1, 1), ROTATE_000.transform(x))
        self.assertEqual(Coord(-1, 1), ROTATE_090.transform(x))
        self.assertEqual(Coord(-1, -1), ROTATE_180.transform(x))
        self.assertEqual(Coord(1, -1), ROTATE_270.transform(x))
        self.assertEqual(Coord(1, -1), FLIP_VERTICAL.transform(x))
        self.assertEqual(Coord(-1, 1), FLIP_HORIZONTAL.transform(x))

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
        self.assertEqual(ROTATE_000, ROTATE_000)
        self.assertNotEqual(ROTATE_000, ROTATE_090)
        with self.assertRaises(MatrixException):
            _ = ROTATE_000 == 'xxxx'

    def test_repr(self):
        self.assertEqual("Matrix('ROTATE_000', 1, 0, 0, 1)", repr(ROTATE_000))
        self.assertEqual("Matrix('ROTATE_090', 0, -1, 1, 0)", repr(ROTATE_090))
        self.assertEqual("Matrix('ROTATE_180', -1, 0, 0, -1)", repr(ROTATE_180))
        self.assertEqual("Matrix('ROTATE_270', 0, 1, -1, 0)", repr(ROTATE_270))
        self.assertEqual("Matrix('FLIP_HORIZONTAL', -1, 0, 0, 1)", repr(FLIP_HORIZONTAL))
        self.assertEqual("Matrix('FLIP_VERTICAL', 1, 0, 0, -1)", repr(FLIP_VERTICAL))


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
