from typing import List

from src.items.board import Board
from src.items.cell import Cell
from src.items.pair import Pair
from src.solvers.pulp_solver import PulpSolver
from src.utils.rule import Rule


class DifferencePair(Pair):

    def __init__(self, board: Board, c1: Cell, c2: Cell):
        super().__init__(board, c1, c2)

    @property
    def name(self) -> str:
        return f"{self.__class__.__name__}_{self.c1.name}_{self.c2.name}"

    @property
    def difference(self) -> int:
        return 0

    @property
    def rules(self) -> List[Rule]:
        return []

    @property
    def tags(self) -> set[str]:
        return super().tags.union({'Difference'})

    def add_constraint(self, solver: PulpSolver) -> None:
        total = solver.values[self.c1.row][self.c1.column] + solver.values[self.c2.row][self.c2.column]
        solver.model += total == self.difference, self.name
