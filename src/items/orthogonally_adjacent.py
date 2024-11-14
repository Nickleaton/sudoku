from itertools import product
from typing import List, Dict

from src.items.board import Board
from src.items.composed_item import ComposedItem
from src.items.item import Item
from src.solvers.pulp_solver import PulpSolver
from src.utils.direction import Direction
from src.utils.rule import Rule


class OrthogonallyAdjacent(ComposedItem):
    """Represents a region where consecutive digits are restricted from being orthogonally adjacent."""

    def __init__(self, board: Board):
        """Initializes the OrthogonallyAdjacent constraint on the given board.

        Args:
            board (Board): The Sudoku board to which the constraint applies.
        """
        super().__init__(board, [])

    @property
    def tags(self) -> set[str]:
        """Returns a set of tags associated with this constraint.

        Returns:
            set[str]: Tags including 'OrthogonallyAdjacent'.
        """
        return super().tags.union({'OrthogonallyAdjacent'})

    @classmethod
    def create(cls, board: Board, yaml: Dict) -> Item:
        """Factory method to create an OrthogonallyAdjacent constraint from YAML configuration.

        Args:
            board (Board): The board on which this constraint is created.
            yaml (Dict): YAML configuration for the constraint.

        Returns:
            Item: The instantiated OrthogonallyAdjacent constraint.
        """
        return OrthogonallyAdjacent(board)

    @property
    def rules(self) -> List[Rule]:
        """Returns the list of rules enforced by this constraint.

        Returns:
            List[Rule]: Rules indicating that consecutive digits cannot be orthogonally adjacent.
        """
        return [
            Rule("OrthogonallyAdjacent", 1, "Consecutive digits must never be orthogonally adjacent")
        ]

    def __repr__(self) -> str:
        """Returns a string representation of the OrthogonallyAdjacent constraint.

        Returns:
            str: String representation of the constraint.
        """
        return f"{self.__class__.__name__}({self.board!r})"

    def to_dict(self) -> Dict:
        """Serializes the OrthogonallyAdjacent constraint to a dictionary format.

        Returns:
            Dict: Dictionary representation of the constraint.
        """
        return {self.__class__.__name__: None}

    def add_constraint(self, solver: PulpSolver) -> None:
        """Adds the orthogonally adjacent constraint to the solver.

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
