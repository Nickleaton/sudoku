"""Moves."""
from functools import cache
from itertools import product

from src.utils.coord import Coord


class Moves:
    """Utility class listing possible moves as Coords or offsets from a cell."""

    # Initialize all class-level variables to `Coord` instances
    up_left: Coord = Coord(-1, -1)
    up: Coord = Coord(-1, 0)
    up_right: Coord = Coord(-1, 1)
    left: Coord = Coord(0, -1)
    center: Coord = Coord(0, 0)
    right: Coord = Coord(0, 1)
    down_left: Coord = Coord(1, -1)
    down: Coord = Coord(1, 0)
    down_right: Coord = Coord(1, 1)

    @staticmethod
    @cache
    def orthogonals() -> list[Coord]:
        """Get coordinates for orthogonal directions (up, right, down, left).

        Returns:
            list[Coord]: A list of `Coord` instances representing orthogonal directions.
        """
        return [Moves.left, Moves.right, Moves.up, Moves.down]

    @staticmethod
    @cache
    def diagonals() -> list[Coord]:
        """Get coordinates for diagonal directions (up-left, up-right, down-right, down-left).

        Returns:
            list[Coord]: A list of `Coord` instances representing diagonal directions.
        """
        return [Moves.up_left, Moves.up_right, Moves.down_right, Moves.down_left]

    @staticmethod
    @cache
    def kings() -> list[Coord]:
        """Get coordinates for all directions except center, simulating a king's movement in chess.

        Returns:
            list[Coord]: A list of `Coord` instances representing all directions except center.
        """
        return Moves.orthogonals() + Moves.diagonals()

    @staticmethod
    @cache
    def knights() -> list[Coord]:
        """Get coordinates for knight's movement in chess.

        Returns:
            list[Coord]: A list of `Coord` instances representing knight's movement.
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
    def directions() -> list[Coord]:
        """Get a list of all `Coord` instances representing directions.

        Returns:
            list[Coord]: A list of `Coord` instances representing all orthogonal and diagonal directions.
        """
        return Moves.orthogonals() + Moves.diagonals()

    @staticmethod
    @cache
    def all_moves() -> list[Coord]:
        """Get all 8 directions plus the center.

        Returns:
            list[Coord]: A list of `Coord` instances representing all directions including center.
        """
        return [*Moves.directions(), Moves.center]

    @staticmethod
    @cache
    def square() -> list[Coord]:
        """Get square offsets.

        Returns:
            list[Coord]: A list of `Coord` instances representing the current 'square'
        """
        return [Moves.center, Moves.right, Moves.down, Moves.down_right]

    @staticmethod
    @cache
    def monkeys() -> list[Coord]:
        """Get monkey offsets.

        Returns:
            list[Coord]: Monkey moves.
        """
        return [
            Coord(-1, -3),
            Coord(1, -3),
            Coord(-3, -1),
            Coord(-3, 1),
            Coord(-1, 3),
            Coord(1, 3),
            Coord(3, 1),
            Coord(3, -1),
        ]

    @staticmethod
    @cache
    def girandola() -> list[Coord]:
        """Get girandola offsets.

        Returns:
            list[Coord]: Girandola moves.
        """
        return [
            Coord(1, 1),
            Coord(1, 9),
            Coord(2, 5),
            Coord(5, 2),
            Coord(5, 5),
            Coord(5, 8),
            Coord(8, 5),
            Coord(9, 1),
            Coord(9, 9),
        ]

    @staticmethod
    @cache
    def asterix() -> list[Coord]:
        """Get asterix offsets.

        Returns:
            list[Coord]: Asterix moves.
        """
        return [
            Coord(2, 5),
            Coord(3, 3),
            Coord(3, 7),
            Coord(5, 2),
            Coord(5, 5),
            Coord(5, 8),
            Coord(7, 3),
            Coord(7, 7),
            Coord(8, 5),
        ]

    @staticmethod
    @cache
    def disjoint9x9() -> list[Coord]:
        """Get disjoint offsets for a 9x9 board.

        Returns:
            list[Coord]: Disjoint moves.
        """
        return [Coord(box_row * 3, box_col * 3) for box_row, box_col in product(range(3), range(3))]
