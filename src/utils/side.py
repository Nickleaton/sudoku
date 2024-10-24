from enum import Enum

from src.items.board import Board
from src.utils.coord import Coord
from src.utils.cyclic import Cyclic
from src.utils.direction import Direction
from src.utils.order import Order
from src.utils.sudoku_exception import SudokuException


class SideException(SudokuException):
    pass


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
        for side in Side:
            if letter == side.value:
                return True
        return False

    def direction(self, cyclic: Cyclic) -> Direction:  # pylint: disable=too-many-return-statements
        """Get the direction corresponding to the side and cyclic order.

        Args:
            cyclic (Cyclic): The cyclic order (CLOCKWISE or ANTICLOCKWISE).

        Returns:
            Direction: The direction corresponding to the side and cyclic order.

        Raises:
            SideException: If the combination is unknown.
        """
        if cyclic == Cyclic.CLOCKWISE:
            if self == Side.TOP:
                return Direction.DOWN_RIGHT
            if self == Side.RIGHT:
                return Direction.DOWN_LEFT
            if self == Side.BOTTOM:
                return Direction.UP_LEFT
            if self == Side.LEFT:
                return Direction.UP_RIGHT
        if cyclic == Cyclic.ANTICLOCKWISE:
            if self == Side.TOP:
                return Direction.DOWN_LEFT
            if self == Side.RIGHT:
                return Direction.UP_LEFT
            if self == Side.BOTTOM:
                return Direction.UP_RIGHT
            if self == Side.LEFT:
                return Direction.DOWN_RIGHT
        raise SideException("Unknown combination")  # pragma: no cover

    def order_direction(self, order: Order) -> Direction:  # pylint: disable=too-many-return-statements
        """Get the direction based on the side and order.

        Args:
            order (Order): The order (INCREASING or DECREASING).

        Returns:
            Direction: The direction corresponding to the side and order.

        Raises:
            SideException: If the combination is unknown.
        """
        if self == Side.TOP:
            return Direction.DOWN if order == Order.INCREASING else Direction.UP
        if self == Side.RIGHT:
            return Direction.LEFT if order == Order.INCREASING else Direction.RIGHT
        if self == Side.BOTTOM:
            return Direction.UP if order == Order.INCREASING else Direction.DOWN
        if self == Side.LEFT:
            return Direction.RIGHT if order == Order.INCREASING else Direction.LEFT
        raise SideException("Unknown combination")  # pragma: no cover

    def order_offset(self) -> Coord:  # pylint: disable=too-many-return-statements
        """Get the offset for the order based on the side.

        Returns:
            Coord: The coordinate offset corresponding to the side.

        Raises:
            SideException: If the combination is unknown.
        """
        if self == Side.TOP:
            return Direction.DOWN.offset
        if self == Side.RIGHT:
            return Direction.LEFT.offset
        if self == Side.BOTTOM:
            return Direction.UP.offset
        if self == Side.LEFT:
            return Direction.RIGHT.offset
        raise SideException("Unknown combination")  # pragma: no cover

    @property
    def horizontal(self) -> bool:
        """Check if the side is horizontal.

        Returns:
            bool: True if the side is horizontal (LEFT or RIGHT), False otherwise.
        """
        return self in [Side.LEFT, Side.RIGHT]

    @property
    def vertical(self) -> bool:
        """Check if the side is vertical.

        Returns:
            bool: True if the side is vertical (TOP or BOTTOM), False otherwise.
        """
        return self in [Side.TOP, Side.BOTTOM]

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
        if self == Side.TOP:
            return Coord(0, n)
        if self == Side.RIGHT:
            return Coord(n, board.board_rows + 1)
        if self == Side.BOTTOM:
            return Coord(board.board_columns + 1, n)
        if self == Side.LEFT:
            return Coord(n, 0)
        raise SideException("Unknown combination")  # pragma: no cover

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
        if self == Side.TOP:
            return Coord(1, n)
        if self == Side.RIGHT:
            return Coord(n, board.board_rows)
        if self == Side.BOTTOM:
            return Coord(board.board_columns, n)
        if self == Side.LEFT:
            return Coord(n, 1)
        raise SideException("Unknown combination")  # pragma: no cover

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
        if cyclic == Cyclic.CLOCKWISE:
            if self == Side.TOP:
                return Coord(1, n + 1)
            if self == Side.RIGHT:
                return Coord(n + 1, board.board_columns)
            if self == Side.BOTTOM:
                return Coord(board.board_rows, n - 1)
            if self == Side.LEFT:
                return Coord(n - 1, 1)
        if cyclic == Cyclic.ANTICLOCKWISE:
            if self == Side.TOP:
                return Coord(1, n - 1)
            if self == Side.RIGHT:
                return Coord(n - 1, board.board_columns)
            if self == Side.BOTTOM:
                return Coord(board.board_rows, n + 1)
            if self == Side.LEFT:
                return Coord(n + 1, 1)
        raise SideException("Unknown combination")  # pragma: no cover

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
