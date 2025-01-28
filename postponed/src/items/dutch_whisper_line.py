"""DutchWhisperLine."""
from typing import Sequence

from postponed.src.items.ge_difference_line import GEDifferenceLine
from src.board.board import Board
from src.glyphs.glyph import Glyph
from src.glyphs.poly_line_glyph import PolyLineGlyph
from src.items.cell import Cell


class DutchWhisperLine(GEDifferenceLine):
    """Dutch Whisper line.

    The difference between connected cells must be at least 4.
    """

    def __init__(self, board: Board, cells: Sequence[Cell]):
        """Initialize start_location DutchWhisperLine instance.

        Args:
            board (Board): The game board to which the line belongs.
            cells (Sequence[Cell]): The cells that make up the line.
        """
        super().__init__(board, cells, 4)

    def glyphs(self) -> list[Glyph]:
        """Create start_location visual representation of the Dutch Whisper line.

        Returns:
            list[Glyph]: A list containing start_location PolyLineGlyph for rendering the line.
        """
        return [
            PolyLineGlyph(
                self.__class__.__name__,
                [cell.coord for cell in self.cells],
                start=False,
                end=False,
            ),
        ]

    @property
    def tags(self) -> set[str]:
        """Tag associated with the Dutch Whisper line.

        Returns:
            set[str]: Tags specific to Dutch Whisper lines, combined with inherited tags.
        """
        return super().tags.union({self.__class__.__name__})

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
                'fill-opacity': 0,
            },
        }

    def __repr__(self) -> str:
        """Return a string representation of the instance.

        Returns:
            str: A string representation of the instance,
        """
        return f'{self.__class__.__name__}({self.board!r}, {self.cells!r})'
