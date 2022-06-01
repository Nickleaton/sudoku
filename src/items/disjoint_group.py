import re
from typing import List, Dict, Optional

from src.items.board import Board
from src.items.cell import Cell
from src.items.item import Item
from src.items.standard_region import StandardRegion
from src.solvers.pulp_solver import PulpSolver
from src.utils.rule import Rule


class DisjointGroup(StandardRegion):
    offsets = [
        (0, 0),
        (0, 3),
        (0, 6),
        (3, 0),
        (3, 3),
        (3, 6),
        (6, 0),
        (6, 3),
        (6, 6)
    ]

    def __init__(self, board: Board, index: int):
        r = (index - 1) // 3 + 1
        c = (index - 1) % 3 + 1
        super().__init__(board, index)
        self.add_items([Cell.make(board, r + ro, c + co) for ro, co in DisjointGroup.offsets])
        self.strict = True
        self.unique = True

    @classmethod
    def extract(cls, board: Board, yaml: Dict) -> int:
        return int(yaml[cls.__name__])

    @classmethod
    def create(cls, board: Board, yaml: Dict) -> Item:
        index = cls.extract(board, yaml)
        return cls(board, index)

    @property
    def rules(self) -> List[Rule]:
        return [Rule('DisjointGroup', 1, 'Digits in same place each box must be unique')]

    @property
    def tags(self) -> set[str]:
        return super().tags.union({'Disjoint Group'})

    def add_constraint(self, solver: PulpSolver) -> None:
        self.add_total_constraint(solver, solver.board.digit_sum)
        self.add_unique_constraint(solver)
