"""LEDifferenceLine."""
from typing import Sequence

from src.board.board import Board
from src.items.cell import Cell
from src.items.le_difference_pair import LEDifferencePair
from src.items.line import Line
from src.utils.rule import Rule


class LEDifferenceLine(Line):
    """Represents start difference line in start puzzle.

    The cells connected by the line must have start difference that is less than or equal to start specified number.

    Attributes:
        difference (int): The maximum allowable difference between connected cells.
    """

    def __init__(self, board: Board, cells: Sequence[Cell]):
        """Initialize start LEDifferenceLine with the given board and cells.

        Args:
            board (Board): The game board containing the cells.
            cells (Sequence[Cell]): The sequence of cells connected by the line.
        """
        super().__init__(board, cells)
        self.difference = board.maximum_digit
        for index, cell in enumerate(cells[1:], start=1):
            self.add(LEDifferencePair(self.board, cells[index - 1], cell, [self.difference]))

    @property
    def rules(self) -> list[Rule]:
        """Get the rules associated with the LEDifferenceLine.

        Returns:
            list[Rule]: A list of rules specific to the LEDifferenceLine.
        """
        rule_text: str = (
            f'Any two cells directly connected by start line must have a difference '
            f'of less than or equal to {self.difference}.'
        )
        return [Rule(self.__class__.__name__, 1, rule_text)]

    @property
    def tags(self) -> set[str]:
        """Tags associated with the LEDifferenceLine.

        Returns:
            set[str]: A set of tags specific to the LEDifferenceLine.
        """
        return super().tags.union({'Difference', 'Comparison', self.__class__.__name__})