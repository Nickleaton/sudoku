import re
from typing import List

from src.glyphs.glyph import LineGlyph, Glyph
from src.items.board import Board
from src.items.cell import Cell
from src.items.standard_diagonal import StandardDiagonal
from src.solvers.pulp_solver import PulpSolver
from src.utils.coord import Coord


class BLTR(StandardDiagonal):

    def __init__(self, board: Board):
        super().__init__(board)
        self.add_items([Cell.make(board, board.maximum_digit - i + 1, i) for i in board.row_range])

    def add_constraint(self, solver: PulpSolver, include: re.Pattern, exclude: re.Pattern) -> None:
        self.add_unique_constraint(solver)

    @property
    def glyphs(self) -> List[Glyph]:
        return [LineGlyph('Diagonal', Coord(self.board.maximum_digit + 1, 1), Coord(1, self.board.maximum_digit + 1))]
