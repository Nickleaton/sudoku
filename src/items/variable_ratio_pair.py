"""
Kropki Dots
"""
from math import ceil, log10
from typing import List, Dict

from pulp import LpElement

from src.items.variable_pair import VariablePair
from src.solvers.constraint_utilities import ConstraintUtilities
from src.solvers.formulations import Formulations
from src.solvers.pulp_solver import PulpSolver
from src.utils.rule import Rule
from src.utils.variable_type import VariableType


class VariableRatioPair(VariablePair):

    @property
    def rules(self) -> List[Rule]:
        return [
            Rule(
                self.__class__.__name__,
                1,
                (
                    "A black dot between two cells means that one of the digits in those cells "
                    "have a fixed ratio. The ratio is not necessarily an integer"
                )
            )
        ]

    @property
    def tags(self) -> set[str]:
        return super().tags.union({'Ratio'})

    def variable_type(self) -> VariableType:
        return VariableType.LOGFLOAT

    def target(self, solver: PulpSolver) -> LpElement:
        limit = ceil(log10(self.board.maximum_digit)) + 1
        x1 = ConstraintUtilities.log10_cell(solver, self.cell_1)
        x2 = ConstraintUtilities.log10_cell(solver, self.cell_2)
        return Formulations.abs(
            solver.model,
            x1,
            x2,
            limit
        )

    def css(self) -> Dict:
        return {
            '.FixedRatioPair': {
                'fill': 'black',
                'stroke-width': 1,
                'stroke': 'black'
            }
        }
