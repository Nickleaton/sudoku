from typing import List, Dict

from pulp import LpElement

from src.items.variable_pair import VariablePair
from src.solvers.formulations import Formulations
from src.solvers.pulp_solver import PulpSolver
from src.utils.rule import Rule
from src.utils.variable_type import VariableType


class VariableDifferencePair(VariablePair):

    @property
    def rules(self) -> List[Rule]:
        return [
            Rule(
                self.__class__.__name__,
                1,
                (
                    f"A white dot between two cells means that the digits in those cells "
                    f"have a fixed difference."
                )
            )
        ]

    def variable_type(self) -> VariableType:
        return VariableType.INT

    @property
    def tags(self) -> set[str]:
        return super().tags.union({'Difference'})

    def target(self, solver: PulpSolver) -> LpElement:
        v1 = solver.values[self.cell_1.row][self.cell_1.column]
        v2 = solver.values[self.cell_2.row][self.cell_2.column]
        return Formulations.abs(solver.model, v1, v2, self.board.maximum_digit + 1)

    def css(self) -> Dict:
        return {
            '.FixedDifferencePair': {
                'fill': 'white',
                'stroke-width': 1,
                'stroke': 'black'
            }
        }
