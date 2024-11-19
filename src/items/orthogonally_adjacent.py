"""OrthogonallyAdjacent."""
from itertools import product

from src.items.board import Board
from src.items.composed_item import ComposedItem
from src.items.item import Item
from src.solvers.pulp_solver import PulpSolver
from src.utils.direction import Direction
from src.utils.rule import Rule


class OrthogonallyAdjacent(ComposedItem):
    """Represent a region where consecutive digits are restricted from being orthogonally adjacent."""

    def __init__(self, board: Board):
        """Initialize the OrthogonallyAdjacent constraint on the given board.

        Args:
            board (Board): The Sudoku board to which the constraint applies.
        """
        super().__init__(board, [])

    @property
    def tags(self) -> set[str]:
        """Return a set of tags associated with this constraint.

        Returns:
            set[str]: Tags including 'OrthogonallyAdjacent'.
        """
        return super().tags.union({'OrthogonallyAdjacent'})

    @classmethod
    def create(cls, board: Board, yaml: dict) -> Item:
        """Create an OrthogonallyAdjacent constraint from YAML configuration.

        Args:
            board (Board): The board on which this constraint is created.
            yaml (dict): YAML configuration for the constraint.

        Returns:
            Item: The instantiated OrthogonallyAdjacent constraint.
        """
        return OrthogonallyAdjacent(board)

    @property
    def rules(self) -> list[Rule]:
        """Return the list of rules enforced by this constraint.

        Returns:
            list[Rule]: Rules indicating that consecutive digits cannot be orthogonally adjacent.
        """
        return [
            Rule("OrthogonallyAdjacent", 1, "Consecutive digits must never be orthogonally adjacent")
        ]

    def __repr__(self) -> str:
        """Return a string representation of the OrthogonallyAdjacent constraint.

        Returns:
            str: String representation of the constraint.
        """
        return f"{self.__class__.__name__}({self.board!r})"

    def to_dict(self) -> dict:
        """Serialize the OrthogonallyAdjacent constraint to a dictionary format.

        Returns:
            dict: Dictionary representation of the constraint.
        """
        return {self.__class__.__name__: None}

    # pylint: disable=loop-invariant-statement
    def add_constraint(self, solver: PulpSolver) -> None:
        """Add the orthogonally adjacent constraint to the solver.

        Args:
            solver (PulpSolver): The solver to which the constraint is added.
        """
        for row, column in product(self.board.row_range, self.board.row_range):
            for offset in Direction.orthogonals():
                if not self.board.is_valid(int(row + offset.row), int(column + offset.column)):
                    continue
                for digit in self.board.digit_range:
                    if digit + 1 > self.board.maximum_digit:
                        continue
                    if digit - 1 < 1:
                        continue
                    lhs = solver.choices[digit][row][column]
                    prefix = f"{self.name}_{row}_{column}_{row + offset.row}_{row + offset.column}_{digit}"

                    rhs_1 = solver.choices[digit + 1][row + offset.row][column + offset.column]
                    solver.model += lhs + rhs_1 <= 1, f"{prefix}_{digit + 1}"

                    rhs_2 = solver.choices[digit - 1][row + offset.row][column + offset.column]
                    solver.model += lhs + rhs_2 <= 1, f"{prefix}_{digit - 1}"
