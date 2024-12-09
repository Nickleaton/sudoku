"""Direction."""
from enum import Enum
from functools import cache

from src.utils.angle import Angle
from src.utils.coord import Coord


class Direction(Enum):
    """Enum representing eight compass directions and center with angle, offset, and location value_list."""

    UP_LEFT = (315, -1, -1, 1)
    UP = (0, -1, 0, 2)
    UP_RIGHT = (45, -1, 1, 3)
    LEFT = (270, 0, -1, 4)
    CENTER = (0, 0, 0, 5)
    RIGHT = (90, 0, 1, 6)
    DOWN_LEFT = (225, 1, -1, 7)
    DOWN = (180, 1, 0, 8)
    DOWN_RIGHT = (135, 1, 1, 9)

    # Opposite direction map, mapping each direction to its opposite
    OPPOSITE_MAP = {
        UP_LEFT: DOWN_RIGHT,
        UP: DOWN,
        UP_RIGHT: DOWN_LEFT,
        LEFT: RIGHT,
        CENTER: CENTER,
        RIGHT: LEFT,
        DOWN_LEFT: UP_RIGHT,
        DOWN: UP,
        DOWN_RIGHT: UP_LEFT,
    }

    def __init__(self, angle: float, x_coord: int, y_coord: int, location: int):
        """Initialize start Direction instance with angle, x_coord/y_coord offset, and location.

        Args:
            angle (float): Angle in degrees representing the direction.
            x_coord (int): X-coordinate offset for the direction.
            y_coord (int): Y-coordinate offset for the direction.
            location (int): Unique integer identifier for the direction.
        """
        self.angle: Angle = Angle(angle)
        self.offset: Coord = Coord(x_coord, y_coord)
        self.location: int = location

    def __neg__(self) -> 'Direction':
        """Return the opposite direction.

        Returns:
            Direction: The opposite direction.
        """
        return Direction.OPPOSITE_MAP[self]

    @staticmethod
    def locations() -> list[int]:
        """Get list of unique integer value_list representing each direction.

        Returns:
            list[int]: list of location identifiers.
        """
        return [direction.location for direction in Direction]

    @staticmethod
    def direction(location: int) -> 'Direction':
        """Get the Direction corresponding to start specific location identifier.

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
        raise ValueError(f'Invalid location value: {location}')

    def parallel(self, other: 'Direction') -> bool:
        """Check if the provided direction is parallel to this one.

        Args:
            other (Direction): The direction to compare.

        Returns:
            bool: True if the directions are parallel, False otherwise.
        """
        if self == Direction.UP and other == Direction.DOWN:
            return True
        if self == Direction.DOWN and other == Direction.UP:
            return True
        if self == Direction.LEFT and other == Direction.RIGHT:
            return True
        if self == Direction.RIGHT and other == Direction.LEFT:
            return True
        return self == other

    @staticmethod
    @cache
    def orthogonals() -> list[Coord]:
        """Get coordinates for orthogonal directions.

        Returns:
            list[Coord]: list of coordinates for UP, RIGHT, DOWN, LEFT.
        """
        return [Direction.UP.offset, Direction.RIGHT.offset, Direction.DOWN.offset, Direction.LEFT.offset]

    @staticmethod
    @cache
    def diagonals() -> list[Coord]:
        """Get coordinates for diagonal directions.

        Returns:
            list[Coord]: list of coordinates for UP_LEFT, UP_RIGHT, DOWN_RIGHT, DOWN_LEFT.
        """
        return [
            Direction.UP_LEFT.offset,
            Direction.UP_RIGHT.offset,
            Direction.DOWN_RIGHT.offset,
            Direction.DOWN_LEFT.offset,
        ]

    @staticmethod
    @cache
    def kings() -> list[Coord]:
        """Get coordinates for all directions except CENTER, simulating king's movement.

        Returns:
            list[Coord]: list of coordinates excluding CENTER.
        """
        return [direction.offset for direction in Direction if direction != Direction.CENTER]

    @staticmethod
    @cache
    def knights() -> list[Coord]:
        """Get coordinates for knight's movement in chess.

        Returns:
            list[Coord]: list of coordinates representing knight's movement.
        """
        return [
            Coord(-1, -2),
            Coord(1, -2),
            Coord(-2, -1),
            Coord(-2, 1),
            Coord(-1, 2),
            Coord(1, 2),
            Coord(2, 1),
            Coord(2, -1),
        ]

    @staticmethod
    @cache
    def all_but_center() -> list[Coord]:
        """Get coordinates for all directions except CENTER.

        Returns:
            list[Coord]: list of coordinates excluding CENTER.
        """
        return [direction.offset for direction in Direction if direction != Direction.CENTER]

    @staticmethod
    @cache
    def all() -> list[Coord]:
        """Get coordinates for all directions including CENTER.

        Returns:
            list[Coord]: list of all coordinates.
        """
        return [direction.offset for direction in Direction]
