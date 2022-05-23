import re
from itertools import product
from typing import Dict, Tuple, List

from pulp import lpSum

from src.glyphs.glyph import Glyph, CellGlyph
from src.items.board import Board
from src.items.item import Item
from src.solvers.pulp_solver import PulpSolver
from src.utils.coord import Coord
from src.utils.rule import Rule


class CellException(Exception):
    pass


# pylint: disable=too-many-public-methods
class Cell(Item):
    cache: Dict[Tuple[int, int], 'Cell'] = {}

    @classmethod
    def clear(cls):
        cls.cache.clear()

    def __init__(self, board: Board, row: int, column: int):
        super().__init__(board)
        self.row = row
        self.column = column
        self.possibles = [True] * self.board.maximum_digit

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.board!r}, {self.row!r}, {self.column!r})"

    def __hash__(self):
        return self.row * self.board.maximum_digit + self.column

    def set_possible(self, digits: List[int]) -> None:
        for digit in self.board.digit_range:
            if digit not in digits:
                self.possibles[digit - 1] = False

    def set_impossible(self, digits: List[int]) -> None:
        for digit in self.board.digit_range:
            if digit in digits:
                self.possibles[digit - 1] = False

    def set_odd(self) -> None:
        for digit in self.board.digit_range:
            if digit % 2 != 1:
                self.possibles[digit - 1] = False

    def set_even(self) -> None:
        for digit in self.board.digit_range:
            if digit % 2 != 0:
                self.possibles[digit - 1] = False

    def set_minimum(self, lower: int) -> None:
        for digit in self.board.digit_range:
            if digit < lower:
                self.possibles[digit - 1] = False

    def set_maximum(self, upper: int) -> None:
        for digit in self.board.digit_range:
            if digit > upper:
                self.possibles[digit - 1] = False

    def set_range(self, lower: int, upper: int) -> None:
        self.set_minimum(lower)
        self.set_maximum(upper)

    def fixed(self) -> bool:
        return sum(self.possibles) == 1

    def is_possible(self, digit: int) -> bool:
        return self.possibles[digit - 1]

    @staticmethod
    def letter() -> str:
        return '.'

    @property
    def rules(self) -> List[Rule]:
        return []

    @staticmethod
    def cells() -> List['Cell']:
        return list(Cell.cache.values())

    @property
    def glyphs(self) -> List[Glyph]:
        return [CellGlyph('Cell', Coord(self.row, self.column))]

    @classmethod
    def make(cls, board: Board, row: int, column: int) -> 'Cell':
        key = (row, column)
        if key in Cell.cache:
            return Cell.cache[key]
        cell = Cell(board, row, column)
        Cell.cache[key] = cell
        return cell

    @classmethod
    def make_board(cls, board: Board):
        for row, column in product(board.row_range, board.column_range):
            Cell.make(board, row, column)

    @classmethod
    def extract(cls, board: Board, yaml: Dict) -> Coord:
        return Coord.create_from_int(yaml[cls.__name__])

    @classmethod
    def create(cls, board: Board, yaml: Dict) -> Item:
        coord: Coord = Cell.extract(board, yaml)
        return cls(board, int(coord.row), int(coord.column))

    @property
    def valid(self) -> bool:
        return self.board.is_valid(self.row, self.column)

    @property
    def row_column(self) -> Tuple[int, int]:
        return self.row, self.column

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Cell):
            return self.row == other.row and self.column == other.column
        raise CellException(f"Cannot compare {object.__class__.__name__} with {self.__class__.__name__}")

    def __lt__(self, other: object) -> bool:
        if isinstance(other, Cell):
            if self.row < other.row:
                return True
            if self.row == other.row:
                return self.column < other.column
            return False
        raise CellException(f"Cannot compare {object.__class__.__name__} with {self.__class__.__name__}")

    @property
    def coord(self) -> Coord:
        return Coord(self.row, self.column)

    @property
    def row_column_string(self) -> str:
        return f"{self.row}{self.column}"

    def add_constraint(self, solver: PulpSolver, include: re.Pattern, exclude: re.Pattern) -> None:
        solver.model += lpSum(
            [
                solver.choices[digit][self.row][self.column]
                for digit in self.board.digit_range
            ]
        ) == 1

    def to_dict(self) -> Dict:
        return {self.__class__.__name__: int(self.row_column_string)}

    def css(self) -> Dict:
        return {
            '.Cell': {
                'stroke': 'black',
                'stroke-width': 1,
                'fill-opacity': 0
            }
        }

    def __str__(self) -> str:
        return f"Cell({self.row}, {self.column})"


