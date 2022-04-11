from typing import List

from src.items.board import Board
from src.items.cell import Cell
from src.items.pair import Pair
from src.utils.rule import Rule


class GreaterThanPair(Pair):

    def __init__(self, board: Board, c1: Cell, c2: Cell):
        super().__init__(board, c1, c2)

    @property
    def rules(self) -> List[Rule]:
        return [
            Rule(
                "GreaterThanPair",
                1,
                (
                    "Where cells are separated by chevron "
                    "the arrow points at the smaller digit"
                )
            )
        ]

    @property
    def tags(self) -> set[str]:
        return super().tags.union({'Comparison'})