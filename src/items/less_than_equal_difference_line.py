"""LessThanEqualDifferenceLine."""
from typing import Sequence

from src.items.board import Board
from src.items.cell import Cell
from src.items.less_than_equal_difference_pair import LessThanEqualDifferencePair
from src.items.line import Line
from src.utils.rule import Rule


class LessThanEqualDifferenceLine(Line):
    """Represents a difference line in a puzzle.

    The cells connected by the line must have a difference that is less than or equal to a specified value.

    Attributes:
        difference (int): The maximum allowable difference between connected cells.
    """

    def __init__(self, board: Board, cells: Sequence[Cell]):
        """Initialize a LessThanEqualDifferenceLine with the given board and cells.

        Args:
            board (Board): The game board containing the cells.
            cells (Sequence[Cell]): The sequence of cells connected by the line.
        """
        super().__init__(board, cells)
        self.difference = board.maximum_digit
        for i in range(1, len(cells)):
            self.add(LessThanEqualDifferencePair(self.board, cells[i - 1], cells[i], [self.difference]))

    @property
    def rules(self) -> list[Rule]:
        """Get the rules associated with the LessThanEqualDifferenceLine.

        Returns:
            list[Rule]: A list of rules specific to the LessThanEqualDifferenceLine.
        """
        return [
            Rule(
                self.__class__.__name__,
                1,
                (
                    f"Any two cells directly connected by a line must have a difference "
                    f"of less than or equal to {self.difference}."
                )
            )
        ]

    @property
    def tags(self) -> set[str]:
        """Tags associated with the LessThanEqualDifferenceLine.

        Returns:
            set[str]: A set of tags specific to the LessThanEqualDifferenceLine.
        """
        return super().tags.union({'Difference', 'Comparison'})
