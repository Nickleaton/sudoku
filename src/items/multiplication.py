from math import log10
from typing import List, Set

from pulp import lpSum

from src.items.board import Board
from src.items.cell import Cell
from src.solvers.pulp_solver import PulpSolver


class Multiplication:

    @staticmethod
    def get_set(board: Board, n: int) -> Set[int]:
        used = set({})
        for a in board.digit_range:
            for b in board.digit_range:
                for c in board.digit_range:
                    for d in board.digit_range:
                        product = a * b * c * d
                        if product == n:
                            used.add(a)
                            used.add(b)
                            used.add(c)
                            used.add(d)
                        if product > n:
                            break
        return used

    @staticmethod
    def add_constraint(board: Board, solver: PulpSolver, cells: List[Cell], product: int, name: str) -> None:
        # multiplication restriction
        log_product = lpSum(
            [
                log10(digit) * solver.choices[digit][cell.row][cell.column]
                for digit in board.digit_range
                for cell in cells
            ]
        )
        solver.model += log_product == log10(product)

        # restrict possible choices
        valid_digits = Multiplication.get_set(board, product)
        for cell in cells:
            for digit in board.digit_range:
                if digit not in valid_digits:
                    solver.model += solver.choices[digit][cell.row][cell.column] == 0, f"{name}_{cell.name}_{digit}"
