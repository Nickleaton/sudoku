"""Moves."""
from functools import cache
from typing import List

from src.utils.coord import Coord


class Moves:
    """Utility class listing possible moves as Coords or offsets from a cell."""

    # Initialize all class-level variables to `Coord` instances
    UP_LEFT: Coord = Coord(-1, -1)
    UP: Coord = Coord(-1, 0)
    UP_RIGHT: Coord = Coord(-1, 1)
    LEFT: Coord = Coord(0, -1)
    CENTER: Coord = Coord(0, 0)
    RIGHT: Coord = Coord(0, 1)
    DOWN_LEFT: Coord = Coord(1, -1)
    DOWN: Coord = Coord(1, 0)
    DOWN_RIGHT: Coord = Coord(1, 1)

    @staticmethod
    @cache
    def orthogonals() -> List[Coord]:
        """Get coordinates for orthogonal directions (up, right, down, left).

        Returns:
            List[Coord]: A list of `Coord` instances representing orthogonal directions.
        """
        return [Moves.LEFT, Moves.RIGHT, Moves.UP, Moves.DOWN]

    @staticmethod
    @cache
    def diagonals() -> List[Coord]:
        """Get coordinates for diagonal directions (up-left, up-right, down-right, down-left).

        Returns:
            List[Coord]: A list of `Coord` instances representing diagonal directions.
        """
        return [Moves.UP_LEFT, Moves.UP_RIGHT, Moves.DOWN_RIGHT, Moves.DOWN_LEFT]

    @staticmethod
    @cache
    def kings() -> List[Coord]:
        """Get coordinates for all directions except CENTER, simulating a king's movement in chess.

        Returns:
            List[Coord]: A list of `Coord` instances representing all directions except CENTER.
        """
        return Moves.orthogonals() + Moves.diagonals()

    @staticmethod
    @cache
    def knights() -> List[Coord]:
        """Get coordinates for knight's movement in chess.

        Returns:
            List[Coord]: A list of `Coord` instances representing knight's movement.
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
    def directions() -> List[Coord]:
        """Get a list of all `Coord` instances representing directions.

        Returns:
            List[Coord]: A list of `Coord` instances representing all orthogonal and diagonal directions.
        """
        return Moves.orthogonals() + Moves.diagonals()

    @staticmethod
    @cache
    def all() -> List[Coord]:
        """Get all 8 directions plus the CENTER.

        Returns:
            List[Coord]: A list of `Coord` instances representing all directions including CENTER.
        """
        return Moves.directions() + [Moves.CENTER]

    @staticmethod
    @cache
    def square() -> List[Coord]:
        """Get square offsets.

        Returns:
            List[Coord]: A list of `Coord` instances representing the current 'square'
        """
        return [Moves.CENTER, Moves.UP_RIGHT, Moves.DOWN, Moves.DOWN_RIGHT]
