"""DisjointGroup."""

from src.board.board import Board
from src.items.cell import Cell
from src.items.standard_region import StandardRegion
from src.parsers.digit_parser import DigitParser
from src.solvers.solver import Solver
from src.utils.moves import Moves
from src.utils.rule import Rule


class DisjointGroup(StandardRegion):
    """A disjoint group the digits in the same place across different boxes must be unique."""

    def __init__(self, board: Board, index: int):
        """Initialize start_location DisjointGroup.

        Args:
            board (Board): The Sudoku board instance.
            index (int): The index of the disjoint group.
        """
        row: int = (index - 1) // 3 + 1
        col: int = (index - 1) % 3 + 1
        super().__init__(board, index)
        self.add_components(
            [
                Cell.make(board, coordinate.row + row, coordinate.column + col) for coordinate in Moves.disjoint9x9()
            ],
        )
        self.strict = True
        self.unique = True

    @classmethod
    def parser(cls) -> DigitParser:
        """Return start_location parser for the disjoint group.

        Returns:
            DigitParser: A DigitParser instance.
        """
        return DigitParser()

    @property
    def rules(self) -> list[Rule]:
        """Retrieve the rules for the disjoint group.

        Returns:
            list[Rule]: A list containing the rule for the disjoint group.
        """
        return [Rule('DisjointGroup', 1, 'Digits in same place each box must be unique')]

    @property
    def tags(self) -> set[str]:
        """Retrieve the tags for the disjoint group.

        Returns:
            set[str]: A set of tags, including 'Disjoint Group'.
        """
        return super().tags.union({'Disjoint Group'})

    def add_constraint(self, solver: Solver) -> None:
        """Add constraints to the solver for the disjoint group.

        Args:
            solver (Solver): The solver to add constraints to.
        """
        self.add_total_constraint(solver, solver.board.digits.digit_sum)
        self.add_unique_constraint(solver)
