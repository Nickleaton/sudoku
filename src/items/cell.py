from itertools import product
from typing import Dict, Tuple, List, Any

from pulp import lpSum

from src.glyphs.glyph import Glyph, CellGlyph
from src.items.board import Board
from src.items.item import Item, YAML
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

    @property
    def name(self) -> str:
        return f"{self.__class__.__name__}_{self.row}_{self.column})"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.board!r}, {self.row!r}, {self.column!r})"

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

    @staticmethod
    def validate(board: Board, yaml: Any) -> List[str]:
        result = []
        if not isinstance(yaml, dict):
            result.append(f"Expecting dict, got {yaml!r}")
            return result
        if len(yaml) != 2:
            result.append(f"Expecting Row and Column only, got {yaml!r}")

        if 'Row' not in yaml:
            result.append(f"Expecting 'Row', got {yaml!r}")
        if 'Column' not in yaml:
            result.append(f"Expecting 'Column', got {yaml!r}")
        if len(result) > 0:
            return result
        row = int(yaml['Row'])
        column = int(yaml['Column'])
        if row not in board.row_range:
            result.append(f'Invalid row {row}')
        if column not in board.column_range:
            result.append(f'Invalid column {column}')
        return result

    @staticmethod
    def extract(_: Board, yaml: Any) -> Coord:
        return Coord(yaml['Row'], yaml['Column'])

    @classmethod
    def create(cls, name: str, board: Board, yaml: YAML) -> Item:
        Cell.validate(board, yaml)
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

    def add_constraint(self, solver: PulpSolver) -> None:
        solver.model += lpSum(
            [
                solver.choices[digit][self.row][self.column]
                for digit in self.board.digit_range
            ]
        ) == 1
