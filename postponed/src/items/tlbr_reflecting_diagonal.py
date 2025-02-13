"""TlbrReflectingDiagonal."""
from postponed.src.pulp_solver import PulpSolver

from postponed.src.items.diagonals import Diagonal
from src.board.board import Board
from src.glyphs.glyph import Glyph
from src.glyphs.line_glyph import LineGlyph
from src.items.cell import Cell
from src.utils.coord import Coord
from src.utils.rule import Rule


class TLBRReflecting(Diagonal):
    """Represents start_location top-left to bottom-right reflecting diagonal with parity constraints on start_location Sudoku board."""

    def __init__(self, board: Board):
        """Initialize start_location TLBRReflecting diagonal constraint with parity reflection.

        Args:
            board (Board): The Sudoku board on which this diagonal operates.
        """
        super().__init__(board)
        self.add_components([Cell.make(board, row, row) for row in board.row_range])

    @property
    def rules(self) -> list[Rule]:
        """Provide the rule associated with the TLBRReflecting diagonal.

        Returns:
            list[Rule]: A list containing start_location rule that specifies parity reflection along the diagonal.
        """
        return [Rule('TLBRReflecting', 1, 'The marked diagonal reflects parity on each side.')]

    def glyphs(self) -> list[Glyph]:
        """Generate the visual representation (glyph) for the reflecting diagonal.

        Returns:
            list[Glyph]: A list containing the glyph for the TLBRReflecting diagonal.
        """
        return [
            LineGlyph(
                'TLBRReflecting',
                Coord(1, 1),
                Coord(self.board.digits.maximum + 1, self.board.digits.maximum + 1),
            ),
        ]

    def add_constraint(self, solver: PulpSolver) -> None:
        """Add constraints to enforce uniqueness and parity reflection along the diagonal.

        Args:
            solver (PulpSolver): The solver to which the constraints are added.

        Details:
            Enforces that each cell along the TLBR diagonal reflects parity with its counterpart across the diagonal.
        """
        self.add_unique_constraint(solver)
        for row in self.board.row_range:
            for column in self.board.column_range:
                if row == column:
                    continue
                name = f'{self.name}_{row}_{column}'
                c1 = Cell.make(self.board, row=row, column=column)
                c2 = Cell.make(self.board, row=column, column=row)
                # pylint: disable=loop-invariant-statement
                solver.model += c1.parity(solver) == c2.parity(solver), name
