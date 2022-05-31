import re
from typing import List, Optional

from src.items.diagonals import Diagonal
from src.solvers.pulp_solver import PulpSolver
from src.utils.rule import Rule


class StandardDiagonal(Diagonal):

    @property
    def rules(self) -> List[Rule]:
        return [Rule('Diagonal', 1, "Digits along a blue diagonal cannot repeat")]

    @property
    def tags(self) -> set[str]:
        return super().tags.union({'Diagonal', 'Uniqueness'})

    def add_constraint(self, solver: PulpSolver, include: Optional[re.Pattern], exclude: Optional[re.Pattern]) -> None:
        self.add_unique_constraint(solver)
