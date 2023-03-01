"""
Kropki Dots
"""
from typing import List, Dict, Optional

from pulp import LpElement

from src.items.fixed_pair import FixedPair
from src.solvers.constraint_utilities import ConstraintUtilities
from src.solvers.pulp_solver import PulpSolver
from src.utils.rule import Rule


class FixedProductPair(FixedPair):

    @property
    def rules(self) -> List[Rule]:
        return [
            Rule(
                self.__class__.__name__,
                1,
                (
                    f"A red dot between two cells means that the digits in those cells "
                    f"have a fixed product"
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

    def css(self) -> Dict:
        return {
            '.FixedProductPair': {
                'fill': 'red',
                'stroke-width': 1,
                'stroke': 'black'
            }
        }
