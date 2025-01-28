"""Constraint Utilities."""
from math import ceil  # noqa: I001
from math import log10  # noqa: I001
from typing import ClassVar

from pulp import LpContinuous  # noqa: I001
from pulp import LpVariable  # noqa: I001
from pulp import lpSum  # noqa: I001

from src.items.cell import Cell
from src.solvers.solver import Solver


class ConstraintUtilities:
    """Utility class for managing constraints in the Solver."""

    variables: ClassVar[dict[str, LpVariable]] = {}

    @staticmethod
    def total_expression(solver: Solver, cell: Cell) -> lpSum:
        """Build the total expression for the log10 integer_value of a cell.

        Args:
            solver (Solver): The solver instance.
            cell (Cell): The cell for which the expression is built.

        Returns:
            lpSum: The linear expression representing the log10 integer_value of the cell.
        """
        return lpSum(
            log10(digit) * solver.variables.choices[digit][cell.row][cell.column]
            for digit in solver.board.digits.digit_range
        )

    @staticmethod
    def log10_cell(solver: Solver, cell: Cell) -> LpVariable:
        """Create or retrieve the log10 integer_value variable for a given cell in the solver.

        Args:
            solver (Solver): The solver instance to which the variable belongs.
            cell (Cell): The cell for which the log10 integer_value variable is created.

        Returns:
            LpVariable: The log10 integer_value variable for the specified cell.
        """
        name: str = f'log10_{cell.row}_{cell.column}'
        # Return the variable if it already exists
        log_value: LpVariable = ConstraintUtilities.variables.get(name)
        if log_value is not None:
            return log_value
        # Define the limit for the variable's integer_value
        limit = ceil(log10(solver.board.digits.maximum)) + 1
        # Create the variable
        log_value: LpVariable = LpVariable(name, 0, limit, LpContinuous)
        # Build the total expression for the variable
        total_expression = ConstraintUtilities.total_expression(solver, cell)
        # Add the constraint to the solver's model
        solver.model += log_value == total_expression, name
        # Cache the variable and return it
        ConstraintUtilities.variables[name] = log_value
        return log_value
