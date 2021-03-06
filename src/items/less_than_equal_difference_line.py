from typing import List, Sequence

from src.items.board import Board
from src.items.cell import Cell
from src.items.less_than_equal_difference_pair import LessThanEqualDifferencePair
from src.items.line import Line
from src.utils.rule import Rule


class LessThanEqualDifferenceLine(Line):

    def __init__(self, board: Board, cells: Sequence[Cell]):
        super().__init__(board, cells)
        self.difference = board.maximum_digit
        for i in range(1, len(cells)):
            self.add(LessThanEqualDifferencePair(self.board, cells[i - 1], cells[i], self.difference))

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
