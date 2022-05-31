import re
from itertools import product
from typing import List, Dict, Optional

from src.items.board import Board
from src.items.composed_item import ComposedItem
from src.items.item import Item
from src.solvers.pulp_solver import PulpSolver
from src.utils.direction import Direction
from src.utils.rule import Rule


class OrthogonallyAdjacent(ComposedItem):

    def __init__(self, board: Board):
        super().__init__(board, [])

    @property
    def tags(self) -> set[str]:
        return super().tags.union({'OrthogonallyAdjacent'})

    @classmethod
    def create(cls, board: Board, yaml: Dict) -> Item:
        return OrthogonallyAdjacent(board)

    @property
    def rules(self) -> List[Rule]:
        return [
            Rule("OrthogonallyAdjacent", 1, "Consecutive digits must never be orthogonally adjacent")
        ]

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.board!r})"

    def to_dict(self) -> Dict:
        return {self.__class__.__name__: None}

    def add_constraint(self, solver: PulpSolver, include: Optional[re.Pattern], exclude: Optional[re.Pattern]) -> None:
        for row, column in product(self.board.row_range, self.board.row_range):
            for offset in Direction.orthogonals():
                if not self.board.is_valid(int(row + offset.row), int(column + offset.column)):
                    continue
                for digit in self.board.digit_range:
                    if digit + 1 > self.board.maximum_digit:
                        continue
                    if digit - 1 < 1:
                        continue
                    lhs = solver.choices[digit][row][column]
                    prefix = f"{self.name}_{row}_{column}_{row + offset.row}_{row + offset.column}_{digit}"

                    rhs_1 = solver.choices[digit + 1][row + offset.row][column + offset.column]
                    solver.model += lhs + rhs_1 <= 1, f"{prefix}_{digit + 1}"

                    rhs_2 = solver.choices[digit - 1][row + offset.row][column + offset.column]
                    solver.model += lhs + rhs_2 <= 1, f"{prefix}_{digit - 1}"
