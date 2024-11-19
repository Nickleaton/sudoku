"""Constraint Utilities."""
from math import log10, ceil
from typing import dict, ClassVar

from pulp import lpSum, LpVariable, LpContinuous

from src.items.cell import Cell
from src.solvers.pulp_solver import PulpSolver


# pylint: disable=too-few-public-methods
class ConstraintUtilities:
    """Utility class for managing constraints in the PulpSolver."""

    variables: ClassVar[dict[str, LpVariable]] = {}

    @staticmethod
    def log10_cell(solver: PulpSolver, cell: Cell) -> LpVariable:
        """Create a log10 variable for a given cell in the solver.

        Args:
            solver (PulpSolver): The solver instance to which the variable belongs.
            cell (Cell): The cell for which the log10 variable is created.

        Returns:
            LpVariable: The log10 variable for the specified cell.
        """
        name = f"Log10_{cell.row}_{cell.column}"

        if name in ConstraintUtilities.variables:
            return ConstraintUtilities.variables[name]

        limit = ceil(log10(solver.board.maximum_digit)) + 1
        variable = LpVariable(name, 0, limit, LpContinuous)

        # Create the total expression for the variable
        total = lpSum(log10(digit) * solver.choices[digit][cell.row][cell.column]
                      for digit in solver.board.digit_range)

        # Add constraint to the model
        solver.model += variable == total, name

        ConstraintUtilities.variables[name] = variable
        return variable
