from typing import List, Callable

from src.glyphs.glyph import Glyph
from src.glyphs.line_glyph import LineGlyph
from src.items.board import Board
from src.items.cell import Cell
from src.items.item import Item
from src.items.standard_diagonal import StandardDiagonal
from src.solvers.pulp_solver import PulpSolver
from src.utils.coord import Coord


class BLTR(StandardDiagonal):

    def __init__(self, board: Board):
        super().__init__(board)
        self.add_items([Cell.make(board, board.maximum_digit - i + 1, i) for i in board.row_range])

    def add_constraint(self, solver: PulpSolver) -> None:
        self.add_unique_constraint(solver)

    def glyphs(self) -> List[Glyph]:
        return [LineGlyph('Diagonal', Coord(self.board.maximum_digit + 1, 1), Coord(1, self.board.maximum_digit + 1))]
