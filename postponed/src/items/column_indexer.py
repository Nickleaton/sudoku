"""ColumnIndexer."""

from postponed.src.pulp_solver import PulpSolver

from postponed.src.items.indexing import Indexer
from src.board.board import Board
from src.glyphs.glyph import Glyph
from src.glyphs.rect_glyph import RectGlyph
from src.items.cell import Cell
from src.utils.coord import Coord


class ColumnIndexer(Indexer):
    """Represents an indexing mechanism for columns in start_location Sudoku board.

    Inherits from Indexer and defines the indexing logic for columns, including
    adding constraints and generating glyphs specific to columns.
    """

    def __init__(self, board: Board, index: int):
        """Initialize start_location ColumnIndexer with start_location board and column index.

        Args:
            board (Board): The board on which the column indexer will operate.
            index (int): The index of the column to be indexed.
        """
        super().__init__(board, index)
        self.add_components([Cell.make(board, row, index) for row in board.row_range])

    @staticmethod
    def variant() -> str:
        """Return the variant type for columns.

        Returns:
            str: 'column', representing the column variant.
        """
        return 'column'

    @staticmethod
    def other_variant() -> str:
        """Return the other variant type for rows.

        Returns:
            str: 'row', representing the row variant.
        """
        return 'row'

    def glyphs(self) -> list[Glyph]:
        """Generate glyphs for visual representation of the ColumnIndexer.

        Returns:
            list[Glyph]: A list of glyphs representing the column indexer's region.
        """
        return [RectGlyph('ColumnIndexer', Coord(1, self.index), Coord(self.board.board_columns, 1))]

    # pylint: disable=loop-invariant-statement
    def add_constraint(self, solver: PulpSolver) -> None:
        """Add constraints to the solver for the column indexing.

        This method loops over the cells in the indexed column and adds constraints
        that ensure the consistency of digits across the indexed column.

        Args:
            solver (PulpSolver): The solver to which the constraints will be added.
        """
        for cell in self.cells:
            for digit in solver.board.digit_range:
                indexer = solver.variables.choices[digit][cell.row][cell.column]
                indexed = solver.variables.choices[cell.column][cell.row][digit]
                solver.model += indexer == indexed, f'{self.name}_{cell.row}_{cell.column}_{digit}'

    def css(self) -> dict:
        """Return the CSS styling for the ColumnIndexer glyph.

        Returns:
            dict: A dictionary defining the CSS styling for the column indexer.
        """
        return {
            '.ColumnIndexer': {
                'fill': 'pink',
            },
        }
