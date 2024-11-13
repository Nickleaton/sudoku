from typing import List

from pulp import lpSum

from src.items.board import Board
from src.items.diagonals import Diagonal
from src.solvers.pulp_solver import PulpSolver
from src.utils.rule import Rule


class AntiDiagonal(Diagonal):
    """
    Represents an anti-diagonal constraint on a Sudoku board, enforcing uniqueness of digits along specified diagonals.
    """

    def __init__(self, board: Board):
        """
        Initializes an AntiDiagonal instance with the given board, enforcing box size consistency.

        Args:
            board (Board): The Sudoku board associated with this anti-diagonal.
        """
        assert board.box_rows == board.box_columns
        assert board.board_rows == board.board_rows
        assert board.board_rows % board.box_rows == 0
        super().__init__(board)
        self.size = board.box_rows
        self.count = board.board_rows // board.box_rows

    @property
    def rules(self) -> List[Rule]:
        """
        Provides the rule associated with the anti-diagonal constraint.

        Returns:
            List[Rule]: A list containing a rule that specifies the number of unique digits
                        on each marked main diagonal.
        """
        return [
            Rule(
                'AntiDiagonal',
                1,
                f"Each marked main diagonal contains exactly {self.size} different digits"
            )
        ]

    @property
    def tags(self) -> set[str]:
        """
        Provides the tags associated with the anti-diagonal constraint.

        Returns:
            set[str]: A set of tags, including 'Diagonal' and 'Uniqueness'.
        """
        return super().tags.union({'Diagonal', 'Uniqueness'})

    def add_constraint(self, solver: PulpSolver) -> None:
        """
        Adds a constraint to enforce that the digit distribution is identical
        across marked diagonals in different boxes.

        Args:
            solver (PulpSolver): The solver to which the constraint is added.

        Example:
            For a 9x9 grid with 3x3 boxes, this method enforces that the sum of used digits on each diagonal
            in one box matches the corresponding sum in another box, maintaining anti-diagonal consistency.
        """
        if len(self.cells) == 0:
            return
        for b in range(0, self.count - 1):
            for digit in self.board.digit_range:
                first = lpSum(
                    solver.choices[digit][self.cells[x].row][self.cells[x].column]
                    for x in range(b * self.size, (b + 1) * self.size)
                )
                second = lpSum(
                    solver.choices[digit][self.cells[x].row][self.cells[x].column]
                    for x in range((b + 1) * self.size, (b + 2) * self.size)
                )
                solver.model += first == second, f"{self.name}_{b + 1}_{digit}"
