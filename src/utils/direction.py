"""Direction."""
from enum import Enum
from functools import cache
from typing import List

from src.utils.angle import Angle
from src.utils.coord import Coord


class Direction(Enum):
    """Enum representing eight compass directions and center with angle, offset, and location values."""

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
        """Initialize a Direction instance with angle, x/y offset, and location.

        Args:
            angle (float): Angle in degrees representing the direction.
            x (int): X-coordinate offset for the direction.
            y (int): Y-coordinate offset for the direction.
            location (int): Unique integer identifier for the direction.
        """
        self.angle: Angle = Angle(angle)
        self.offset: Coord = Coord(x, y)
        self.location: int = location

    def __neg__(self) -> 'Direction':
        """Return the opposite direction.

        Returns:
            Direction: The opposite direction.
        """
        return OPPOSITE_MAP[self]

    @staticmethod
    def locations() -> List[int]:
        """Get list of unique integer values representing each direction.

        Returns:
            List[int]: List of location identifiers.
        """
        return [d.location for d in Direction]

    @staticmethod
    def direction(location: int) -> 'Direction':
        """Get the Direction corresponding to a specific location identifier.

        Args:
            location (int): Location identifier.

        Returns:
            Direction: Corresponding Direction instance.

        Raises:
            ValueError: If no Direction matches the provided location.
        """
        for direction in Direction:
            if direction.location == location:
                return direction
        raise ValueError(f"Invalid location value: {location}")

    def parallel(self, other: 'Direction') -> bool:
        """Check if the provided direction is parallel to this one.

        Args:
            other (Direction): The direction to compare.

        Returns:
            bool: True if the directions are parallel, False otherwise.
        """
        return self in [other, -other]

    @staticmethod
    @cache
    def orthogonals() -> List[Coord]:
        """Get coordinates for orthogonal directions.

        Returns:
            List[Coord]: List of coordinates for UP, RIGHT, DOWN, LEFT.
        """
        return [Direction.UP.offset, Direction.RIGHT.offset, Direction.DOWN.offset, Direction.LEFT.offset]

    @staticmethod
    @cache
    def diagonals() -> List[Coord]:
        """Get coordinates for diagonal directions.

        Returns:
            List[Coord]: List of coordinates for UP_LEFT, UP_RIGHT, DOWN_RIGHT, DOWN_LEFT.
        """
        return [
            Direction.UP_LEFT.offset,
            Direction.UP_RIGHT.offset,
            Direction.DOWN_RIGHT.offset,
            Direction.DOWN_LEFT.offset
        ]

    @staticmethod
    @cache
    def kings() -> List[Coord]:
        """Get coordinates for all directions except CENTER, simulating king's movement.

        Returns:
            List[Coord]: List of coordinates excluding CENTER.
        """
        return [d.offset for d in Direction if d != Direction.CENTER]

    @staticmethod
    @cache
    def knights() -> List[Coord]:
        """Get coordinates for knight's movement in chess.

        Returns:
            List[Coord]: List of coordinates representing knight's movement.
        """
        return [
            Coord(-1, -2),
            Coord(1, -2),
            Coord(-2, -1),
            Coord(-2, 1),
            Coord(-1, 2),
            Coord(1, 2),
            Coord(2, 1),
            Coord(2, -1)
        ]

    @staticmethod
    @cache
    def all_but_center() -> List[Coord]:
        """Get coordinates for all directions except CENTER.

        Returns:
            List[Coord]: List of coordinates excluding CENTER.
        """
        return [d.offset for d in Direction if d != Direction.CENTER]

    @staticmethod
    @cache
    def all() -> List[Coord]:
        """Get coordinates for all directions including CENTER.

        Returns:
            List[Coord]: List of all coordinates.
        """
        return [d.offset for d in Direction]


# Define the opposite map outside the class to avoid `Direction` enum's limitations with subscripting.
OPPOSITE_MAP = {
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
