"""Side."""
from enum import Enum
from typing import Dict

from src.items.board import Board
from src.utils.coord import Coord
from src.utils.cyclic import Cyclic
from src.utils.direction import Direction
from src.utils.order import Order
from src.utils.sudoku_exception import SudokuException


class SideException(SudokuException):
    """Handle exceptions in the Side Enum."""


class Side(Enum):
    """Enum representing the sides of a board."""

    TOP = 'T'
    RIGHT = 'R'
    BOTTOM = 'B'
    LEFT = 'L'

    @staticmethod
    def create(letter: str) -> 'Side':
        """Create a Side from a letter.

        Args:
            letter (str): The letter representing the side.

        Returns:
            Side: The corresponding Side enum.
        """
        return Side(letter)

    @staticmethod
    def valid(letter: str) -> bool:
        """Check if a letter corresponds to a valid Side.

        Args:
            letter (str): The letter to validate.

        Returns:
            bool: True if the letter is valid, False otherwise.
        """
        # noinspection PyProtectedMember
        return letter in Side._value2member_map_

    def direction(self, cyclic: Cyclic) -> Direction:
        """Get the direction corresponding to the side and cyclic order.

        Args:
            cyclic (Cyclic): The cyclic order (CLOCKWISE or ANTICLOCKWISE).

        Returns:
            Direction: The direction corresponding to the side and cyclic order.

        Raises:
            SideException: If the combination is unknown.
        """
        return DIRECTION_MAP[(self, cyclic)]

    def order_direction(self, order: Order) -> Direction:  # pylint: disable=too-many-return-statements
        """Get the direction based on the side and order.

        Args:
            order (Order): The order (INCREASING or DECREASING).

        Returns:
            Direction: The direction corresponding to the side and order.

        Raises:
            SideException: If the combination is unknown.
        """
        return ORDER_DIRECTION_MAP[(self, order)]

    def order_offset(self) -> Coord:  # pylint: disable=too-many-return-statements
        """Get the offset for the order based on the side.

        Returns:
            Coord: The coordinate offset corresponding to the side.

        Raises:
            SideException: If the combination is unknown.
        """
        return ORDER_OFFSET_MAP[self]

    @property
    def horizontal(self) -> bool:
        """Check if the side is horizontal.

        Returns:
            bool: True if the side is horizontal (LEFT or RIGHT), False otherwise.
        """
        return self in {Side.LEFT, Side.RIGHT}

    @property
    def vertical(self) -> bool:
        """Check if the side is vertical.

        Returns:
            bool: True if the side is vertical (TOP or BOTTOM), False otherwise.
        """
        return self in {Side.TOP, Side.BOTTOM}

    def marker(self, board: Board, n: int) -> Coord:  # pylint: disable=too-many-return-statements
        """Get the marker coordinate for the side on the board.

        Args:
            board (Board): The board on which the marker is placed.
            n (int): The index for the side.

        Returns:
            Coord: The coordinate of the marker.

        Raises:
            SideException: If the combination is unknown.
        """
        return MARKER_COORDINATES[self](board, n)

    def start_cell(self, board: Board, n: int) -> Coord:  # pylint: disable=too-many-return-statements
        """Get the starting cell coordinate for the side on the board.

        Args:
            board (Board): The board on which the starting cell is located.
            n (int): The index for the side.

        Returns:
            Coord: The coordinate of the starting cell.

        Raises:
            SideException: If the combination is unknown.
        """
        return START_CELL_COORDINATES[self](board, n)

    def start(self, board: Board, cyclic: Cyclic, n: int) -> Coord:  # pylint: disable=too-many-return-statements
        """Get the starting coordinate for the side based on cyclic direction.

        Args:
            board (Board): The board on which the starting coordinate is located.
            cyclic (Cyclic): The cyclic order (CLOCKWISE or ANTICLOCKWISE).
            n (int): The index for the side.

        Returns:
            Coord: The starting coordinate.

        Raises:
            SideException: If the combination is unknown.
        """
        return START_COORDINATES[(self, cyclic)](board, n)

    @staticmethod
    def values() -> str:
        """Get the string representation of all side values.

        Returns:
            str: A string of all side values.
        """
        return "".join([side.value for side in Side])

    def __repr__(self) -> str:
        """Return the string representation of the Side.

        Returns:
            str: The string representation of the side.
        """
        return f"Side.{self.name}"


