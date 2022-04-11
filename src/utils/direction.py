from enum import Enum
from typing import List

from src.utils.angle import Angle
from src.utils.coord import Coord


class DirectionException(Exception):
    pass


class Direction(Enum):
    UPLEFT = 1
    UP = 2
    UPRIGHT = 3
    LEFT = 4
    CENTER = 5
    RIGHT = 6
    DOWNLEFT = 7
    DOWN = 8
    DOWNRIGHT = 9

    @staticmethod
    def locations():
        return [d.value for d in Direction]

    def __neg__(self) -> 'Direction':
        if self == Direction.UPLEFT:
            return Direction.DOWNRIGHT
        if self == Direction.UP:
            return Direction.DOWN
        if self == Direction.UPRIGHT:
            return Direction.DOWNLEFT
        if self == Direction.LEFT:
            return Direction.RIGHT
        if self == Direction.CENTER:
            return Direction.CENTER
        if self == Direction.RIGHT:
            return Direction.LEFT
        if self == Direction.DOWNLEFT:
            return Direction.UPRIGHT
        if self == Direction.DOWN:
            return Direction.UP
        if self == Direction.DOWNRIGHT:
            return Direction.UPLEFT

    @property
    def angle(self) -> Angle:
        if self == Direction.UPLEFT:
            return Angle(315)
        if self == Direction.UP:
            return Angle(0)
        if self == Direction.UPRIGHT:
            return Angle(45)
        if self == Direction.LEFT:
            return Angle(270)
        if self == Direction.CENTER:
            return Angle(0)
        if self == Direction.RIGHT:
            return Angle(90)
        if self == Direction.DOWNLEFT:
            return Angle(225)
        if self == Direction.DOWN:
            return Angle(180)
        if self == Direction.DOWNRIGHT:
            return Angle(135)

    @property
    def offset(self) -> Coord:
        if self == Direction.UPLEFT:
            return Coord(-1, -1)
        if self == Direction.UP:
            return Coord(-1, 0)
        if self == Direction.UPRIGHT:
            return Coord(-1, 1)
        if self == Direction.LEFT:
            return Coord(0, -1)
        if self == Direction.CENTER:
            return Coord(0, 0)
        if self == Direction.RIGHT:
            return Coord(0, 1)
        if self == Direction.DOWNLEFT:
            return Coord(1, -1)
        if self == Direction.DOWN:
            return Coord(1, 0)
        if self == Direction.DOWNRIGHT:
            return Coord(1, 1)

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
            d.offset for d in [Direction.UPLEFT, Direction.UPRIGHT, Direction.DOWNRIGHT, Direction.DOWNLEFT]
        ]

    @staticmethod
    def kings() -> List[Coord]:
        return [
            d.offset
            for d in [
                Direction.UPLEFT,
                Direction.UPRIGHT,
                Direction.DOWNRIGHT,
                Direction.DOWNLEFT,
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
                Direction.UPLEFT,
                Direction.UP,
                Direction.UPRIGHT,
                Direction.LEFT,
                Direction.CENTER,
                Direction.RIGHT,
                Direction.DOWNLEFT,
                Direction.DOWN,
                Direction.DOWNRIGHT
            ]
        ]
