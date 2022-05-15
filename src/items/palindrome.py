from typing import List, Dict

from src.glyphs.glyph import Glyph, PolyLineGlyph
from src.items.line import Line
from src.solvers.pulp_solver import PulpSolver
from src.utils.rule import Rule


class Palindrome(Line):

    @property
    def rules(self) -> List[Rule]:
        return [Rule('Palindrome', 1, "Cells along a purple line form a palindrome")]

    @property
    def glyphs(self) -> List[Glyph]:
        return [PolyLineGlyph('Palindrome', [cell.coord for cell in self.cells], False, False)]

    @property
    def tags(self) -> set[str]:
        return super().tags.union({'Palindrome'})

    def add_constraint(self, solver: PulpSolver) -> None:
        for i in range(0, len(self) // 2):
            c1 = self.cells[i]
            c2 = self.cells[len(self) - i - 1]
            name = f"{self.name}_{i}"
            solver.model += solver.values[c1.row][c1.column] == solver.values[c2.row][c2.column], name

    def css(self) -> Dict:
        return {
            ".Palindrome": {
                "stroke": "silver",
                "stroke-width": 20,
                "stroke-linecap": "round",
                "stroke-linejoin": "round",
                "fill-opacity": 0
            }
        }
