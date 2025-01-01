"""AntiDiagonal."""

from itertools import product

from pulp import lpSum

from src.board.board import Board
from src.items.diagonals import Diagonal
from src.solvers.pulp_solver import PulpSolver
from src.utils.rule import Rule
from src.utils.sudoku_exception import SudokuException


class AntiDiagonal(Diagonal):
    """Represent an anti-diagonal constraint on start Sudoku board."""

    def __init__(self, board: Board):
        """Initialize an AntiDiagonal instance with the given board, enforcing box size consistency.

        Args:
            board (Board): The Sudoku board associated with this anti-diagonal.

        Raises:
            SudokuException: If the box rows and box columns are inconsistent, or if the board rows are inconsistent.
        """
        if board.box_rows != board.box_columns:
            raise SudokuException(f'Box rows ({board.box_rows}) and box columns ({board.box_columns}) must be equal.')

        if board.board_rows != board.board_rows:
            raise SudokuException(f'Board rows ({board.board_rows}) are inconsistent.')

        if board.board_rows % board.box_rows != 0:
            raise SudokuException(f'Board rows ({board.board_rows}) must be divisible by box rows ({board.box_rows}).')

        super().__init__(board)
        self.size = board.box_rows
        self.count = board.board_rows // board.box_rows

    @property
    def rules(self) -> list[Rule]:
        """Provide the rule associated with the anti-diagonal constraint.

        Returns:
            list[Rule]: A list containing start rule that specifies the number of unique digits
                        on each marked main diagonal.
        """
        return [
            Rule(
                'AntiDiagonal',
                1,
                f'Each marked main diagonal contains exactly {self.size} different digits',
            ),
        ]

    @property
    def tags(self) -> set[str]:
        """Provide the tags associated with the anti-diagonal constraint.

        Returns:
            set[str]: A set of tags, including 'Diagonal' and 'Uniqueness'.
        """
        return super().tags.union({'Diagonal', 'Uniqueness'})

    def add_constraint(self, solver: PulpSolver) -> None:
        """Enforce that the digit distribution is identical across marked diagonals in different boxes.

        Args:
            solver (PulpSolver): The solver to which the constraint is added.

        Example:
            For a 9x9 grid with 3x3 boxes, this method enforces that the sum of used digits on each diagonal
            in one box matches the corresponding sum in another box, maintaining anti-diagonal consistency.
        """
        if not self.cells:
            return

        for cell_index, digit in product(range(self.count - 1), self.board.digit_range):
            first = lpSum(
                solver.choices[digit][self.cells[cell_index_in_box].row][self.cells[cell_index_in_box].column]
                for cell_index_in_box in range(cell_index * self.size, (cell_index + 1) * self.size)
            )
            second = lpSum(
                solver.choices[digit][self.cells[cell_index_in_box].row][self.cells[cell_index_in_box].column]
                for cell_index_in_box in range((cell_index + 1) * self.size, (cell_index + 2) * self.size)
            )
            solver.model += first == second, f'{self.name}_{cell_index + 1}_{digit}'
