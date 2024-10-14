"""
Kropki Dots
"""
from typing import List, Dict, Optional

from pulp import LpElement

from src.items.variable_pair import VariablePair
from src.solvers.constraint_utilities import ConstraintUtilities
from src.solvers.pulp_solver import PulpSolver
from src.utils.rule import Rule
from src.utils.variable_type import VariableType


class VariableProductPair(VariablePair):

    @property
    def rules(self) -> List[Rule]:
        return [
            Rule(
                self.__class__.__name__,
                1,
                (
                    "A red dot between two cells means that the digits in those cells "
                    "have a fixed product"
                )
            )
        ]

    @property
    def tags(self) -> set[str]:
        return super().tags.union({'Product'})

    def target(self, solver: PulpSolver) -> Optional[LpElement]:
        x1 = ConstraintUtilities.log10_cell(solver, self.cell_1)
        x2 = ConstraintUtilities.log10_cell(solver, self.cell_2)
        return x1 + x2

    def variable_type(self) -> VariableType:
        return VariableType.LOGINT

    def css(self) -> Dict:
        return {
            '.FixedProductPair': {
                'fill': 'red',
                'stroke-width': 1,
                'stroke': 'black'
            }
        }
