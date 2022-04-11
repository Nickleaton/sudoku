from typing import Union, List

from src.utils.coord import Coord
from src.utils.direction import Direction


class Vector:

    def __init__(self, start: Coord, end: Coord):
        self.start = start
        self.end = end

    def __eq__(self, other: 'Vector') -> bool:
        if self.start == other.start:
            return self.end == other.end
        if self.start == other.end:
            return self.end == other.start
        return False

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

    def __add__(self, other: Union[Coord, 'Vector']) -> 'Vector':
        if isinstance(other, Coord):
            return Vector(self.start + other, self.end + other)
        if isinstance(other, Vector):
            return Vector(self.start + other.start, self.end + other.end)
        raise Exception(f'Add not supported for Vector and {other.__class__.__name__}')

    @property
    def direction(self) -> Direction:
        # Only for orthogonal
        if self.start.row == self.end.row:
            if self.start.column < self.end.column:
                return Direction.LEFT
            elif self.start.column > self.end.column:
                return Direction.RIGHT
            else:
                return Direction.CENTER
        elif self.start.column == self.end.column:
            if self.start.row < self.end.row:
                return Direction.UP
            elif self.start.row > self.end.row:
                return Direction.DOWN
            else:
                return Direction.CENTER  # pragma: no cover

    def mergeable(self, other: 'Vector') -> bool:
        if self.start == other.start:
            return self.direction.parallel(other.direction)
        elif self.start == other.end:
            return self.direction.parallel(other.direction)
        elif self.end == other.start:
            return self.direction.parallel(other.direction)
        elif self.end == other.end:
            return self.direction.parallel(other.direction)
        else:
            return False

    def merge(self, other: 'Vector') -> 'Vector':
        assert (self.mergeable(other))
        if self == other:
            return self
        if self.start == other.start:
            return Vector(self.end, other.end)
        elif self.start == other.end:
            return Vector(self.end, other.start)
        elif self.end == other.start:
            return Vector(self.start, other.end)
        elif self.end == other.end:
            return Vector(self.start, other.start)
        else:
            raise Exception("Non mergeable lines")  # pragma: no cover



    def __repr__(self):
        return f"{self.__class__.__name__}({repr(self.start)}, {repr(self.end)})"
