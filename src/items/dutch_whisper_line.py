"""DutchWhisperLine."""
from typing import Sequence

from src.board.board import Board
from src.glyphs.glyph import Glyph
from src.glyphs.poly_line_glyph import PolyLineGlyph
from src.items.cell import Cell
from src.items.greater_than_equal_difference_line import GreaterThanEqualDifferenceLine


class DutchWhisperLine(GreaterThanEqualDifferenceLine):
    """Dutch Whisper line.

    The difference between connected cells must be at least 4.
    """

    def __init__(self, board: Board, cells: Sequence[Cell]):
        """Initialize a DutchWhisperLine instance.

        Args:
            board (Board): The game board to which the line belongs.
            cells (Sequence[Cell]): The cells that make up the line.
        """
        super().__init__(board, cells, 4)

    def glyphs(self) -> list[Glyph]:
        """Create a visual representation of the Dutch Whisper line.

        Returns:
            list[Glyph]: A list containing a PolyLineGlyph for rendering the line.
        """
        return [PolyLineGlyph('DutchWhisperLine', [cell.coord for cell in self.cells], False, False)]

    @property
    def tags(self) -> set[str]:
        """Tag associated with the Dutch Whisper line.

        Returns:
            set[str]: Tags specific to Dutch Whisper lines, combined with inherited tags.
        """
        return super().tags.union({'Dutch Whisper'})

    def css(self) -> dict:
        """CSS styling properties for rendering the Dutch Whisper line.

        Returns:
            dict: A dictionary defining CSS properties for the Dutch Whisper line.
        """
        return {
            '.DutchWhisperLine': {
                'stroke': 'green',
                'stroke-width': 20,
                'stroke-linecap': 'round',
                'stroke-linejoin': 'round',
                'fill-opacity': 0
            }
        }

    def __repr__(self) -> str:
        """Return a string representation of the instance."""
        return f"{self.__class__.__name__}({self.board!r}, {self.cells!r})"
