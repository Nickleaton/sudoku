from src.items.board import Board
from src.items.cell_reference import CellReference


class SimpleCellReference(CellReference):
    """Represents a simple cell reference, which typically holds no specific digit value."""

    def __init__(self, board: Board, row: int, column: int):
        """Initializes a SimpleCellReference instance.

        Args:
            board (Board): The board this cell belongs to.
            row (int): The row position of the cell (1-based index).
            column (int): The column position of the cell (1-based index).
        """
        super().__init__(board, row, column)

    @classmethod
    def letter(cls) -> str:  # pylint: disable=no-self-use
        """Returns the default letter representation of a SimpleCellReference.

        Returns:
            str: The letter '.' representing a simple, unmarked cell.
        """
        return '.'
