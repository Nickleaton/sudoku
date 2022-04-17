from enum import Enum
from typing import List

from src.utils.angle import Angle
from src.utils.coord import Coord


class DirectionException(Exception):
    pass


class Direction(Enum):
    UP_LEFT = 1
    UP = 2
    UP_RIGHT = 3
    LEFT = 4
    CENTER = 5
    RIGHT = 6
    DOWN_LEFT = 7
    DOWN = 8
    DOWN_RIGHT = 9

    @staticmethod
    def locations() -> List[int]:
        return [d.value for d in Direction]

    def __neg__(self) -> 'Direction':
        if self == Direction.UP_LEFT:
            return Direction.DOWN_RIGHT
        if self == Direction.UP:
            return Direction.DOWN
        if self == Direction.UP_RIGHT:
            return Direction.DOWN_LEFT
        if self == Direction.LEFT:
            return Direction.RIGHT
        if self == Direction.CENTER:
            return Direction.CENTER
        if self == Direction.RIGHT:
            return Direction.LEFT
        if self == Direction.DOWN_LEFT:
            return Direction.UP_RIGHT
        if self == Direction.DOWN:
            return Direction.UP
        if self == Direction.DOWN_RIGHT:
            return Direction.UP_LEFT
        raise DirectionException('Unknown direction') # pragma: no cover

    @property
    def angle(self) -> Angle:
        if self == Direction.UP_LEFT:
            return Angle(315)
        if self == Direction.UP:
            return Angle(0)
        if self == Direction.UP_RIGHT:
            return Angle(45)
        if self == Direction.LEFT:
            return Angle(270)
        if self == Direction.CENTER:
            return Angle(0)
        if self == Direction.RIGHT:
            return Angle(90)
        if self == Direction.DOWN_LEFT:
            return Angle(225)
        if self == Direction.DOWN:
            return Angle(180)
        if self == Direction.DOWN_RIGHT:
            return Angle(135)
        raise DirectionException('Unknown direction') # pragma: no cover

    @property
    def offset(self) -> Coord:
        if self == Direction.UP_LEFT:
            return Coord(-1, -1)
        if self == Direction.UP:
            return Coord(-1, 0)
        if self == Direction.UP_RIGHT:
            return Coord(-1, 1)
        if self == Direction.LEFT:
            return Coord(0, -1)
        if self == Direction.CENTER:
            return Coord(0, 0)
        if self == Direction.RIGHT:
            return Coord(0, 1)
        if self == Direction.DOWN_LEFT:
            return Coord(1, -1)
        if self == Direction.DOWN:
            return Coord(1, 0)
        if self == Direction.DOWN_RIGHT:
            return Coord(1, 1)
        raise DirectionException('Unknown direction')  # pragma: no cover

    def parallel(self, other: 'Direction') -> bool:
        return (self == other) or (self == -other)

    @staticmethod
    def direction(location: int) -> 'Direction':
        return Direction(location)

    @property
    def location(self) -> int:
        return self.value

    @staticmethod
    def orthogonals() -> List[Coord]:
        return [
            d.offset for d in [Direction.UP, Direction.RIGHT, Direction.DOWN, Direction.LEFT]
        ]

    @staticmethod
    def diagonals() -> List[Coord]:
        return [
            d.offset for d in [Direction.UP_LEFT, Direction.UP_RIGHT, Direction.DOWN_RIGHT, Direction.DOWN_LEFT]
        ]

    @staticmethod
    def kings() -> List[Coord]:
        return [
            d.offset
            for d in [
                Direction.UP_LEFT,
                Direction.UP_RIGHT,
                Direction.DOWN_RIGHT,
                Direction.DOWN_LEFT,
                Direction.UP,
                Direction.RIGHT,
                Direction.DOWN,
                Direction.LEFT
            ]
        ]

    @staticmethod
    def all() -> List[Coord]:
        return [
            d.offset
            for d in [
                Direction.UP_LEFT,
                Direction.UP,
                Direction.UP_RIGHT,
                Direction.LEFT,
                Direction.CENTER,
                Direction.RIGHT,
                Direction.DOWN_LEFT,
                Direction.DOWN,
                Direction.DOWN_RIGHT
            ]
        ]
