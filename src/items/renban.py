from typing import List, Sequence, Optional

from pulp import LpVariable, LpInteger

from src.glyphs.glyph import Glyph, PolyLineGlyph
from src.items.board import Board
from src.items.cell import Cell
from src.items.line import Line
from src.solvers.pulp_solver import PulpSolver
from src.utils.bound import Bounds
from src.utils.rule import Rule


class Renban(Line):

    def __init__(self, board: Board, cells: Sequence[Cell]):
        super().__init__(board, cells)

    @property
    def name(self) -> str:
        if self.identity is None:
            return super().name
        return f"{self.__class__.__name__}_{self.identity}"

    @property
    def rules(self) -> List[Rule]:
        return [
            Rule(
                'Renban',
                1,
                "Pink lines must contain a set of consecutive, non-repeating digits, in any order"
            )
        ]

    @property
    def glyphs(self) -> List[Glyph]:
        return [PolyLineGlyph('Renban', [cell.coord for cell in self.cells], False, False)]

    @property
    def tags(self) -> set[str]:
        return super().tags.union({'Renban', 'Adjacent', 'Set'})

    def add_variables(self, board: Board, solver: PulpSolver) -> None:
        self.identity = len(solver.renbans) + 1
        solver.renbans[self.name] = {}
        for bound in Bounds:
            var = LpVariable(f"{self.name}_{bound.name}", 1, board.maximum_digit, LpInteger)
            solver.renbans[self.name][bound.name] = var

    def add_constraint(self, solver: PulpSolver) -> None:
        # unique on lines
        self.add_unique_constraint(solver)

        # lower and upper bounds for the line.
        # Upper is greater than or equal to all values on the line
        # Lower is less than or equal to all values on the line
        # The difference of the lower and the upper is the length of the line less one.

        # eg. 4 6 5 on the line. We have to force upper - lower = 3 - 1
        # 6 - 4 = 2 = length - 1 = 3 - 1 = 2

        lower = solver.renbans[self.name][Bounds.LOWER.name]
        upper = solver.renbans[self.name][Bounds.UPPER.name]

        # handle upper and lower
        for cell in self.cells:
            value = solver.values[cell.row][cell.column]
            solver.model += lower <= value, f"{self.name}_lower_{cell.row}_{cell.column}"
            solver.model += upper >= value, f"{self.name}_upper_{cell.row}_{cell.column}"

        # set the difference constraint
        solver.model += upper - lower == len(self.cells) - 1, f"{self.name}_range_{len(self.cells) - 1}"
