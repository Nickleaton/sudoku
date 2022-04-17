from typing import Optional, List

from pulp import lpSum

from src.glyphs.glyph import Glyph, OddCellGlyph
from src.items.cell_reference import CellReference
from src.solvers.pulp_solver import PulpSolver
from src.utils.coord import Coord
from src.utils.rule import Rule


class Odd(CellReference):

    @staticmethod
    def included(digit: int) -> bool:
        return digit % 2 == 1

    def svg(self) -> Optional[Glyph]:
        return None

    def letter(self) -> str:
        return 'o'

    @property
    def rules(self) -> List[Rule]:
        return [Rule("Odd", 1, "An opaque grey circle must contain an odd digit")]

    @property
    def glyphs(self) -> List[Glyph]:
        return [OddCellGlyph('OddCell', Coord(self.row, self.column))]

    @property
    def tags(self) -> set[str]:
        return super().tags.union({'Parity'})

    def add_constraint(self, solver: PulpSolver) -> None:
        solver.model += lpSum(
            [
                solver.choices[digit][self.row][self.column]
                for digit in self.board.digit_range
                if not Odd.included(digit)
            ]
        ) == 0, f"{self.__class__.__name__}_{self.row}_{self.column}"
