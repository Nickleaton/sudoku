from typing import List, Dict

from src.items.board import Board
from src.items.cell import Cell
from src.items.pair import Pair
from src.solvers.pulp_solver import PulpSolver
from src.utils.rule import Rule


class DifferentPair(Pair):

    def __init__(self, board: Board, c1: Cell, c2: Cell, digits: List[int]):
        super().__init__(board, c1, c2)
        self.digits = digits

    @classmethod
    def create(cls, name: str, board: Board, yaml: Dict) -> 'DifferentPair':
        c1 = Cell(board, yaml['Cells'][0][0], yaml['Cells'][0][1])
        c2 = Cell(board, yaml['Cells'][1][0], yaml['Cells'][1][1])
        digits = yaml['Digits']
        return cls(board, c1, c2, digits)

    @property
    def rules(self) -> List[Rule]:
        return []

    @property
    def tags(self) -> set[str]:
        return super().tags.union({'Different'})

    def add_constraint(self, solver: PulpSolver) -> None:
        for digit in self.digits:
            name = f"{self.__class__.__name__}_{digit}_{self.c1.row}_{self.c1.column}_{self.c2.row}_{self.c2.column}"
            # TODO int should not be needed
            solver.model += solver.choices[int(digit)][self.c1.row][self.c1.column] + \
                            solver.choices[int(digit)][self.c2.row][self.c2.column] <= 1, name
