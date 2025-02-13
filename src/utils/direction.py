"""Direction."""
from enum import StrEnum
from types import MappingProxyType

from src.utils.coord import Coord

COORD_MAP: MappingProxyType[str, Coord] = MappingProxyType({
    'UL': Coord(-1, -1),
    'U': Coord(-1, 0),
    'UR': Coord(-1, 1),
    'L': Coord(0, -1),
    'R': Coord(0, 1),
    'DL': Coord(1, -1),
    'D': Coord(1, 0),
    'DR': Coord(1, 1),
})


class Direction(StrEnum):
    """Enumeration representing eight possible movement directions."""

    up_left = 'UL'
    up = 'U'
    up_right = 'UR'
    left = 'L'
    right = 'R'
    down_left = 'DL'
    down = 'D'
    down_right = 'DR'

    @staticmethod
    def create(name: str) -> 'Direction':
        """Retrieve the corresponding Direction from a short name.

        Args:
            name (str): Short name representing a direction (e.g., 'UL', 'U', 'UR', etc.).

        Returns:
            Direction: Corresponding Direction enum instance.

        Raises:
            ValueError: If the provided name does not match a valid direction.
        """
        try:
            return Direction(name)
        except ValueError as exc:
            raise ValueError(f'Invalid direction name {name!r}.') from exc

    @property
    def coord(self) -> Coord:
        """Return the coordinate offset for this direction.

        Returns:
            Coord: Corresponding coordinate offset.
        """
        return COORD_MAP[str(self)]

    def __repr__(self) -> str:
        """Return a string representation of the Direction enum instance.

        Returns:
            str: String in the format 'Direction.<name>'.
        """
        return f'Direction.{self.name}'
