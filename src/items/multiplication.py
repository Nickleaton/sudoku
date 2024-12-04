"""Multiplication."""
from math import log10

from pulp import lpSum

from src.items.board import Board
from src.items.cell import Cell
from src.solvers.pulp_solver import PulpSolver


class Multiplication:
    """Provides functionality for handling multiplication constraints in Sudoku puzzles."""

    @staticmethod
    # pylint: disable=loop-invariant-statement
    def get_set(board: Board, n: int) -> set[int]:
        """Determine the set of digits that can contribute to a given product.

        Args:
            board (Board): The Sudoku board, providing the valid digit range.
            n (int): The target product.

        Returns:
            set[int]: The set of digits that can contribute to the target product.
        """
        used: set[int] = set()
        for a in board.digit_range:
            for b in board.digit_range:
                for c in board.digit_range:
                    for d in board.digit_range:
                        product: int = a * b * c * d
                        if product == n:
                            used.update({a, b, c, d})
                        if product > n:
                            break
        return used

    @staticmethod
    # pylint: disable=loop-invariant-statement
    def add_constraint(board: Board, solver: PulpSolver, cells: list[Cell], product: int, name: str) -> None:
        """Add constraints to enforce a multiplication rule on a group of cells.

        Args:
            board (Board): The Sudoku board, providing the valid digit range.
            solver (PulpSolver): The solver to which the constraints are added.
            cells (list[Cell]): The list of cells involved in the multiplication.
            product (int): The target product of the cell values.
            name (str): The base name for the constraints.
        """
        # Enforce the multiplication restriction using logarithms
        log_product = lpSum(
            [
                log10(digit) * solver.choices[digit][cell.row][cell.column]
                for digit in board.digit_range
                for cell in cells
            ]
        )
        solver.model += log_product == log10(product), f"{name}_log_constraint"

        # Restrict the possible choices for each cell
        valid_digits = Multiplication.get_set(board, product)
        for cell in cells:
            for digit in board.digit_range:
                if digit not in valid_digits:
                    solver.model += solver.choices[digit][cell.row][cell.column] == 0, f"{name}_{cell.name}_{digit}"
