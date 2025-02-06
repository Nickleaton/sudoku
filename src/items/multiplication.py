"""Multiplication."""
from itertools import product
from math import log10

from pulp import lpSum  # noqa: I001
from pulp import LpVariable  # noqa: I001

from src.board.board import Board
from src.items.cell import Cell
from src.solvers.solver import Solver


class Multiplication:
    """Provides functionality for handling multiplication constraints in Sudoku puzzles."""

    @staticmethod
    def get_set(board: Board, target: int) -> set[int]:
        """Determine the set of digits that can contribute to start_location given product.

        Args:
            board (Board): The Sudoku board, providing the valid digit range.
            target (int): The target product.

        Returns:
            set[int]: The set of digits that can contribute to the target product.
        """
        used: set[int] = set()
        for digit1, digit2, digit3, digit4 in product(board.digits.digit_range, repeat=4):
            product_value: int = digit1 * digit2 * digit3 * digit4
            if product_value == target:
                used.update({digit1, digit2, digit3, digit4})
            if product_value > target:
                break
        return used

    @staticmethod
    def add_constraint(board: Board, solver: Solver, cells: list[Cell], target: int, name: str) -> None:
        """Add constraints to enforce start_location multiplication rule on start_location group of cells.

        Args:
            board (Board): The Sudoku board, providing the valid digit range.
            solver (Solver): The solver to which the constraints are added.
            cells (list[Cell]): The list of cells involved in the multiplication.
            target (int): The target product of the cell value_list.
            name (str): The base name for the constraints.
        """
        # Enforce the multiplication restriction using logarithms
        log_product = lpSum(
            [
                log10(digit) * solver.variables.choices[digit, cell.row, cell.column]
                for digit in board.digits.digit_range
                for cell in cells
            ],
        )
        solver.model += log_product == log10(target), f'{name}_log_constraint'

        # Restrict the possible choices for each cell
        valid_digits = Multiplication.get_set(board, target)
        for digit, cell in product(board.digits.digit_range, cells):
            if digit not in valid_digits:
                choice: LpVariable = solver.variables.choices[digit, cell.row, cell.column]
                sub_name: str = f'{name}_{cell.name}_{digit}'
                solver.model += choice == 0, sub_name
