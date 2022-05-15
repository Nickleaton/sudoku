from typing import Dict

from src.items.sum_pair import SumPair
from src.solvers.pulp_solver import PulpSolver


class VPair(SumPair):

    @property
    def total(self) -> int:
        return 5

    @property
    def tags(self) -> set[str]:
        return super().tags.union({'V'})

    @property
    def label(self) -> str:
        return "V"

    def add_constraint(self, solver: PulpSolver) -> None:
        super().add_constraint(solver)
        self.add_unique_constraint(solver, True)
        self.add_allowed_constraint(solver, self.cells, [1, 2, 3, 4])

    def css(self) -> Dict:
        return {
            ".VPairForeground": {
                "font-size": "30px",
                "stroke": "black",
                "stroke-width": 1,
                "fill": "black"
            },
            ".VPairBackground": {
                "font-size": "30px",
                "stroke": "white",
                "stroke-width": 8,
                "fill": "white",
                "font-weight": "bolder"
            }
        }
