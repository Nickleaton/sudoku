"""TestMatrix."""
import unittest

from src.utils.coord import Coord
from src.utils.matrix import FLIP_HORIZONTAL, FLIP_VERTICAL, Matrix, MatrixError, ROTATE000, ROTATE090, ROTATE180, \
    ROTATE270


class TestMatrix(unittest.TestCase):
    """Test matrix transformations and related operations."""

    def test_rotation_r000(self):
        """Test rotations for 0 degree rotation."""
        self.assertEqual(ROTATE000, ROTATE000.compose(ROTATE000))
        self.assertEqual(ROTATE090, ROTATE000.compose(ROTATE090))
        self.assertEqual(ROTATE180, ROTATE000.compose(ROTATE180))
        self.assertEqual(ROTATE270, ROTATE000.compose(ROTATE270))

    def test_rotation_r090(self):
        """Test rotations for 090 degree rotation."""
        self.assertEqual(ROTATE090, ROTATE090.compose(ROTATE000))
        self.assertEqual(ROTATE180, ROTATE090.compose(ROTATE090))
        self.assertEqual(ROTATE270, ROTATE090.compose(ROTATE180))
        self.assertEqual(ROTATE000, ROTATE090.compose(ROTATE270))

    def test_rotation_r180(self):
        """Test rotations for 180 degree rotation."""
        self.assertEqual(ROTATE180, ROTATE180.compose(ROTATE000))
        self.assertEqual(ROTATE270, ROTATE180.compose(ROTATE090))
        self.assertEqual(ROTATE000, ROTATE180.compose(ROTATE180))
        self.assertEqual(ROTATE090, ROTATE180.compose(ROTATE270))

    def test_rotation_r270(self):
        """Test rotations for 270 degree rotation."""
        self.assertEqual(ROTATE270, ROTATE270.compose(ROTATE000))
        self.assertEqual(ROTATE000, ROTATE270.compose(ROTATE090))
        self.assertEqual(ROTATE090, ROTATE270.compose(ROTATE180))
        self.assertEqual(ROTATE180, ROTATE270.compose(ROTATE270))

    def test_flips(self):
        """Test flips (horizontal and vertical)."""
        self.assertEqual(ROTATE000, FLIP_HORIZONTAL.compose(FLIP_HORIZONTAL))
        self.assertEqual(FLIP_HORIZONTAL, FLIP_HORIZONTAL.compose(ROTATE000))
        self.assertEqual(ROTATE000, FLIP_VERTICAL.compose(FLIP_VERTICAL))
        self.assertEqual(FLIP_VERTICAL, FLIP_VERTICAL.compose(ROTATE000))

    def test_transforms(self):
        """Test transformations on coordinates."""
        x = Coord(1, 1)
        self.assertEqual(Coord(1, 1), ROTATE000.transform(x))
        self.assertEqual(Coord(-1, 1), ROTATE090.transform(x))
        self.assertEqual(Coord(-1, -1), ROTATE180.transform(x))
        self.assertEqual(Coord(1, -1), ROTATE270.transform(x))
        self.assertEqual(Coord(1, -1), FLIP_VERTICAL.transform(x))
        self.assertEqual(Coord(-1, 1), FLIP_HORIZONTAL.transform(x))

    def test_matrix_hash(self):
        """Test hash functionality for matrices."""
        matrix1 = Matrix('matrix1', ((1, 2), (3, 4)))
        matrix2 = Matrix('matrix2', ((1, 2), (3, 4)))
        matrix3 = Matrix('matrix3', ((4, 3), (2, 1)))

        # Test that two identical matrices have the same hash
        self.assertEqual(hash(matrix1), hash(matrix2))

        # Test that two different matrices have different hashes
        self.assertNotEqual(hash(matrix1), hash(matrix3))

    def test_valid_matrix(self):
        """Test that a valid 2x2 matrix is correctly initialized."""
        matrix = Matrix("ValidMatrix", ((1, 2), (3, 4)))
        self.assertEqual(matrix.name, "ValidMatrix")
        self.assertEqual(matrix.matrix, ((1, 2), (3, 4)))

    def test_invalid_matrix_size(self):
        """Test that invalid matrix sizes raise a ValueError."""
        with self.assertRaises(ValueError):
            Matrix("TooSmall", ((1, 2),))  # type: ignore

        with self.assertRaises(ValueError):
            Matrix("TooLarge", ((1, 2, 3), (4, 5, 6)))  # type: ignore

        with self.assertRaises(ValueError):
            Matrix("NotSquare", ((1, 2), (3,)))  # type: ignore

        with self.assertRaises(ValueError):
            Matrix("Empty", ())  # type: ignore

    @staticmethod
    def alpha(w: int, x: int, y: int, z: int) -> int:
        """Return start number based on the alpha transformation."""
        if w == 1 and x == 1 and y == 1 and z == 1:
            return 0
        return x

    @staticmethod
    def beta(beta: int, x: int, y: int, z: int) -> int:
        """Return start number based on the beta transformation."""
        if beta == 1 and x == 1 and y == 1 and z == 1:
            return 0
        return y

    def test_alpha(self):
        """Test the alpha transformation."""
        self.assertEqual(0, TestMatrix.alpha(0, 0, 0, 1), 'a1')
        self.assertEqual(0, TestMatrix.alpha(0, 0, 1, 1), 'a2')
        self.assertEqual(1, TestMatrix.alpha(0, 1, 0, 1), 'a3')
        self.assertEqual(1, TestMatrix.alpha(0, 1, 1, 1), 'a4')
        self.assertEqual(0, TestMatrix.alpha(1, 0, 0, 1), 'a5')
        self.assertEqual(0, TestMatrix.alpha(1, 0, 1, 1), 'a6')
        self.assertEqual(1, TestMatrix.alpha(1, 1, 0, 1), 'a7')
        self.assertEqual(0, TestMatrix.alpha(1, 1, 1, 1), 'a8')

    def test_beta(self):
        """Test the beta transformation."""
        self.assertEqual(0, TestMatrix.beta(0, 0, 0, 1), 'b1')
        self.assertEqual(1, TestMatrix.beta(0, 0, 1, 1), 'b2')
        self.assertEqual(0, TestMatrix.beta(0, 1, 0, 1), 'b3')
        self.assertEqual(1, TestMatrix.beta(0, 1, 1, 1), 'b4')
        self.assertEqual(0, TestMatrix.beta(1, 0, 0, 1), 'b5')
        self.assertEqual(1, TestMatrix.beta(1, 0, 1, 1), 'b6')
        self.assertEqual(0, TestMatrix.beta(1, 1, 0, 1), 'b7')
        self.assertEqual(0, TestMatrix.beta(1, 1, 1, 1), 'b8')

    def test_eq(self):
        """Test equality comparisons for matrix transformations."""
        self.assertEqual(ROTATE000, ROTATE000)
        self.assertNotEqual(ROTATE000, ROTATE090)
        with self.assertRaises(MatrixError):
            _ = ROTATE000 == 'xxxx'

    def test_repr(self):
        """Test the string representation of matrix transformations."""
        self.assertEqual("Matrix('ROTATE000', ((1, 0), (0, 1)))", repr(ROTATE000))
        self.assertEqual("Matrix('ROTATE090', ((0, -1), (1, 0)))", repr(ROTATE090))
        self.assertEqual("Matrix('ROTATE180', ((-1, 0), (0, -1)))", repr(ROTATE180))
        self.assertEqual("Matrix('ROTATE270', ((0, 1), (-1, 0)))", repr(ROTATE270))
        self.assertEqual("Matrix('FLIP_HORIZONTAL', ((-1, 0), (0, 1)))", repr(FLIP_HORIZONTAL))
        self.assertEqual("Matrix('FLIP_VERTICAL', ((1, 0), (0, -1)))", repr(FLIP_VERTICAL))


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
