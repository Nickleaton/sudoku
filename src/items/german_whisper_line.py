"""GermanWhisperLine."""
from typing import List, Sequence, Dict
from src.glyphs.glyph import Glyph
from src.glyphs.poly_line_glyph import PolyLineGlyph
from src.items.board import Board
from src.items.cell import Cell
from src.items.greater_than_equal_difference_line import GreaterThanEqualDifferenceLine
from src.utils.rule import Rule


class GermanWhisperLine(GreaterThanEqualDifferenceLine):
    """Represents a German Whisper line.

    The difference between connected cells must be at least 5.

    Attributes:
        excluded (List[int]): Digits that are excluded from the line (e.g., 5).
    """

    def __init__(self, board: Board, cells: Sequence[Cell]):
        """Initialize a GermanWhisperLine instance.

        Args:
            board (Board): The game board to which the line belongs.
            cells (Sequence[Cell]): The cells that make up the line.
        """
        super().__init__(board, cells, 5)
        self.excluded = [5]

    def glyphs(self) -> List[Glyph]:
        """Create a visual representation of the German Whisper line.

        Returns:
            List[Glyph]: A list containing a PolyLineGlyph for rendering the line.
        """
        return [PolyLineGlyph('GermanWhisperLine', [cell.coord for cell in self.cells], False, False)]

    @property
    def rules(self) -> List[Rule]:
        """Define the rules for the German Whisper line.

        Returns:
            List[Rule]: A list of Rule objects specifying the digit difference requirements.
        """
        return [
            Rule(
                self.__class__.__name__,
                1,
                "Any two cells directly connected by a green line must have a difference of at least 5."
            )
        ]

    @property
    def tags(self) -> set[str]:
        """Tags associated with the German Whisper line.

        Returns:
            set[str]: Tags specific to German Whisper lines, combined with inherited tags.
        """
        return super().tags.union({'German Whisper'})

    def css(self) -> Dict:
        """CSS styling properties for rendering the German Whisper line.

        Returns:
            Dict: A dictionary defining CSS properties for the German Whisper line.
        """
        return {
            '.GermanWhisperLine': {
                'stroke': 'green',
                'stroke-width': 20,
                'stroke-linecap': 'round',
                'stroke-linejoin': 'round',
                'fill-opacity': 0
            }
        }

