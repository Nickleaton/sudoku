import re
from itertools import product
from typing import List, Dict

from pulp import lpSum

from src.items.board import Board
from src.items.cell import Cell
from src.items.item import Item
from src.solvers.pulp_solver import PulpSolver
from src.utils.coord import Coord
from src.utils.rule import Rule


class Quadro(Item):

    @property
    def rules(self) -> List[Rule]:
        return [
            Rule('Quadro', 3, 'There must be at least one even and at least one odd digit in every 2×2 adjacent cells')
        ]

    @classmethod
    def create(cls, board: Board, yaml: Dict) -> Item:
        return cls(board)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.board!r})"

    def add_constraint(self, solver: PulpSolver, include: re.Pattern, exclude: re.Pattern) -> None:
        offsets = [Coord(0, 0), Coord(0, 1), Coord(1, 0), Coord(1, 1)]
        for row, column in product(self.board.row_range, self.board.column_range):
            if row == self.board.board_rows:
                continue
            if column == self.board.board_columns:
                continue
            evens = lpSum(
                [
                    Cell.make(self.board, int(row + offset.row), int(column + offset.column)).parity(solver)
                    for offset in offsets
                ]
            )
            # There are four cells. At least one must be even
            solver.model += evens >= 1, f"{self.name}_{row}_{column}_even"
            # There are four cells. At least one must be odd.
            # If there are 4 evens, its wrong. So no more than 3 evens means at least one odd
            solver.model += evens <= 3, f"{self.name}_{row}_{column}_odd"
