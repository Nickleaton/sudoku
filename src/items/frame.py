"""Frame."""
import re
from typing import List, Any, Dict

from src.glyphs.glyph import Glyph
from src.glyphs.text_glyph import TextGlyph
from src.items.board import Board
from src.items.first_n import FirstN
from src.items.item import Item
from src.parsers.frame_parser import FrameParser
from src.solvers.pulp_solver import PulpSolver
from src.utils.rule import Rule
from src.utils.side import Side


class Frame(FirstN):
    """Frame Constraints."""

    def __init__(self, board: Board, side: Side, index: int, total: int):
        """Initialize a Frame instance with the given board, side, index, and total."""
        super().__init__(board, side, index)
        self.total = total

    @classmethod
    def is_sequence(cls) -> bool:
        """Return True if this item is a sequence."""
        return True

    @classmethod
    def parser(cls) -> FrameParser:
        """Return the parser for this item."""
        return FrameParser()

    def __repr__(self) -> str:
        """Return the string representation of the frame."""
        return (
            f"{self.__class__.__name__}"
            f"("
            f"{self.board!r}, "
            f"{self.side!r}, "
            f"{self.total}"
            f")"
        )

    @property
    def rules(self) -> List[Rule]:
        """Return the rules associated with the frame."""
        return [
            Rule(
                'Frame',
                1,
                "Numbers outside the frame equal the sum of the first three numbers in the "
                "corresponding row or column in the given direction"
            )
        ]

    def glyphs(self) -> List[Glyph]:
        """Return the list of glyphs associated with the frame."""
        return [
            TextGlyph(
                'FrameText',
                0,
                self.side.marker(self.board, self.index).center,
                str(self.total)
            )
        ]

    @property
    def tags(self) -> set[str]:
        """Return the tags associated with the frame."""
        return super().tags.union({'Comparison', 'Frame'})

    @classmethod
    def extract(cls, board: Board, yaml: Dict) -> Any:
        """Extract and return the side, index, and total from the given YAML configuration."""
        regexp = re.compile(f"([{Side.values()}])([{board.digit_values}])=([1234567890]+)")
        match = regexp.match(yaml[cls.__name__])
        assert match is not None
        side_str, index_str, total_str = match.groups()
        side = Side.create(side_str)
        index = int(index_str)
        total = int(total_str)
        return side, index, total

    @classmethod
    def create(cls, board: Board, yaml: Dict) -> Item:
        """Create and return a Frame instance based on the provided YAML configuration."""
        side, index, total = Frame.extract(board, yaml)
        return cls(board, side, index, total)

    def add_constraint(self, solver: PulpSolver) -> None:
        """Add the constraint for the frame to the solver."""
        self.add_total_constraint(solver, self.total)

    def to_dict(self) -> Dict:
        """Return a dictionary representation of the frame."""
        return {self.__class__.__name__: f"{self.side.value}{self.index}={self.total}"}

    def css(self) -> Dict:
        """Return the CSS styles for visualizing the frame."""
        return {
            ".FrameTextForeground": {
                "fill": "black",
                "font-size": "30px",
                "stroke": "black",
                "stroke-width": 1
            },
            ".FrameTextBackground": {
                "fill": "white",
                "font-size": "30px",
                "font-weight": "bolder",
                "stroke": "white",
                "stroke-width": 8
            }
        }
