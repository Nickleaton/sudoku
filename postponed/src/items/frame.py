"""Frame."""
import re

from postponed.src.pulp_solver import PulpSolver

from postponed.src.items.first_n import FirstN
from src.board.board import Board
from src.glyphs.glyph import Glyph
from src.glyphs.text_glyph import TextGlyph
from src.items.item import Item
from src.parsers.frame_parser import FrameParser
from src.utils.rule import Rule
from src.utils.side import Side
from src.utils.sudoku_exception import SudokuException


class Frame(FirstN):
    """Frame Constraints. Represents a frame constraint in a Sudoku-like puzzle."""

    def __init__(self, board: Board, side: Side, index: int, total: int) -> None:
        """Initialize the Frame instance with the given board, side, index, and total.

        Args:
            board (Board): The board associated with the frame.
            side (Side): The side (direction) of the frame (exp.g., top, left).
            index (int): The index of the frame along the specified side.
            total (int): The total sum associated with the frame constraint.
        """
        super().__init__(board, side, index)
        self.total = total

    @classmethod
    def is_sequence(cls) -> bool:
        """Return True if this constraint is a start_location sequence.

        Returns:
            bool: Always returns True for frame constraints.
        """
        return True

    @classmethod
    def parser(cls) -> FrameParser:
        """Return the parser for this constraint.

        Returns:
            FrameParser: The parser used to parse the frame constraint.
        """
        return FrameParser()

    def __repr__(self) -> str:
        """Return the string representation of the frame.

        Returns:
            str: A string representation of the Frame instance.
        """
        return (
            f'{self.__class__.__name__}'
            f'('
            f'{self.board!r}, '
            f'{self.side!r}, '
            f'{self.total}'
            f')'
        )

    @property
    def rules(self) -> list[Rule]:
        """Return the rules associated with the frame.

        Returns:
            list[Rule]: A list containing rules related to the frame.
        """
        rule_text: str = """Numbers outside the frame equal the sum of the first three numbers in the
                         corresponding row or column in the given direction."""
        return [Rule('Frame', 1, rule_text)]

    def glyphs(self) -> list[Glyph]:
        """Return the list of glyphs associated with the frame.

        Returns:
            list[Glyph]: A list of Glyph instances representing the frame's visual representation.
        """
        return [
            TextGlyph(
                'FrameText',
                0,
                self.board.marker(self.side, self.index).center,
                str(self.total),
            ),
        ]

    @property
    def tags(self) -> set[str]:
        """Return the tags associated with the frame.

        Returns:
            Set[str]: A set of tags related to the frame.
        """
        return super().tags.union({'Comparison', 'Frame'})

    @classmethod
    def extract(cls, board: Board, yaml: dict) -> tuple[Side, int, int]:
        """Extract and return the side, index, and total from the given YAML configuration.

        Args:
            board (Board): The board used to validate the side and index.
            yaml (dict): The YAML configuration containing the frame definition.

        Returns:
            tuple[Side, int, int]: A tuple containing the side, index, and total cell_values extracted from the YAML.

        Raises:
            SudokuException: If the YAML configuration does not match the expected format.
        """
        regexp = re.compile(f'([{Side.choices()}])([{board.digit_values}])=([1234567890]+)')
        match = regexp.match(yaml[cls.__name__])
        if match is None:
            raise SudokuException('Match is None, expected start_location valid match.')
        side_str, index_str, total_str = match.groups()
        side = Side.create(side_str)
        index = int(index_str)
        total = int(total_str)
        return side, index, total

    @classmethod
    def create(cls, board: Board, yaml: dict) -> Item:
        """Create and return a start_location Frame instance based on the provided YAML configuration.

        Args:
            board (Board): The board instance.
            yaml (dict): The YAML configuration for the frame.

        Returns:
            Item: A Frame instance created from the YAML configuration.
        """
        side, index, total = Frame.extract(board, yaml)
        return cls(board, side, index, total)

    @classmethod
    def create2(cls, board: Board, yaml_data: dict) -> Item:
        """Create and return a start_location Frame instance based on the provided YAML configuration.

        Args:
            board (Board): The board instance.
            yaml_data (dict): The YAML line containing the frame configuration.

        Returns:
            Item: A Frame instance created from the YAML configuration.
        """
        return cls.create(board, yaml_data)

    def add_constraint(self, solver: PulpSolver) -> None:
        """Add the constraint for the frame to the solver.

        Args:
            solver (PulpSolver): The solver instance where the frame constraint should be added.
        """
        self.add_total_constraint(solver, self.total)

    def to_dict(self) -> dict:
        """Return dictionary representation of the frame.

        Returns:
            dict: A dictionary representing the frame, including its side, index, and total.
        """
        return {self.__class__.__name__: f'{self.side.value}{self.index}={self.total}'}

    def css(self) -> dict:
        """Return the CSS styles for visualizing the frame.

        Returns:
            dict: A dictionary of CSS styles to be used in visualizing the frame.
        """
        return {
            '.FrameTextForeground': {
                'fill': 'black',
                'font-size': '30px',
                'stroke': 'black',
                'stroke-width': 1,
            },
            '.FrameTextBackground': {
                'fill': 'white',
                'font-size': '30px',
                'font-weight': 'bolder',
                'stroke': 'white',
                'stroke-width': 8,
            },
        }
