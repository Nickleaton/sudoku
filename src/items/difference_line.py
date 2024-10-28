from typing import Sequence, List

from src.items.board import Board
from src.items.cell import Cell
from src.items.line import Line


class DifferenceLine(Line):
    """Represents a line in a puzzle where the cells connected by the line must
    have a specified difference.

    Attributes:
        difference (int): The required difference between connected cells.
        excluded (List[int]): A list of digits that are excluded from being placed
                              in the cells of the line.
    """

    def __init__(self, board: Board, cells: Sequence[Cell], difference: int = 0):
        """Initializes a DifferenceLine with the given board, cells, and difference.

        Args:
            board (Board): The game board containing the cells.
            cells (Sequence[Cell]): The sequence of cells connected by the line.
            difference (int, optional): The required difference between connected cells.
                                         Defaults to 0.
        """
        super().__init__(board, cells)
        self.difference = difference
        self.excluded: List[int] = []

    @property
    def tags(self) -> set[str]:
        """Tags associated with the DifferenceLine.

        Returns:
            set[str]: A set of tags specific to the DifferenceLine.
        """
        return super().tags.union({'Difference', 'Comparison'})

    # def add_constraint(self, solver: PulpSolver) -> None:
    #     # Other rules handled in the pair
    #     # exclude excluded
    #     for cell, digit in product(self.cells, self.excluded):
    #         name = f"Excluded_{cell.name}_{digit}"
    #         solver.model += solver.choices[digit][cell.row][cell.column] == 0, name
