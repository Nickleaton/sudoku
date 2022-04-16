from typing import Dict, List

from src.glyphs.glyph import Glyph, KnownGlyph
from src.items.board import Board
from src.items.cell_reference import CellReference
from src.items.item import Item
from src.solvers.pulp_solver import PulpSolver
from src.utils.coord import Coord


class KnownCell(CellReference):

    def __init__(self, board: Board, row: int, column: int, digit: int):
        super().__init__(board, row, column)
        self.digit = int(digit)

    def add_constraint(self, solver: PulpSolver) -> None:
        solver.model += solver.choices[self.digit][self.row][self.column] == 1, \
                        f"Known_{self.row}_{self.column}_eq_{self.digit}"

    @classmethod
    def create(cls, name: str, board: Board, yaml: Dict | List | str | int | None) -> Item:
        Item.check_yaml_dict(yaml)
        row = yaml['Row']
        column = yaml['Column']
        digit = yaml['Digit']
        return cls(board, row, column, digit)

    def letter(self) -> str:
        return str(self.digit)

    @property
    def glyphs(self) -> List[Glyph]:
        return [KnownGlyph('Known', Coord(self.row, self.column), self.digit)]

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.board!r}, {self.cell!r}, {self.digit!r})"
