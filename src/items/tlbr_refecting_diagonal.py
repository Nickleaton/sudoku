from typing import List

from src.glyphs.glyph import Glyph, LineGlyph
from src.items.board import Board
from src.items.cell import Cell
from src.items.diagonals import Diagonal
from src.solvers.formulations import Formulations
from src.solvers.pulp_solver import PulpSolver
from src.utils.coord import Coord
from src.utils.rule import Rule


class TLBRReflecting(Diagonal):

    def __init__(self, board: Board):
        super().__init__(board)
        self.add_items([Cell.make(board, i, i) for i in board.row_range])

    @property
    def rules(self) -> List[Rule]:
        return [Rule('TLBRReflecting', 1, "The marked diagonal reflects parity on each side.")]

    @property
    def glyphs(self) -> List[Glyph]:
        return [
            LineGlyph('TLBRReflecting', Coord(1, 1), Coord(self.board.maximum_digit + 1, self.board.maximum_digit + 1))]

    def add_constraint(self, solver: PulpSolver) -> None:
        self.add_unique_constraint(solver)
        for row in self.board.row_range:
            for column in self.board.column_range:
                if row == column:
                    continue
                name = f"{self.name}_{row}_{column}"
                # pylint: disable=arguments-out-of-order
                start = Formulations.parity(solver, row, column)
                other = Formulations.parity(solver, column, row)
                solver.model += start == other, name
