from enum import Enum
from typing import List

from src.items.item import SudokuException
from src.utils.angle import Angle
from src.utils.coord import Coord


class DirectionException(SudokuException):
    """
    Custom exception class for errors related to Direction.
    """
    pass


class Direction(Enum):
    """
    Enumeration for 8 possible movement directions and center in a grid.

    Attributes:
        UP_LEFT (int): Represents up-left direction.
        UP (int): Represents up direction.
        UP_RIGHT (int): Represents up-right direction.
        LEFT (int): Represents left direction.
        CENTER (int): Represents the center (no movement).
        RIGHT (int): Represents right direction.
        DOWN_LEFT (int): Represents down-left direction.
        DOWN (int): Represents down direction.
        DOWN_RIGHT (int): Represents down-right direction.
    """
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
        """
        Returns a list of integer values for each direction.

        Returns:
            List[int]: The integer values corresponding to the directions.
        """
        return [d.value for d in Direction]

    def __neg__(self) -> 'Direction':
        """
        Returns the opposite of the current direction.

        Returns:
            Direction: The opposite direction.

        Raises:
            DirectionException: If the direction is unknown.
        """
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
        raise DirectionException('Unknown direction')

    @property
    def angle(self) -> Angle:
        """
        Returns the angle associated with the direction.

        Returns:
            Angle: The angle corresponding to the direction.

        Raises:
            DirectionException: If the direction is unknown.
        """
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
        raise DirectionException('Unknown direction')

    @property
    def offset(self) -> Coord:
        """
        Returns the coordinate offset corresponding to the direction.

        Returns:
            Coord: The coordinate offset.

        Raises:
            DirectionException: If the direction is unknown.
        """
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
        raise DirectionException('Unknown direction')

    def parallel(self, other: 'Direction') -> bool:
        """
        Checks if the given direction is parallel to the current direction.

        Args:
            other (Direction): The other direction to check.

        Returns:
            bool: True if the directions are parallel, otherwise False.
        """
        return self in [other, -other]

    @staticmethod
    def direction(location: int) -> 'Direction':
        """
        Returns the Direction enum instance corresponding to the given location value.

        Args:
            location (int): The integer value of the direction.

        Returns:
            Direction: The corresponding Direction enum.
        """
        return Direction(location)

    @property
    def location(self) -> int:
        """
        Returns the location value of the direction.

        Returns:
            int: The integer value representing the direction.
        """
        return self.value

    @staticmethod
    def orthogonals() -> List[Coord]:
        """
        Returns a list of coordinate offsets for orthogonal directions (up, right, down, left).

        Returns:
            List[Coord]: The offsets for the orthogonal directions.
        """
        return [d.offset for d in [Direction.UP, Direction.RIGHT, Direction.DOWN, Direction.LEFT]]

    @staticmethod
    def diagonals() -> List[Coord]:
        """
        Returns a list of coordinate offsets for diagonal directions.

        Returns:
            List[Coord]: The offsets for the diagonal directions.
        """
        return [d.offset for d in [Direction.UP_LEFT, Direction.UP_RIGHT, Direction.DOWN_RIGHT, Direction.DOWN_LEFT]]

    @staticmethod
    def kings() -> List[Coord]:
        """
        Returns a list of coordinate offsets for all directions except the center (king's movement in chess).

        Returns:
            List[Coord]: The offsets for the king's movement directions.
        """
        return [
            d.offset for d in [
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
        """
        Returns a list of coordinate offsets for all directions, including the center.

        Returns:
            List[Coord]: The offsets for all directions.
        """
        return [
            d.offset for d in [
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