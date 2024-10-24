from src.utils.coord import Coord
from src.utils.sudoku_exception import SudokuException


class MatrixException(SudokuException):
    pass


class Matrix:

    def __init__(self, name: str, a: int, b: int, c: int, d: int):  # pylint: disable=too-many-arguments
        self.name = name
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def compose(self, other: 'Matrix') -> 'Matrix':
        return Matrix(
            f"{self.name} | {other.name}",
            self.a * other.a + self.b * other.c,
            self.a * other.b + self.b * other.d,
            self.c * other.a + self.d * other.c,
            self.c * other.b + self.d * other.d
        )

    def transform(self, other: Coord) -> Coord:
        return Coord(
            self.a * other.row + self.b * other.column,
            self.c * other.row + self.d * other.column
        )

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Matrix):
            return (self.a == other.a) and (self.b == other.b) and (self.c == other.c) and (self.d == other.d)
        raise MatrixException(f"Cannot compare {object.__class__.__name__} with {self.__class__.__name__}")

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.name}', {self.a}, {self.b}, {self.c}, {self.d})"


ROTATE_000 = Matrix('ROTATE_000', 1, 0, 0, 1)
ROTATE_090 = Matrix('ROTATE_090', 0, -1, 1, 0)
ROTATE_180 = Matrix('ROTATE_180', -1, 0, 0, -1)
ROTATE_270 = Matrix('ROTATE_270', 0, 1, -1, 0)
FLIP_HORIZONTAL = Matrix('FLIP_HORIZONTAL', -1, 0, 0, 1)
FLIP_VERTICAL = Matrix('FLIP_VERTICAL', 1, 0, 0, -1)

ROTATIONS = [ROTATE_000, ROTATE_090, ROTATE_180, ROTATE_270]
FLIPS = [ROTATE_000, FLIP_VERTICAL, FLIP_HORIZONTAL]
TRANSFORMS = [r.compose(f) for r in ROTATIONS for f in FLIPS]
