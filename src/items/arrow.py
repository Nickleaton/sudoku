from typing import List

from pulp import lpSum

from src.glyphs.glyph import Glyph, ArrowLineGlyph
from src.items.board import Board
from src.items.cell import Cell
from src.items.line import Line
from src.solvers.pulp_solver import PulpSolver
from src.utils.rule import Rule


class Arrow(Line):

    @property
    def rules(self) -> List[Rule]:
        return [
            Rule(
                'Arrow',
                1,
                "Digits along an arrow must sum to the digit in its circle. Digits may repeat along an arrow"
            )
        ]

    @property
    def glyphs(self) -> List[Glyph]:
        return [ArrowLineGlyph('Arrow', [cell.coord for cell in self.cells])]

    @property
    def tags(self) -> set[str]:
        return super().tags.union({'Arrow', 'Sum'})

    @classmethod
    def create(cls, name: str, board: Board, yaml) -> 'Arrow':
        cells = [Cell.make(board, r, c) for r, c in yaml]
        return cls(board, cells)

    def add_constraint(self, solver: PulpSolver) -> None:
        name = f"{self.__class__.__name__}_ {self.cells[0].row}_{self.cells[0].column}"
        total = lpSum([solver.values[self.cells[i].row][self.cells[i].column] for i in range(1, len(self))])
        solver.model += total == solver.values[self.cells[0].row][self.cells[0].column], name
