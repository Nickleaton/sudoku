"""NumberedRoom."""
from typing import Dict, Tuple, List

from src.glyphs.glyph import Glyph
from src.glyphs.text_glyph import TextGlyph
from src.items.board import Board
from src.items.item import Item
from src.parsers.frame_parser import FrameParser
from src.solvers.pulp_solver import PulpSolver
from src.utils.coord import Coord
from src.utils.cyclic import Cyclic
from src.utils.rule import Rule
from src.utils.side import Side


class NumberedRoom(Item):
    """Represents a numbered room that is associated with a clue and can be part of a sequence.

    A numbered room represents a clue outside of the grid that gives the Xth digit in the row/column,
    seen from the side of the clue. The first digit in the row/column seen from the side of the clue
    is the starting point for determining which digit is referenced.
    """

    def __init__(self, board: Board, side: Side, index: int, digit: int):
        """Initialize the NumberedRoom with the given board, side, index, and digit.

        Args:
            board (Board): The board this item belongs to.
            side (Side): The side of the board (top, left, bottom, right).
            index (int): The index of the row or column.
            digit (int): The digit referenced by the clue.
        """
        super().__init__(board)
        self.side = side
        self.index = index
        self.digit = digit
        self.direction = side.direction(Cyclic.CLOCKWISE)
        self.start_cell = side.start_cell(board, self.index)
        if side == Side.TOP:
            self.reference = self.start_cell - self.direction.offset + Coord(0.5, 1.5)
        elif side == Side.RIGHT:
            self.reference = self.start_cell - self.direction.offset + Coord(1.5, 0.5)
        elif side == Side.BOTTOM:
            self.reference = self.start_cell - self.direction.offset + Coord(0.5, -0.5)
        elif side == Side.LEFT:
            self.reference = self.start_cell - self.direction.offset + Coord(-0.5, 0.5)
        else:  # pragma: no cover
            raise Exception("Unexpected Side")

    @classmethod
    def is_sequence(cls) -> bool:
        """Return True if the NumberedRoom is part of a sequence.

        Returns:
            bool: True, since the NumberedRoom is part of a sequence.
        """
        return True

    @classmethod
    def parser(cls) -> FrameParser:
        """Return the parser for the NumberedRoom.

        Returns:
            FrameParser: The parser associated with the NumberedRoom item.
        """
        return FrameParser()

    @classmethod
    def extract(cls, board: Board, yaml: Dict) -> Tuple:
        """Extract the side, index, and digit from the YAML configuration for the NumberedRoom.

        Args:
            board (Board): The board associated with the item.
            yaml (Dict): The YAML configuration containing the NumberedRoom data.

        Returns:
            Tuple: A tuple containing the side, index, and digit.
        """
        parts = yaml[cls.__name__].split("=")
        side = Side.create(parts[0][0])
        offset = int(parts[0][1])
        digit = int(parts[1])
        return side, offset, digit

    @classmethod
    def create(cls, board: Board, yaml: Dict) -> Item:
        """Create a NumberedRoom item from the given YAML configuration.

        Args:
            board (Board): The board associated with this item.
            yaml (Dict): The YAML configuration containing the NumberedRoom data.

        Returns:
            Item: The created NumberedRoom item.
        """
        side, offset, digit = cls.extract(board, yaml)
        return cls(board, side, offset, digit)

    def glyphs(self) -> List[Glyph]:
        """Generate the glyphs for the NumberedRoom.

        Returns:
            List[Glyph]: A list containing a `TextGlyph` representing the digit for the NumberedRoom.
        """
        return [
            TextGlyph('NumberedRoom', 0, self.reference, str(self.digit)),
        ]

    @property
    def rules(self) -> List[Rule]:
        """Return the rules associated with the NumberedRoom.

        Returns:
            List[Rule]: A list containing a single rule for the NumberedRoom.
        """
        return [
            Rule(
                'NumberedRoom',
                1,
                (
                    'Clues outside of the grid equal the Xth digit in their row/column '
                    'seen from the side of the clue, with X being the first digit in their '
                    'row/column seen from the side of the clue'
                )
            )
        ]

    def __repr__(self) -> str:
        """Return a string representation of the NumberedRoom.

        Returns:
            str: A string representation of the NumberedRoom item.
        """
        return f"{self.__class__.__name__}({self.board!r}, {self.side!r}, {self.index}, {self.digit})"

    def to_dict(self) -> Dict:
        """Convert the NumberedRoom to a dictionary representation.

        Returns:
            Dict: A dictionary representing the NumberedRoom item.
        """
        return {self.__class__.__name__: f"{self.side.value}{self.index}={self.digit}"}

    # pylint: disable=loop-invariant-statement
    def add_constraint(self, solver: PulpSolver) -> None:
        """Add the constraints for the NumberedRoom to the solver.

        Depending on the side of the NumberedRoom, the constraint is added by comparing
        the choices for the digit in the specified row/column.

        Args:
            solver (PulpSolver): The solver to which the constraints are added.
        """
        if self.side == Side.LEFT:
            for d in self.board.digit_range:
                first = solver.choices[d][self.start_cell.row][self.start_cell.column]
                xth = solver.choices[self.digit][self.start_cell.row][d]
                solver.model += first == xth, f"{self.name}_{d}"
        elif self.side == Side.RIGHT:
            for d in self.board.digit_range:
                first = solver.choices[d][self.start_cell.row][self.start_cell.column]
                xth = solver.choices[self.digit][self.start_cell.row][self.board.board_columns - d + 1]
                solver.model += first == xth, f"{self.name}_{d}"
        elif self.side == Side.TOP:
            for d in self.board.digit_range:
                first = solver.choices[d][self.start_cell.row][self.start_cell.column]
                xth = solver.choices[self.digit][d][self.start_cell.column]
                solver.model += first == xth, f"{self.name}_{d}"
        elif self.side == Side.BOTTOM:
            for d in self.board.digit_range:
                first = solver.choices[d][self.start_cell.row][self.start_cell.column]
                xth = solver.choices[self.digit][self.board.board_rows - d + 1][self.start_cell.column]
                solver.model += first == xth, f"{self.name}_{d}"
        else:  # pragma: no cover
            raise Exception(f"Unexpected Side {self.side.name}")

    def css(self) -> Dict:
        """Return the CSS styles associated with the NumberedRoom glyphs.

        Returns:
            Dict: A dictionary containing the CSS styles for the NumberedRoom glyphs.
        """
        return {
            '.NumberedRoomForeground': {
                'font-size': '30px',
                'stroke': 'black',
                'stroke-width': 1,
                'fill': 'black'
            },
            '.NumberedRoomBackground': {
                'font-size': '30px',
                'stroke': 'white',
                'stroke-width': 8,
                'fill': 'white',
                'font-weight': 'bolder'
            }
        }
