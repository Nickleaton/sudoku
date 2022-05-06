from typing import List, Any

from src.glyphs.glyph import Glyph, LineGlyph
from src.items.board import Board
from src.items.cell import Cell
from src.items.diagonals import Diagonal
from src.solvers.pulp_solver import PulpSolver
from src.utils.coord import Coord


class TLBR(Diagonal):

    def __init__(self, board: Board):
        super().__init__(board)
        self.add_items([Cell.make(board, i, i) for i in board.row_range])

    @property
    def glyphs(self) -> List[Glyph]:
        return [LineGlyph('Diagonal', Coord(1, 1), Coord(self.board.maximum_digit + 1, self.board.maximum_digit + 1))]

    def add_constraint(self, solver: PulpSolver) -> None:
        self.add_unique_constraint(solver)
