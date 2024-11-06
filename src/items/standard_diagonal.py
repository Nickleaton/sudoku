from typing import List

from src.items.diagonals import Diagonal
from src.solvers.pulp_solver import PulpSolver
from src.utils.rule import Rule


class StandardDiagonal(Diagonal):
    """Represents a standard Sudoku diagonal with uniqueness constraints for each digit."""

    @property
    def rules(self) -> List[Rule]:
        """
        Provides the rule associated with the standard diagonal.

        Returns:
            List[Rule]: A list of rules indicating that digits along the diagonal cannot repeat.
        """
        return [Rule('Diagonal', 1, "Digits along a blue diagonal cannot repeat")]

    @property
    def tags(self) -> set[str]:
        """
        Provides the tags associated with the standard diagonal.

        Returns:
            set[str]: A set of tags, including 'Diagonal' and 'Uniqueness'.
        """
        return super().tags.union({'Diagonal', 'Uniqueness'})

    def add_constraint(self, solver: PulpSolver) -> None:
        """
        Adds a unique constraint to ensure each digit on the diagonal appears only once.

        Args:
            solver (PulpSolver): The solver to which the uniqueness constraint is added.
        """
        self.add_unique_constraint(solver)
