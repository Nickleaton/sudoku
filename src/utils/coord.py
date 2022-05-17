from typing import List

from src.utils.point import Point


class CoordException(Exception):
    pass


class Coord:

    def __init__(self, row: float, column: float) -> object:
        self.row = row
        self.column = column

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({repr(self.row)}, {repr(self.column)})"

    def __add__(self, other: 'Coord') -> 'Coord':
        return Coord(self.row + other.row, self.column + other.column)

    def __sub__(self, other: 'Coord') -> 'Coord':
        return Coord(self.row - other.row, self.column - other.column)

    def __mul__(self, other: object) -> 'Coord':
        if isinstance(other, Coord):
            return Coord(self.row * other.row, self.column * other.column)
        if isinstance(other, float):
            return Coord(self.row * other, self.column * other)
        if isinstance(other, int):
            return Coord(self.row * other, self.column * other)
        raise CoordException(f"Multiply not supported for Coord and {type(other)}")

    def __truediv__(self, other: float | int) -> 'Coord':
        return Coord(self.row / other, self.column / other)

    def __neg__(self) -> 'Coord':
        return Coord(-self.row, -self.column)

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Coord):
            return (self.row == other.row) and (self.column == other.column)
        raise CoordException(f"Cannot compare {object.__class__.__name__} with {self.__class__.__name__}")

    def __lt__(self, other: object) -> bool:
        if isinstance(other, Coord):
            if self.row < other.row:
                return True
            if self.row == other.row:
                return self.column < other.column
            return False
        raise CoordException(f"Cannot compare {object.__class__.__name__} with {self.__class__.__name__}")

    @staticmethod
    def validate(yaml) -> List[str]:
        result = []
        if not isinstance(yaml, list):
            result.append(f"Expecting list, got {yaml!r}")
            return result
        if len(yaml) != 2:
            result.append("expecting row, column")
        if not isinstance(yaml[0], int):
            result.append("row not int")
        if not isinstance(yaml[1], int):
            result.append("column not int")
        return result

    @property
    def transform(self) -> str:
        return self.point.transform

    @staticmethod
    def middle(a: 'Coord', b: 'Coord') -> 'Coord':
        return Coord(
            (a.row + b.row) / 2,
            (a.column + b.column) / 2
        )

    @property
    def point(self) -> Point:
        return Point(self.column * 100, self.row * 100)

    @property
    def top_left(self) -> 'Coord':
        return Coord(int(self.row), int(self.column))

    @property
    def center(self) -> 'Coord':
        return self.top_left + Coord(0.5, 0.5)

    @property
    def bottom_right(self) -> 'Coord':
        return self.top_left + Coord(1, 1)

    @property
    def bottom_left(self) -> 'Coord':
        return self.top_left + Coord(1, 0)

    @property
    def top_right(self) -> 'Coord':
        return self.top_left + Coord(0, 1)

    @staticmethod
    def create_from_int(row_column: int) -> 'Coord':
        r, c = divmod(row_column, 10)
        return Coord(r, c)
