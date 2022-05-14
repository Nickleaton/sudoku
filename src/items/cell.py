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


class Cell(Item):
    cache: Dict[Tuple[int, int], 'Cell'] = {}

    def __init__(self, board: Board, row: int, column: int):
        super().__init__(board)
        self.row = row
        self.column = column

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.board!r}, {self.row!r}, {self.column!r})"

    def __hash__(self):
        return self.row * self.board.maximum_digit + self.column

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
    def rc(self) -> str:
        return f"{self.row}{self.column}"

    def add_constraint(self, solver: PulpSolver) -> None:
        solver.model += lpSum(
            [
                solver.choices[digit][self.row][self.column]
                for digit in self.board.digit_range
            ]
        ) == 1

    def to_dict(self) -> Dict:
        return {self.__class__.__name__: int(self.rc)}

    def css(self) -> str:
        return (
            ".Cell {\n"
            "    stroke: black;\n"
            "    stroke-width: 1;\n"
            "    fill-opacity: 0\n"
            "}\n"
        )

    def css2(self):
        return {
            '.Cell': {
                'stroke': 'black',
                'stroke-width': 1,
                'fill-opacity': 0
            }
        }
