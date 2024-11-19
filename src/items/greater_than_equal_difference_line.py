"""GreaterThanEqualDifferenceLine."""

from pulp import lpSum

from src.items.board import Board
from src.items.box import Box
from src.items.cell import Cell
from src.items.column import Column
from src.items.difference_line import DifferenceLine
from src.items.greater_than_equal_difference_pair import GreaterThanEqualDifferencePair
from src.items.row import Row
from src.solvers.pulp_solver import PulpSolver
from src.utils.rule import Rule


class GreaterThanEqualDifferenceLine(DifferenceLine):
    """Enforces a minimum difference between adjacent cells in a line."""

    def __init__(self, board: Board, cells: Sequence[Cell], difference: int = 0):
        """Initialize the GreaterThanEqualDifferenceLine.

        Args:
            board (Board): The Sudoku board containing the cells.
            cells (Sequence[Cell]): The sequence of cells forming the difference line.
            difference (int, optional): The minimum difference between consecutive cells.
            Defaults to 0.
        """
        super().__init__(board, cells, difference)
        for i in range(1, len(cells)):
            self.add(GreaterThanEqualDifferencePair(self.board, cells[i - 1], cells[i], self.difference))

    def __repr__(self) -> str:
        """Return a string representation of the instance."""
        return f"{self.__class__.__name__}({self.board!r}, {self.cells!r}, {self.difference})"

    @property
    def rules(self) -> list[Rule]:
        """Return the rules for the greater-than-equal difference.

        Returns:
            list[Rule]: A list of rules for the constraint.
        """
        return [
            Rule(
                self.__class__.__name__,
                1,
                f"Any two cells directly connected by a line must have a difference of at least {self.difference}"
            )
        ]

    @property
    def tags(self) -> set[str]:
        """Return the tags associated with this constraint.

        Returns:
            set[str]: A set of tags for the constraint.
        """
        return super().tags.union({'Difference', 'Comparison'})

    @staticmethod
    # pylint: disable=loop-invariant-statement
    def get_regions(cell: Cell) -> set:
        """Get the regions that the given cell belongs to.

        Args:
            cell (Cell): The cell to check for associated regions.

        Returns:
            Set: A set of regions (Box, Row, Column) that the cell is part of.
        """
        regions = set(cell.top.regions())
        result: set = set()
        for r in regions:
            if r.__class__ in [Box, Column, Row] and cell in r:
                result.add(r)
        return result

    # pylint: disable=loop-invariant-statement
    def add_constraint(self, solver: PulpSolver) -> None:
        """Add constraints to the solver for the greater-than-equal difference.

        This method ensures that the difference between adjacent cells in the line is
        at least the specified minimum difference.

        Args:
            solver (PulpSolver): The solver to add the constraints to.
        """
        # Add constraints for values that are impossible on a line (currently commented out)
        for i in range(len(self.cells) - 1):
            for digit in self.board.digit_range:
                name = f"{self.name}_{i}_{digit}"
                total = lpSum(
                    [
                        solver.choices[d][self.cells[i + 1].row][self.cells[i + 1].column]
                        for d in self.board.digit_range if abs(d - digit) >= self.difference
                    ]
                )
                first = solver.choices[digit][self.cells[i].row][self.cells[i].column]
                solver.model += first <= total, name

        # Check for region intersections and ensure values are not allowed in certain cases
        for i in range(1, len(self.cells) - 1):
            c0 = self.cells[i - 1]
            c1 = self.cells[i]
            c2 = self.cells[i + 1]
            r0 = self.get_regions(c0)
            r1 = self.get_regions(c1)
            r2 = self.get_regions(c2)
            intersection = r0.intersection(r1).intersection(r2)

            if len(intersection) != 0:
                for digit in [4, 6]:
                    name = f"{self.name}_{self.cells[i].name}_{digit}_not_allowed"
                    solver.model += solver.choices[digit][self.cells[i].row][self.cells[i].column] == 0, name
