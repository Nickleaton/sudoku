from typing import List, Dict

from pulp import LpElement

from src.items.variable_pair import VariablePair
from src.solvers.pulp_solver import PulpSolver
from src.utils.rule import Rule


class FixedSumPair(VariablePair):

    @property
    def rules(self) -> List[Rule]:
        return [
            Rule(
                self.__class__.__name__,
                1,
                "Cells separated by an blue dot must have a sum the same sum"
            )
        ]

    @property
    def tags(self) -> set[str]:
        return super().tags.union({'Sum'})

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
