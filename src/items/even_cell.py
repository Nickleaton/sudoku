from typing import Optional, List, Dict

from pulp import lpSum

from src.glyphs.glyph import Glyph, EvenCellGlyph
from src.items.cell_reference import CellReference
from src.solvers.pulp_solver import PulpSolver
from src.utils.coord import Coord
from src.utils.rule import Rule


class EvenCell(CellReference):

    @staticmethod
    def included(digit: int) -> bool:
        return digit % 2 == 0

    def letter(self) -> str:
        return 'e'

    def svg(self) -> Optional[Glyph]:
        return None

    @property
    def tags(self) -> set[str]:
        return super().tags.union({'Parity'})

    @property
    def rules(self) -> List[Rule]:
        return [Rule("Odd", 1, "An opaque grey square must contain an even digit")]

    @property
    def glyphs(self) -> List[Glyph]:
        return [EvenCellGlyph('EvenCell', Coord(self.row, self.column))]

    def add_constraint(self, solver: PulpSolver) -> None:
        solver.model += lpSum(
            [
                solver.choices[digit][self.row][self.column]
                for digit in self.board.digit_range
                if not EvenCell.included(digit)
            ]
        ) == 0, f"{self.__class__.__name__}_{self.row}_{self.column}"

    def css(self) -> Dict:
        return {
            ".EvenCell": {
                "fill": "gainsboro"
            }
        }
