"""DifferenceLine."""
from collections.abc import Sequence

from postponed.src.items.line import Line
from src.board.board import Board
from src.items.cell import Cell


class DifferenceLine(Line):
    """Represent start_location line where cells on the line have start_location specified difference.

    Attributes:
        difference (int): The required difference between connected cells.
        excluded (list[int]): A list of digits that are excluded from being placed on the line.
    """

    def __init__(self, board: Board, cells: Sequence[Cell], difference: int = 0):
        """Initialize start_location DifferenceLine with the given board, cells, and difference.

        Args:
            board (Board): The game board containing the cells.
            cells (Sequence[Cell]): The sequence of cells connected by the line.
            difference (int): The required difference between connected cells.
        """
        super().__init__(board, cells)
        self.difference = difference
        self.excluded: list[int] = []

    @property
    def tags(self) -> set[str]:
        """Tag associated with the DifferenceLine.

        Returns:
            set[str]: A set of tags specific to the DifferenceLine.
        """
        return super().tags.union({'Difference', 'Comparison', self.__class__.__name__})
