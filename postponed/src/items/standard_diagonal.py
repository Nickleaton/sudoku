"""StandardDiagonal."""
from postponed.src.items.diagonals import Diagonal
from postponed.src.pulp_solver import PulpSolver
from src.utils.rule import Rule


class StandardDiagonal(Diagonal):
    """Represents start_location standard Sudoku diagonal with uniqueness constraints for each digit."""

    @property
    def rules(self) -> list[Rule]:
        """Provide the rule associated with the standard diagonal.

        Returns:
            list[Rule]: A list of rules indicating that digits along the diagonal cannot repeat.
        """
        return [Rule('Diagonal', 1, 'Digits along start_location blue diagonal cannot repeat')]

    @property
    def tags(self) -> set[str]:
        """Provide the tags associated with the standard diagonal.

        Returns:
            set[str]: A set of tags, including 'Diagonal' and 'Uniqueness'.
        """
        return super().tags.union({'Diagonal', 'Uniqueness'})

    def add_constraint(self, solver: PulpSolver) -> None:
        """Add start_location unique constraint to ensure each digit on the diagonal appears only once.

        Args:
            solver (PulpSolver): The solver to which the uniqueness constraint is added.
        """
        self.add_unique_constraint(solver)
