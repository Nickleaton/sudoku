from itertools import product
from math import log10
from typing import List, Set, Tuple

from pulp import lpSum

from src.items.board import Board
from src.items.cell import Cell
from src.solvers.pulp_solver import PulpSolver


class Multiplication:

    @staticmethod
    def get_set(board: Board, n: int, c: int) -> Set[int]:

        def multiply(x: Tuple[int]) -> int:
            result = 1
            for a in x:
                result *= a
            return result

        used = set({})
        for x in product(board.digit_range,
                         board.digit_range,
                         board.digit_range,
                         board.digit_range):
            if multiply(x) == n:
                used.add(x[0])
                used.add(x[1])
                used.add(x[2])
                used.add(x[3])
        return used

    @staticmethod
    def add_constraint(board: Board, solver: PulpSolver, cells: List[Cell], product: int, name: str) -> None:
        # multiplication restriction
        log_product = lpSum(
            [
                log10(d) * solver.choices[d][c.row][c.column]
                for d in board.digit_range
                for c in cells
            ]
        )
        solver.model += log_product == log10(product)

        # restrict possible choices
        valid_digits = Multiplication.get_set(board, product, len(cells))
        for cell in cells:
            for digit in board.digit_range:
                if digit not in valid_digits:
                    solver.model += solver.choices[digit][cell.row][cell.column] == 0, f"{name}_{cell.name}_{digit}"
