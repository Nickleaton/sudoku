from src.utils.coord import Coord
from src.utils.direction import Direction


class VectorException(Exception):
    pass


class Vector:

    def __init__(self, start: Coord, end: Coord):
        self.start = start
        self.end = end

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Vector):
            if self.start == other.start:
                return self.end == other.end
            if self.start == other.end:
                return self.end == other.start
            return False
        raise VectorException(f"Cannot compare {object.__class__.__name__} with {self.__class__.__name__}")

    def __lt__(self, other: 'Vector') -> bool:
        if self.start < other.start:
            return True
        if self.start > other.start:
            return False
        return self.end < other.end

    def __le__(self, other: 'Vector') -> bool:
        if self == other:
            return True
        return self < other

    def __neg__(self) -> 'Vector':
        return Vector(self.end, self.start)

    def __add__(self, other: object) -> 'Vector':
        if isinstance(other, Coord):
            return Vector(self.start + other, self.end + other)
        if isinstance(other, Vector):
            return Vector(self.start + other.start, self.end + other.end)
        raise VectorException(f'Add not supported for Vector and {other.__class__.__name__}')

    @property
    def direction(self) -> Direction:  # pylint: disable=too-many-return-statements
        # Only for orthogonal
        if self.start.row == self.end.row:
            if self.start.column < self.end.column:
                return Direction.LEFT
            if self.start.column > self.end.column:
                return Direction.RIGHT
            return Direction.CENTER
        if self.start.column == self.end.column:
            if self.start.row < self.end.row:
                return Direction.UP
            if self.start.row > self.end.row:
                return Direction.DOWN
            return Direction.CENTER  # pragma: no cover
        return Direction.CENTER  # pragma: no cover

    def mergeable(self, other: 'Vector') -> bool:
        if self.start == other.start:
            return self.direction.parallel(other.direction)
        if self.start == other.end:
            return self.direction.parallel(other.direction)
        if self.end == other.start:
            return self.direction.parallel(other.direction)
        if self.end == other.end:
            return self.direction.parallel(other.direction)
        return False

    def merge(self, other: 'Vector') -> 'Vector':
        assert self.mergeable(other)
        if self == other:
            return self
        if self.start == other.start:
            return Vector(self.end, other.end)
        if self.start == other.end:
            return Vector(self.end, other.start)
        if self.end == other.start:
            return Vector(self.start, other.end)
        if self.end == other.end:
            return Vector(self.start, other.start)
        raise Exception("Non mergeable lines")  # pragma: no cover

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({repr(self.start)}, {repr(self.end)})"
