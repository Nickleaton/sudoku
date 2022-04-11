from typing import Optional, List

from src.items.board import Board
from src.items.cell import Cell
from src.items.line import Line
from src.solvers.solver import Solver
from src.utils.rule import Rule


class LockOut(Line):

    def __init__(self, board: Board, cells: Optional[List[Cell]]):
        super().__init__(board, cells)

    @property
    def rules(self) -> List[Rule]:
        return [
            Rule(
                'LockOut',
                1,
                (
                    "Diamond endpoints must be at least 4 apart. "
                    "Digits on the line must fall strictly outside the end points"
                )
            )
        ]

    @property
    def tags(self) -> set[str]:
        return super().tags.union({'LockOut', 'Comparison'})

