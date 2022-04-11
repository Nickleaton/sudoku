from src.utils.coord import Coord


class Matrix:

    def __init__(self, name: str, a: int, b: int, c: int, d: int):
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

    def __eq__(self, other: 'Matrix') -> bool:
        return (self.a == other.a) and (self.b == other.b) and (self.c == other.c) and (self.d == other.d)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.name}', {self.a}, {self.b}, {self.c}, {self.d})"


R000 = Matrix('R000', 1, 0, 0, 1)
R090 = Matrix('R090', 0, -1, 1, 0)
R180 = Matrix('R180', -1, 0, 0, -1)
R270 = Matrix('R270', 0, 1, -1, 0)
FHOR = Matrix('FHOR', -1, 0, 0, 1)
FVER = Matrix('FVER', 1, 0, 0, -1)

ROTATIONS = [R000, R090, R180, R270]
FLIPS = [R000, FVER, FHOR]
TRANSFORMS = [r.compose(f) for r in ROTATIONS for f in FLIPS]
