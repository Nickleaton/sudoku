"""GEDifferenceLine."""

from collections.abc import Sequence
from typing import Set

from postponed.src.pulp_solver import PulpSolver
from pulp import LpAffineExpression, lpSum

from postponed.src.items.difference_line import DifferenceLine
from postponed.src.items.ge_difference_pair import GEDifferencePair
from src.board.board import Board
from src.items.box import Box
from src.items.cell import Cell
from src.items.column import Column
from src.items.item import Item
from src.items.row import Row
from src.utils.rule import Rule


class GEDifferenceLine(DifferenceLine):
    """Enforces a minimum difference between adjacent cells in a line."""

    def __init__(self, board: Board, cells: Sequence[Cell], difference: int = 5):
        """Initialize the GEDifferenceLine.

        Args:
            board (Board): The Sudoku board containing the cells.
            cells (Sequence[Cell]): The sequence of cells forming the difference line.
            difference (int): The minimum difference between consecutive cells. Defaults to 5.
        """
        super().__init__(board, cells, difference)
        for index, cell in enumerate(cells[1:], start=1):  # Start from index 1
            self.add(GEDifferencePair(self.board, cells[index - 1], cell, self.difference))

    def __repr__(self) -> str:
        """Return a string representation of the instance.

        Returns:
            str: String representation of the GEDifferenceLine instance.
        """
        return f'{self.__class__.__name__}({self.board!r}, {self.cells!r}, {self.difference!r})'

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
                f'Any two cells directly connected by a line must have a difference of at least {self.difference}.',
            ),
        ]

    @property
    def tags(self) -> set[str]:
        """Return the tags associated with this constraint.

        Returns:
            set[str]: A set of tags for the constraint.
        """
        return super().tags.union({'Difference', 'Comparison'})

    @staticmethod
    def find_regions(cell: Cell) -> Set[Box | Column | Row]:
        """Get the regions that the given cell belongs to.

        Args:
            cell (Cell): The cell to check for associated regions.

        Returns:
            Set[Box | Column | Row]: A set of regions (Box, Row, Column) that the cell is part of.
        """
        regions: Set[Item] = set(cell.top.regions())
        filtered_regions: Set[Box | Column | Row] = set()
        for region in regions:
            if isinstance(region, (Box, Column, Row)):
                if cell in region:
                    filtered_regions.add(region)
        return filtered_regions

    def add_constraint(self, solver: PulpSolver) -> None:
        """Add constraints to the solver for the greater-than-equal difference.

        Args:
            solver (PulpSolver): The solver to add the constraints to.
        """
        # Add constraints for the difference between adjacent cells
        self.add_difference_constraints(solver)

        # Add constraints for specific regions where certain digits are not allowed
        self.add_region_constraints(solver)

    def add_difference_constraints(self, solver: PulpSolver) -> None:
        """Add constraints for the greater-than-equal difference between adjacent cells.

        Args:
            solver (PulpSolver): The solver to add the constraints to.
        """
        for index in range(len(self.cells) - 1):
            for digit in self.board.digits.digit_range:
                constraint_name: str = f'{self.name}_{index}_{digit}'
                valid_cell_digits: list[int] = [
                    cell_digit for cell_digit in self.board.digits.digit_range if
                    abs(cell_digit - digit) >= self.difference
                ]
                total: LpAffineExpression = lpSum(
                    [
                        solver.variables.choices[cell_digit][self.cells[index + 1].row][self.cells[index + 1].column]
                        for cell_digit in valid_cell_digits
                    ],
                )
                cell: Cell = self.cells[index]
                first = solver.variables.choices[digit][cell.row][cell.column]
                solver.model += first <= total, constraint_name

    def add_region_constraints(self, solver: PulpSolver) -> None:
        """Add constraints for regions where certain digits are not allowed.

        Args:
            solver (PulpSolver): The solver to add the constraints to.
        """
        for index in range(1, len(self.cells) - 1):
            cell0: Cell = self.cells[index - 1]
            cell1: Cell = self.cells[index]
            cell2: Cell = self.cells[index + 1]
            region0: set[Box | Column | Row] = self.find_regions(cell0)
            region1: set[Box | Column | Row] = self.find_regions(cell1)
            region2: set[Box | Column | Row] = self.find_regions(cell2)
            intersection: set[Box | Column | Row] = region0.intersection(region1).intersection(region2)

            # If there is an intersection of regions, add constraints for restricted digits
            if intersection:
                for digit in (4, 6):
                    cell: Cell = self.cells[index]
                    name = f'{self.name}_{cell.name}_{digit}_not_allowed'
                    solver.model += solver.variables.choices[digit][cell.row][cell.column] == 0, name
