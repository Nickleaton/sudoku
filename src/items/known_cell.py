from typing import List, Any, Tuple

from src.glyphs.glyph import Glyph, KnownGlyph
from src.items.board import Board
from src.items.cell_reference import CellReference
from src.items.item import Item, YAML
from src.solvers.pulp_solver import PulpSolver
from src.utils.coord import Coord


class KnownCell(CellReference):

    def __init__(self, board: Board, row: int, column: int, digit: int):
        super().__init__(board, row, column)
        self.digit = int(digit)

    def add_constraint(self, solver: PulpSolver) -> None:
        solver.model += solver.choices[self.digit][self.row][self.column] == 1, \
                        f"Known_{self.row}_{self.column}_eq_{self.digit}"

    @staticmethod
    def validate(board: Board, yaml: Any) -> List[str]:
        result: List[str] = []
        if not isinstance(yaml, dict):
            result.append(f"Expecting dict, got {yaml!r}")
            return result
        if len(yaml) != 3:
            result.append(f"Row, Column and digit {yaml!r}")
        if 'Row' not in yaml:
            result.append(f"Row:, got {yaml!r}")
        if 'Column' not in yaml:
            result.append(f"Column:, got {yaml!r}")
        if 'Digit' not in yaml:
            result.append(f"Digit:, got {yaml!r}")
        if len(result) > 0:
            return result
        if yaml['Row'] not in board.row_range:
            result.append(f"Invalid row:, got {yaml!r}")
        if yaml['Column'] not in board.column_range:
            result.append(f"Invalid column:, got {yaml!r}")
        if yaml['Digit'] not in board.digit_range:
            result.append(f"Invalid digit:, got {yaml!r}")
        return result

    @staticmethod
    def extract(_: Board, yaml: Any) -> Tuple:
        return int(yaml['Row']), int(yaml['Column']), int(yaml['Digit'])

    @classmethod
    def create(cls, name: str, board: Board, yaml: YAML) -> Item:
        KnownCell.validate(board, yaml)
        row, column, digit = KnownCell.extract(board, yaml)
        return cls(board, row, column, digit)

    def letter(self) -> str:
        return str(self.digit)

    @property
    def glyphs(self) -> List[Glyph]:
        return [KnownGlyph('Known', Coord(self.row, self.column), self.digit)]

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.board!r}, {self.cell!r}, {self.digit!r})"
