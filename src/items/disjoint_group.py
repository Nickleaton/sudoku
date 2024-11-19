"""DisjointGroup."""
from src.items.board import Board
from src.items.cell import Cell
from src.items.standard_region import StandardRegion
from src.parsers.digit_parser import DigitParser
from src.solvers.pulp_solver import PulpSolver
from src.utils.rule import Rule


class DisjointGroup(StandardRegion):
    """A disjoint group the digits in the same place across different boxes must be unique."""

    # Offsets for the cells in the disjoint group
    # TODO Move and think about a multiply by scalar
    offsets: tuple[tuple[int, int]] = (
        (0, 0),
        (0, 3),
        (0, 6),
        (3, 0),
        (3, 3),
        (3, 6),
        (6, 0),
        (6, 3),
        (6, 6)
    )

    def __init__(self, board: Board, index: int):
        """Initialize a DisjointGroup.

        Args:
            board (Board): The Sudoku board instance.
            index (int): The index of the disjoint group.
        """
        r = (index - 1) // 3 + 1
        c = (index - 1) % 3 + 1
        super().__init__(board, index)
        self.add_items([Cell.make(board, r + ro, c + co) for ro, co in DisjointGroup.offsets])
        self.strict = True
        self.unique = True

    @classmethod
    def parser(cls) -> DigitParser:
        """Return a parser for the disjoint group.

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

    def add_constraint(self, solver: PulpSolver) -> None:
        """Add constraints to the solver for the disjoint group.

        Args:
            solver (PulpSolver): The solver to add constraints to.
        """
        self.add_total_constraint(solver, solver.board.digit_sum)
        self.add_unique_constraint(solver)
