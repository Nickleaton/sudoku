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

    @staticmethod
    def validate(board: Board, yaml: Any) -> List[str]:
        result = []
        if not isinstance(yaml, dict):
            result.append(f"Expecting a dict got, {yaml!r}")
            return result
        if len(yaml) != 1:
            result.append(f"Expecting one item got, {yaml!r}")
        for k, v in yaml.items():
            if k != 'TLBR':
                result.append(f"Expecting TLBR, got {yaml!r}")
            if v is not None:
                result.append(f"Expecting TLBR with no values, got {yaml!r}")
        return result

    @property
    def glyphs(self) -> List[Glyph]:
        return [LineGlyph('Diagonal', Coord(1, 1), Coord(self.board.maximum_digit + 1, self.board.maximum_digit + 1))]

    def add_constraint(self, solver: PulpSolver) -> None:
        self.add_unique_constraint(solver, "TLBR")