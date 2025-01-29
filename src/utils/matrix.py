"""Matrix for 2x2 transformations."""
from src.utils.coord import Coord


class MatrixError(Exception):
    """Custom exception for errors related to Matrix operations."""


class Matrix:
    """Represents a 2x2 matrix and provides methods to compose, transform, and compare matrices.

    Attributes:
        name (str): The name of the matrix.
        matrix (list[list[int]]): A 2x2 matrix represented as a list of lists.
    """

    def __init__(self, name: str, matrix: list[list[int]]) -> None:
        """Initialize a Matrix with a given name and 2x2 matrix.

        Args:
            name (str): The name of the matrix.
            matrix (list[list[int]]): A 2x2 matrix represented as a list of lists.

        Raises:
            ValueError: If the provided matrix is not 2x2.
        """
        if len(matrix) != 2 or len(matrix[0]) != 2 or len(matrix[1]) != 2:
            raise ValueError('Matrix must be 2x2')
        self.name: str = name
        self.matrix: list[list[int]] = matrix

    def compose(self, other: 'Matrix') -> 'Matrix':
        """Compose this matrix with another matrix using matrix multiplication.

        Args:
            other (Matrix): The matrix to compose with.

        Returns:
            Matrix: The resulting matrix after composition.
        """
        result_matrix = [
            [
                self.matrix[0][0] * other.matrix[0][0] + self.matrix[0][1] * other.matrix[1][0],  # Element [0][0]
                self.matrix[0][0] * other.matrix[0][1] + self.matrix[0][1] * other.matrix[1][1],  # Element [0][1]
            ],
            [
                self.matrix[1][0] * other.matrix[0][0] + self.matrix[1][1] * other.matrix[1][0],  # Element [1][0]
                self.matrix[1][0] * other.matrix[0][1] + self.matrix[1][1] * other.matrix[1][1],  # Element [1][1]
            ],
        ]
        return Matrix(
            f'{self.name} | {other.name}',
            result_matrix,
        )

    def transform(self, other: Coord) -> Coord:
        """Transform a coordinate using this matrix.

        Args:
            other (Coord): The coordinate to be transformed.

        Returns:
            Coord: The resulting transformed coordinate.
        """
        return Coord(
            self.matrix[0][0] * other.row + self.matrix[0][1] * other.column,
            self.matrix[1][0] * other.row + self.matrix[1][1] * other.column,
        )

    def __eq__(self, other: object) -> bool:
        """Compare this matrix to another matrix for equality.

        Args:
            other (object): The object to compare to.

        Returns:
            bool: True if the matrices are equal, False otherwise.

        Raises:
            MatrixError: If the comparison is attempted with a non-matrix object.
        """
        if isinstance(other, Matrix):
            return self.matrix == other.matrix
        raise MatrixError(f'Cannot compare {other.__class__.__name__} with {self.__class__.__name__}')

    def __hash__(self) -> int:
        """Return the hash of the matrix based on its elements.

        Returns:
            int: The hash number for the matrix.
        """
        return hash(tuple(tuple(row) for row in self.matrix))

    def __repr__(self) -> str:
        """Return the string representation of the matrix.

        Returns:
            str: A string representing the matrix object.
        """
        return f'{self.__class__.__name__}({self.name!r}, {self.matrix!r})'


# Predefined matrix transformations
ROTATE000: Matrix = Matrix('ROTATE000', [[1, 0], [0, 1]])
ROTATE090: Matrix = Matrix('ROTATE090', [[0, -1], [1, 0]])
ROTATE180: Matrix = Matrix('ROTATE180', [[-1, 0], [0, -1]])
ROTATE270: Matrix = Matrix('ROTATE270', [[0, 1], [-1, 0]])
FLIP_HORIZONTAL: Matrix = Matrix('FLIP_HORIZONTAL', [[-1, 0], [0, 1]])
FLIP_VERTICAL: Matrix = Matrix('FLIP_VERTICAL', [[1, 0], [0, -1]])

# Rotations, flips, and composed transforms
ROTATIONS: tuple[Matrix, Matrix, Matrix, Matrix] = (ROTATE000, ROTATE090, ROTATE180, ROTATE270)
FLIPS: tuple[Matrix, Matrix, Matrix] = (ROTATE000, FLIP_VERTICAL, FLIP_HORIZONTAL)
TRANSFORMS: tuple[Matrix, ...] = tuple(rotate.compose(flip) for rotate in ROTATIONS for flip in FLIPS)
