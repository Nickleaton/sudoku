from typing import List, Dict

from pulp import LpElement

from src.items.pair import Pair
from src.solvers.pulp_solver import PulpSolver
from src.utils.rule import Rule


class SumPair(Pair):

    @property
    def tags(self) -> set[str]:
        return super().tags.union({'Sum'})

    @property
    def rules(self) -> List[Rule]:
        return [
            Rule(
                self.__class__.__name__,
                1,
                f"Cells separated by an blue dot must have a sum"
            )
        ]

    def target(self, solver: PulpSolver) -> LpElement:
        return solver.values[self.cell_1.row][self.cell_1.column] + solver.values[self.cell_2.row][self.cell_2.column]

    def css(self) -> Dict:
        return {
            '.FixedSumPair': {
                'fill': 'cyan',
                'stroke-width': 1,
                'stroke': 'black'
            }
        }
