from typing import List

from src.items.board import Board
from src.items.cell import Cell
from src.items.difference_line import DifferenceLine
from src.items.greater_than_equal_difference_pair import GreaterThanEqualDifferencePair
from src.utils.rule import Rule


class GreaterThanEqualDifferenceLine(DifferenceLine):

    def __init__(self, board: Board, cells: List[Cell], difference: int):
        super().__init__(board, cells, difference)
        for i in range(1, len(cells)):
            self.add(GreaterThanEqualDifferencePair(self.board, cells[i - 1], cells[i], self.difference))

    @property
    def rules(self) -> List[Rule]:
        return [
            Rule(
                self.__class__.__name__,
                1,
                f"Any two cells directly connected by a line must have a difference of at least {self.difference}"
            )
        ]

    @property
    def tags(self) -> set[str]:
        return super().tags.union({'Difference', 'Comparison'})
