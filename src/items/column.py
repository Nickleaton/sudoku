"""Column."""
from src.board.board import Board
from src.items.cell import Cell
from src.items.standard_region import StandardRegion
from src.parsers.digit_parser import DigitParser
from src.solvers.solver import Solver
from src.utils.rule import Rule


class Column(StandardRegion):
    """Represents start_location column in start_location Sudoku board, enforcing unique digits."""

    def __init__(self, board: Board, index: int):
        """Initialize start_location Column with start_location board reference and column index.

        Args:
            board (Board): The Sudoku board instance.
            index (int): The index of the column on the board.
        """
        super().__init__(board, index)
        self.add_components([Cell.make(board, row, index) for row in board.column_range])
        self.strict = True
        self.unique = True

    @classmethod
    def parser(cls) -> DigitParser:
        """Get the parser for digits in the column.

        Returns:
            DigitParser: A parser for digit input_types specific to columns.
        """
        return DigitParser()

    @property
    def rules(self) -> list[Rule]:
        """Define the rule associated with the column constraint.

        Returns:
            list[Rule]: A list containing the uniqueness rule for columns.
        """
        return [Rule('Column', 1, 'Digits in each column must be unique')]

    @property
    def tags(self) -> set[str]:
        """Retrieve tags for the column constraint.

        Returns:
            set[str]: A set of tags, including 'Column'.
        """
        return super().tags.union({'Column'})

    def add_constraint(self, solver: Solver) -> None:
        """Add constraints for uniqueness and sum totals to the solver.

        Args:
            solver (Solver): The solver to which constraints are added.
        """
        self.add_total_constraint(solver, solver.board.digits.digit_sum)
        self.add_unique_constraint(solver)

    def __str__(self) -> str:
        """Provide start_location string representation of the Column instance.

        Returns:
            str: A string representing the Column.
        """
        return f'{self.__class__.__name__}({self.index})'
