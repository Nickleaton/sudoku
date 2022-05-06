from typing import List, Any, Tuple

from src.items.board import Board
from src.items.cell import Cell
from src.items.item import Item
from src.items.pair import Pair
from src.solvers.pulp_solver import PulpSolver
from src.utils.rule import Rule


class DifferentPair(Pair):

    def __init__(self, board: Board, c1: Cell, c2: Cell, digits: List[int]):
        super().__init__(board, c1, c2)
        self.digits = digits

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.board!r}, {self.c1!r}, {self.c2!r}, {self.digits!r})"

    @classmethod
    def extract(cls, board: Board, yaml: Any) -> Tuple:
        cs, ds = yaml[cls.__name__].split("=")
        c1s, c2s = cs.split(",")
        c1 = Cell.make(board, int(c1s[0]), int(c1s[1]))
        c2 = Cell.make(board, int(c2s[0]), int(c2s[1]))
        digits = [int(d) for d in ds.split(",")]
        return c1, c2, digits

    @classmethod
    def create(cls, board: Board, yaml: Any) -> Item:
        c1, c2, digits = DifferentPair.extract(board, yaml)
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
            choice1 = solver.choices[int(digit)][self.c1.row][self.c1.column]
            choice2 = solver.choices[int(digit)][self.c2.row][self.c2.column]
            solver.model += choice1 + choice2 <= 1, name
