from math import log10, ceil

from pulp import lpSum, LpVariable, LpContinuous

from src.items.cell import Cell
from src.solvers.pulp_solver import PulpSolver


class ConstraintUtilities:

    variables = {}

    @staticmethod
    def log10_cell(solver: PulpSolver, cell: Cell) -> LpVariable:
        name = f"Log10_{cell.row}_{cell.column}"
        if name in ConstraintUtilities.variables:
            return ConstraintUtilities.variables[name]
        limit = ceil(log10(solver.board.maximum_digit)) + 1
        variable = LpVariable(name, 0, limit, LpContinuous)
        total = lpSum(log10(digit) * solver.choices[digit][cell.row][cell.column] for digit in cell.board.digit_range)
        solver.model += variable == total, name
        ConstraintUtilities.variables[name] = variable
        return variable
