from typing import List

from src.glyphs.glyph import Glyph, ConsecutiveGlyph
from src.items.difference_pair import DifferencePair
from src.solvers.pulp_solver import PulpSolver
from src.utils.rule import Rule


class ConsecutivePair(DifferencePair):

    @property
    def difference(self):
        return 1

    @property
    def rules(self) -> List[Rule]:
        return [Rule("ConsecutivePair", 1, "Cells separated by a white dot must be consecutive")]

    @property
    def tags(self) -> set[str]:
        return super().tags.union({'Consecutive'})

    @property
    def glyphs(self) -> List[Glyph]:
        return [ConsecutiveGlyph(self.__class__.__name__, self.c1.coord.center, self.c2.coord.center)]

    def add_constraint(self, solver: PulpSolver) -> None:
        value1 = solver.values[self.c1.row][self.c1.column]
        value2 = solver.values[self.c2.row][self.c2.column]
        diff = value1 - value2
        solver.model += diff <= self.difference, f"{self.name}_upper"
        solver.model += -diff <= self.difference, f"{self.name}_lower"
