"""AntiDiagonal."""
from typing import List

from pulp import lpSum

from src.items.board import Board
from src.items.diagonals import Diagonal
from src.solvers.pulp_solver import PulpSolver
from src.utils.rule import Rule
from src.utils.sudoku_exception import SudokuException


class AntiDiagonal(Diagonal):
    """Represent an anti-diagonal constraint on a Sudoku board."""

    def __init__(self, board: Board):
        """Initialize an AntiDiagonal instance with the given board, enforcing box size consistency.

        Args:
            board (Board): The Sudoku board associated with this anti-diagonal.
        """
        if board.box_rows != board.box_columns:
            raise SudokuException(f"Box rows ({board.box_rows}) and box columns ({board.box_columns}) must be equal.")

        if board.board_rows != board.board_rows:
            raise SudokuException(f"Board rows ({board.board_rows}) are inconsistent.")

        if board.board_rows % board.box_rows != 0:
            raise SudokuException(f"Board rows ({board.board_rows}) must be divisible by box rows ({board.box_rows}).")

        super().__init__(board)
        self.size = board.box_rows
        self.count = board.board_rows // board.box_rows

    @property
    def rules(self) -> List[Rule]:
        """Provide the rule associated with the anti-diagonal constraint.

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
        """Provide the tags associated with the anti-diagonal constraint.

        Returns:
            set[str]: A set of tags, including 'Diagonal' and 'Uniqueness'.
        """
        return super().tags.union({'Diagonal', 'Uniqueness'})

    # pylint: disable=loop-invariant-statement
    def add_constraint(self, solver: PulpSolver) -> None:
        """Enforce that the digit distribution is identical across marked diagonals in different boxes.

        Args:
            solver (PulpSolver): The solver to which the constraint is added.

        Example:
            For a 9x9 grid with 3x3 boxes, this method enforces that the sum of used digits on each diagonal
            in one box matches the corresponding sum in another box, maintaining anti-diagonal consistency.
        """
        if len(self.cells) == 0:
            return
        for b in range(self.count - 1):
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
