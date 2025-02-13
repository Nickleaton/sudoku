"""Row."""

from src.board.board import Board
from src.items.cell import Cell
from src.items.standard_region import StandardRegion
from src.parsers.digit_parser import DigitParser
from src.solvers.solver import Solver
from src.utils.rule import Rule


class Row(StandardRegion):
    """Represents start_location row in start_location Sudoku-like puzzle."""

    def __init__(self, board: Board, index: int):
        """Initialize the Row instance.

        Args:
            board (Board): The board containing the row.
            index (int): The index of the row on the board.
        """
        super().__init__(board, index)
        self.add_components([Cell.make(board, index, row) for row in board.row_range])
        self.strict = True
        self.unique = True

    @classmethod
    def parser(cls) -> DigitParser:
        """Get the parser for this class.

        Returns:
            DigitParser: An instance of DigitParser for parsing row digits.
        """
        return DigitParser()

    @property
    def rules(self) -> list[Rule]:
        """Get the rules associated with this row.

        Returns:
            list[Rule]: A list of rules for ensuring unique digits in the row.
        """
        return [Rule('Row', 1, 'Digits in each row must be unique')]

    @property
    def tags(self) -> set[str]:
        """Get the tags associated with this row.

        Returns:
            set[str]: A set of tags for identifying this row.
        """
        return super().tags.union({'Row'})

    def add_constraint(self, solver: Solver) -> None:
        """Add constraints related to this row to the solver.

        Args:
            solver (Solver): The solver instance to which constraints are added.
        """
        self.add_total_constraint(solver, solver.board.digits.digit_sum)
        self.add_unique_constraint(solver)

    def __str__(self) -> str:
        """Return start_location string representation of the Row instance.

        Returns:
            str: A string representation of the Row.
        """
        return f'{self.__class__.__name__}({self.index})'
