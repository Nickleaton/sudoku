"""
Kropki Dots
"""
from itertools import product
from typing import List

from pulp import LpVariable, LpInteger, lpSum

from src.glyphs.glyph import Glyph, KropkiGlyph
from src.items.pair import Pair
from src.solvers.pulp_solver import PulpSolver
from src.utils.rule import Rule


class KropkiPair(Pair):

    @property
    def factor(self) -> int:
        return 2

    @property
    def factor_name(self) -> str:
        return "double"

    @property
    def rules(self) -> List[Rule]:
        return [
            Rule(
                self.__class__.__name__,
                1,
                (
                    f"A black dot between two cells means that one of the digits in those cells "
                    f"is exactly {self.factor_name} the other"
                )
            )
        ]

    @property
    def glyphs(self) -> List[Glyph]:
        return [KropkiGlyph(self.__class__.__name__, self.c1.coord.center, self.c2.coord.center)]

    @property
    def tags(self) -> set[str]:
        return super().tags.union({'Kropki'})

    def add_constraint_pair(self, solver: PulpSolver, x: int, y: int) -> None:
        pass

    def add_constraint(self, solver: PulpSolver) -> None:
        # eliminate the impossible
        count = 0
        for x, y in product(self.board.digit_range, self.board.digit_range):
            choice1 = solver.choices[x][self.c1.row][self.c1.column]
            choice2 = solver.choices[y][self.c2.row][self.c2.column]
            if x == self.factor * y or self.factor * x == y:
                count += 1
            else:
                solver.model += choice1 + choice2 == 0, f"{self.name}_{x}_{y}"
        # We can only have one of the remaining choices, so create an SOS set
        sos_range = range(0, count)
        sos = LpVariable.dicts(self.name, sos_range, 0, 1, LpInteger)
        solver.model += lpSum([sos[i] for i in sos_range]) == 1, f"{self.name}_sos"

        count = 0
        for x, y in product(self.board.digit_range, self.board.digit_range):
            choice1 = solver.choices[x][self.c1.row][self.c1.column]
            choice2 = solver.choices[y][self.c2.row][self.c2.column]
            if x == self.factor * y or self.factor * x == y:
                solver.model += choice1 + choice2 + (1 - sos[count]) == 2, f"{self.name}_{x}_{y}"
                count += 1
