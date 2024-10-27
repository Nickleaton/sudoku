from enum import Enum
from typing import List

from src.utils.angle import Angle
from src.utils.coord import Coord


class Direction(Enum):
    UP_LEFT = (315, -1, -1, 1)
    UP = (0, -1, 0, 2)
    UP_RIGHT = (45, -1, 1, 3)
    LEFT = (270, 0, -1, 4)
    CENTER = (0, 0, 0, 5)
    RIGHT = (90, 0, 1, 6)
    DOWN_LEFT = (225, 1, -1, 7)
    DOWN = (180, 1, 0, 8)
    DOWN_RIGHT = (135, 1, 1, 9)

    def __init__(self, angle: float, x: int, y: int, location: int):
        self.angle: Angle = Angle(angle)
        self.offset: Coord = Coord(x, y)
        self.location: int = location

    def __neg__(self) -> 'Direction':
        opposite_map: dict[Direction, Direction] = {
            Direction.UP_LEFT: Direction.DOWN_RIGHT,
            Direction.UP: Direction.DOWN,
            Direction.UP_RIGHT: Direction.DOWN_LEFT,
            Direction.LEFT: Direction.RIGHT,
            Direction.CENTER: Direction.CENTER,
            Direction.RIGHT: Direction.LEFT,
            Direction.DOWN_LEFT: Direction.UP_RIGHT,
            Direction.DOWN: Direction.UP,
            Direction.DOWN_RIGHT: Direction.UP_LEFT,
        }
        return opposite_map[self]

    @staticmethod
    def locations() -> List[int]:
        """
        Returns a list of integer values for each direction.

        Returns:
            List[int]: The integer values corresponding to the directions.
        """
        return [d.location for d in Direction]

    @staticmethod
    def direction(location: int) -> 'Direction':
        """
        Returns the Direction enum instance corresponding to the given location value.

        Args:
            location (int): The integer value of the direction.

        Returns:
            Direction: The corresponding Direction enum.
        """
        for direction in Direction:
            if direction.location == location:
                return direction
        raise ValueError(f"Invalid location value: {location}")

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
    def orthogonals() -> List[Coord]:
        """
        Returns a list of coordinate offsets for orthogonal directions (up, right, down, left).

        Returns:
            List[Coord]: The offsets for the orthogonal directions.
        """
        return [
            d.offset for d in [
                Direction.UP,
                Direction.RIGHT,
                Direction.DOWN,
                Direction.LEFT
            ]
        ]

    @staticmethod
    def diagonals() -> List[Coord]:
        """
        Returns a list of coordinate offsets for diagonal directions.

        Returns:
            List[Coord]: The offsets for the diagonal directions.
        """
        return [
            d.offset for d in [
                Direction.UP_LEFT,
                Direction.UP_RIGHT,
                Direction.DOWN_RIGHT,
                Direction.DOWN_LEFT
            ]
        ]

    @staticmethod
    def kings() -> List[Coord]:
        """
        Returns a list of coordinate offsets for all directions except the center (king's movement in chess).

        Returns:
            List[Coord]: The offsets for the king's movement directions.
        """
        return [d.offset for d in Direction if d != Direction.CENTER]

    @staticmethod
    def all() -> List[Coord]:
        """
        Returns a list of coordinate offsets for all directions, including the center.

        Returns:
            List[Coord]: The offsets for all directions.
        """
        return [d.offset for d in Direction]
