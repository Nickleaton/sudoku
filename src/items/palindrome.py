from typing import Optional, List

from src.glyphs.glyph import Glyph, PolyLineGlyph
from src.items.board import Board
from src.items.cell import Cell
from src.items.line import Line
from src.solvers.pulp_solver import PulpSolver
from src.utils.rule import Rule


class Palindrome(Line):

    def __init__(self, board: Board, cells: Optional[List[Cell]]):
        super().__init__(board, cells)

    @property
    def rules(self) -> List[Rule]:
        return [Rule('Palindrome', 1, "Cells along a purple line form a palindrome")]

    @property
    def glyphs(self) -> List[Glyph]:
        return [PolyLineGlyph('Palindrome', [cell.coord for cell in self.items], False, False)]

    @property
    def tags(self) -> set[str]:
        return super().tags.union({'Palindrome'})

    def add_constraint(self, solver: PulpSolver) -> None:
        for i in range(0, len(self) // 2):
            c1 = self.items[i]
            c2 = self.items[len(self) - i - 1]
            name = f"{self.__class__.__name__}_{c1.row}_{c1.column}_{c2.row}_{c2.column}"
            solver.model += solver.values[c1.row][c1.column] == solver.values[c2.row][c2.column],name
