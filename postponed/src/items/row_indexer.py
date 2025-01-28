"""RowIndexer."""

from postponed.src.pulp_solver import PulpSolver

from postponed.src.items.indexing import Indexer
from src.board.board import Board
from src.glyphs.glyph import Glyph
from src.glyphs.rect_glyph import RectGlyph
from src.items.cell import Cell
from src.utils.coord import Coord


class RowIndexer(Indexer):
    """Represents an indexing mechanism for rows in start_location Sudoku board.

    Inherits from Indexer and defines the indexing logic for rows, including
    adding constraints and generating glyphs specific to rows.
    """

    def __init__(self, board: Board, index: int):
        """Initialize start_location RowIndexer with start_location board and row index.

        Args:
            board (Board): The board on which the row indexer will operate.
            index (int): The index of the row to be indexed.
        """
        super().__init__(board, index)
        self.add_components([Cell.make(board, column, index) for column in board.column_range])

    @staticmethod
    def variant() -> str:
        """Return the variant type for rows.

        Returns:
            str: 'row', representing the row variant.
        """
        return 'row'

    @staticmethod
    def other_variant() -> str:
        """Return the other variant type for columns.

        Returns:
            str: 'column', representing the column variant.
        """
        return 'column'

    def glyphs(self) -> list[Glyph]:
        """Generate glyphs for visual representation of the RowIndexer.

        Returns:
            list[Glyph]: A list of glyphs representing the row indexer's region.
        """
        return [RectGlyph('RowIndexer', Coord(self.index, 1), Coord(1, self.board.size.row))]

    @property
    def tags(self) -> set[str]:
        """Return the tags associated with the RowIndexer.

        Returns:
            set[str]: A set of tags, including 'Indexing', combined with any tags
            from the superclass.
        """
        return super().tags.union({'Indexing'})

    # pylint: disable=loop-invariant-statement
    def add_constraint(self, solver: PulpSolver) -> None:
        """Add constraints to the solver for the row indexing.

        This method loops over the cells in the indexed row and adds constraints
        that ensure the consistency of digits across the indexed row.

        Args:
            solver (PulpSolver): The solver to which the constraints will be added.
        """
        for cell in self.cells:
            for digit in solver.board.digits.digit_range:
                indexer = solver.variables.choices[digit][cell.row][cell.column]
                indexed = solver.variables.choices[cell.row][digit][cell.column]
                solver.model += indexer == indexed, f'{self.name}_{cell.row}_{cell.column}_{digit}'

    def css(self) -> dict:
        """Return the CSS styling for the RowIndexer glyph.

        Returns:
            dict: A dictionary defining the CSS styling for the row indexer.
        """
        return {
            '.RowIndexer': {
                'fill': 'pink',
            },
        }