DIRECTION_MAP: Dict[tuple, Direction] = {
    (Side.TOP, Cyclic.CLOCKWISE): Direction.DOWN_RIGHT,
    (Side.RIGHT, Cyclic.CLOCKWISE): Direction.DOWN_LEFT,
    (Side.BOTTOM, Cyclic.CLOCKWISE): Direction.UP_LEFT,
    (Side.LEFT, Cyclic.CLOCKWISE): Direction.UP_RIGHT,
    (Side.TOP, Cyclic.ANTICLOCKWISE): Direction.DOWN_LEFT,
    (Side.RIGHT, Cyclic.ANTICLOCKWISE): Direction.UP_LEFT,
    (Side.BOTTOM, Cyclic.ANTICLOCKWISE): Direction.UP_RIGHT,
    (Side.LEFT, Cyclic.ANTICLOCKWISE): Direction.DOWN_RIGHT,
}

ORDER_DIRECTION_MAP: Dict[tuple, Direction] = {
    (Side.TOP, Order.INCREASING): Direction.DOWN,
    (Side.TOP, Order.DECREASING): Direction.UP,
    (Side.RIGHT, Order.INCREASING): Direction.LEFT,
    (Side.RIGHT, Order.DECREASING): Direction.RIGHT,
    (Side.BOTTOM, Order.INCREASING): Direction.UP,
    (Side.BOTTOM, Order.DECREASING): Direction.DOWN,
    (Side.LEFT, Order.INCREASING): Direction.RIGHT,
    (Side.LEFT, Order.DECREASING): Direction.LEFT,
}

ORDER_OFFSET_MAP: Dict[Side, Coord] = {
    Side.TOP: Direction.DOWN.offset,
    Side.RIGHT: Direction.LEFT.offset,
    Side.BOTTOM: Direction.UP.offset,
    Side.LEFT: Direction.RIGHT.offset,
}

# Coordinate mappings for `marker` and `start_cell` to reduce repetitive code
MARKER_COORDINATES = {
    Side.TOP: lambda board, n: Coord(0, n),
    Side.RIGHT: lambda board, n: Coord(n, board.board_rows + 1),
    Side.BOTTOM: lambda board, n: Coord(board.board_columns + 1, n),
    Side.LEFT: lambda board, n: Coord(n, 0),
}

START_CELL_COORDINATES = {
    Side.TOP: lambda board, n: Coord(1, n),
    Side.RIGHT: lambda board, n: Coord(n, board.board_rows),
    Side.BOTTOM: lambda board, n: Coord(board.board_columns, n),
    Side.LEFT: lambda board, n: Coord(n, 1),
}

START_COORDINATES = {
    (Side.TOP, Cyclic.CLOCKWISE): lambda board, n: Coord(1, n + 1),
    (Side.RIGHT, Cyclic.CLOCKWISE): lambda board, n: Coord(n + 1, board.board_columns),
    (Side.BOTTOM, Cyclic.CLOCKWISE): lambda board, n: Coord(board.board_rows, n - 1),
    (Side.LEFT, Cyclic.CLOCKWISE): lambda board, n: Coord(n - 1, 1),
    (Side.TOP, Cyclic.ANTICLOCKWISE): lambda board, n: Coord(1, n - 1),
    (Side.RIGHT, Cyclic.ANTICLOCKWISE): lambda board, n: Coord(n - 1, board.board_columns),
    (Side.BOTTOM, Cyclic.ANTICLOCKWISE): lambda board, n: Coord(board.board_rows, n + 1),
    (Side.LEFT, Cyclic.ANTICLOCKWISE): lambda board, n: Coord(n + 1, 1),
}
