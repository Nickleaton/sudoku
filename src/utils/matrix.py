"""Matrix for 2x2 transformations."""
from src.utils.coord import Coord
from src.utils.sudoku_exception import SudokuException


class MatrixException(SudokuException):
    """Custom exception for errors related to Matrix operations."""


class Matrix:
    """
    Represents a 2x2 matrix and provides methods to compose, transform, and compare matrices.

    Attributes:
        name (str): The name of the matrix.
        a (int): The element in the first row, first column of the matrix.
        b (int): The element in the first row, second column of the matrix.
        c (int): The element in the second row, first column of the matrix.
        d (int): The element in the second row, second column of the matrix.
    """

    # pylint: disable=too-many-positional-arguments
    def __init__(self, name: str, a: int, b: int, c: int, d: int):
        """
        Initialize a Matrix with given parameters.

        Args:
            name (str): The name of the matrix.
            a (int): The element in the first row, first column.
            b (int): The element in the first row, second column.
            c (int): The element in the second row, first column.
            d (int): The element in the second row, second column.
        """
        self.name = name
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def compose(self, other: 'Matrix') -> 'Matrix':
        """
        Compose this matrix with another matrix using matrix multiplication.

        Args:
            other (Matrix): The matrix to compose with.

        Returns:
            Matrix: The resulting matrix after composition.
        """
        return Matrix(
            f"{self.name} | {other.name}",
            self.a * other.a + self.b * other.c,
            self.a * other.b + self.b * other.d,
            self.c * other.a + self.d * other.c,
            self.c * other.b + self.d * other.d
        )

    def transform(self, other: Coord) -> Coord:
        """
        Transform a coordinate using this matrix.

        Args:
            other (Coord): The coordinate to be transformed.

        Returns:
            Coord: The resulting transformed coordinate.
        """
        return Coord(
            self.a * other.row + self.b * other.column,
            self.c * other.row + self.d * other.column
        )

    def __eq__(self, other: object) -> bool:
        """
        Compare this matrix to another matrix for equality.

        Args:
            other (object): The object to compare to.

        Returns:
            bool: True if the matrices are equal, False otherwise.

        Raises:
            MatrixException: If the comparison is attempted with a non-matrix object.
        """
        if isinstance(other, Matrix):
            return (self.a == other.a) and (self.b == other.b) and (self.c == other.c) and (self.d == other.d)
        raise MatrixException(f"Cannot compare {object.__class__.__name__} with {self.__class__.__name__}")

    def __hash__(self) -> int:
        """
        Return a hash of the matrix based on its elements.

        Returns:
            int: The hash value for the matrix.
        """
        return hash((self.a, self.b, self.c, self.d))

    def __repr__(self) -> str:
        """
        Return a string representation of the matrix.

        Returns:
            str: A string representing the matrix object.
        """
        return f"{self.__class__.__name__}('{self.name}', {self.a}, {self.b}, {self.c}, {self.d})"


# Predefined matrix transformations
ROTATE_000 = Matrix('ROTATE_000', 1, 0, 0, 1)
ROTATE_090 = Matrix('ROTATE_090', 0, -1, 1, 0)
ROTATE_180 = Matrix('ROTATE_180', -1, 0, 0, -1)
ROTATE_270 = Matrix('ROTATE_270', 0, 1, -1, 0)
FLIP_HORIZONTAL = Matrix('FLIP_HORIZONTAL', -1, 0, 0, 1)
FLIP_VERTICAL = Matrix('FLIP_VERTICAL', 1, 0, 0, -1)

# Rotations, flips, and composed transforms
ROTATIONS = (ROTATE_000, ROTATE_090, ROTATE_180, ROTATE_270)
FLIPS = (ROTATE_000, FLIP_VERTICAL, FLIP_HORIZONTAL)
TRANSFORMS = (r.compose(f) for r in ROTATIONS for f in FLIPS)
