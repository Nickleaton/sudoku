from enum import Enum

from src.items.board import Board
from src.utils.coord import Coord
from src.utils.cyclic import Cyclic
from src.utils.direction import Direction
from src.utils.order import Order


class Side(Enum):
    TOP = 'T'
    RIGHT = 'R'
    BOTTOM = 'B'
    LEFT = 'L'

    @staticmethod
    def create(letter: str) -> 'Side':
        return Side(letter)

    def direction(self, cyclic: Cyclic) -> Direction:
        if cyclic == Cyclic.CLOCKWISE:
            if self == Side.TOP:
                return Direction.DOWNRIGHT
            if self == Side.RIGHT:
                return Direction.DOWNLEFT
            if self == Side.BOTTOM:
                return Direction.UPLEFT
            if self == Side.LEFT:
                return Direction.UPRIGHT
        if cyclic == Cyclic.ANTICLOCKWISE:
            if self == Side.TOP:
                return Direction.DOWNLEFT
            if self == Side.RIGHT:
                return Direction.UPLEFT
            if self == Side.BOTTOM:
                return Direction.UPRIGHT
            if self == Side.LEFT:
                return Direction.DOWNRIGHT

    def order_direction(self, order: Order) -> Direction:
        if self == Side.TOP:
            return Direction.DOWN if order == Order.INCREASING else Direction.UP
        if self == Side.RIGHT:
            return Direction.LEFT if order == Order.INCREASING else Direction.RIGHT
        if self == Side.BOTTOM:
            return Direction.UP if order == Order.INCREASING else Direction.DOWN
        if self == Side.LEFT:
            return Direction.RIGHT if order == Order.INCREASING else Direction.LEFT

    def order_offset(self, order: Order) -> Coord:
        if self == Side.TOP:
            return Direction.DOWN.offset
        if self == Side.RIGHT:
            return Direction.LEFT.offset
        if self == Side.BOTTOM:
            return Direction.UP.offset
        if self == Side.LEFT:
            return Direction.RIGHT.offset

    def marker(self, board: Board, n: int) -> Coord:
        if self == Side.TOP:
            return Coord(0, n)
        if self == Side.RIGHT:
            return Coord(n, board.board_rows + 1)
        if self == Side.BOTTOM:
            return Coord(board.board_columns + 1, n)
        if self == Side.LEFT:
            return Coord(n, 0)

    def start_cell(self, board: Board, n: int) -> Coord:
        if self == Side.TOP:
            return Coord(1, n)
        if self == Side.RIGHT:
            return Coord(n, board.board_rows)
        if self == Side.BOTTOM:
            return Coord(board.board_columns, n)
        if self == Side.LEFT:
            return Coord(n, 1)

    def start(self, board: Board, cyclic: Cyclic, n: int) -> Coord:
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

    def __repr__(self):
        return f"Side.{self.name}"