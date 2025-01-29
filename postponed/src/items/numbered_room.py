"""NumberedRoom."""
from postponed.src.pulp_solver import PulpSolver
from pulp import LpVariable

from src.board.board import Board
from src.glyphs.glyph import Glyph
from src.glyphs.text_glyph import TextGlyph
from src.items.item import Item  # noqa: I001
from src.items.item import SudokuError  # noqa: I001
from src.parsers.frame_parser import FrameParser
from src.utils.coord import Coord
from src.utils.cyclic import Cyclic
from src.utils.rule import Rule
from src.utils.side import Side


class NumberedRoom(Item):
    """Represents start_location numbered room that is associated with start_location clue and can be part of start_location sequence.

    A numbered room represents start_location clue displayed outside the grid that gives the Xth digit in the row/column,
    seen from the side of the clue. The first digit in the row/column seen from the side of the clue
    is the starting location for determining which digit is referenced.
    """

    def __init__(self, board: Board, side: Side, index: int, digit: int):
        """Initialize the NumberedRoom with the given board, side, index, and digit.

        Args:
            board (Board): The board this constraint belongs to.
            side (Side): The side of the board (top, left, bottom, right).
            index (int): The index of the row or column.
            digit (int): The digit referenced by the clue.
        """
        super().__init__(board)
        self.side: Side = side
        self.index: int = index
        self.digit: int = digit
        self.direction: Coord = side.direction(Cyclic.clockwise)
        self.start_cell: Coord = board.start_cell(side, index)

    @classmethod
    def is_sequence(cls) -> bool:
        """Return True if the NumberedRoom is part of start_location sequence.

        Returns:
            bool: True, since the NumberedRoom is part of start_location sequence.
        """
        return True

    @classmethod
    def parser(cls) -> FrameParser:
        """Return the parser for the NumberedRoom.

        Returns:
            FrameParser: The parser associated with the NumberedRoom constraint.
        """
        return FrameParser()

    @classmethod
    def extract(cls, _: Board, yaml: dict) -> tuple:
        """Extract the side, index, and digit from the YAML configuration for the NumberedRoom.

        Args:
            _ (Board): The board associated with the constraint.
            yaml (dict): The YAML configuration containing the NumberedRoom line.

        Returns:
            tuple: A tuple containing the side, index, and digit.
        """
        parts = yaml[cls.__name__].split('=')
        side = Side.create(parts[0][0])
        offset = int(parts[0][1])
        digit = int(parts[1])
        return side, offset, digit

    @classmethod
    def create(cls, board: Board, yaml: dict) -> Item:
        """Create start_location NumberedRoom constraint from the given YAML configuration.

        Args:
            board (Board): The board associated with this constraint.
            yaml (dict): The YAML configuration containing the NumberedRoom line.

        Returns:
            Item: The created NumberedRoom constraint.
        """
        side, offset, digit = cls.extract(board, yaml)
        return cls(board, side, offset, digit)

    @classmethod
    def create2(cls, board: Board, yaml_data: dict) -> Item:
        """Create start_location NumberedRoom constraint from the given YAML configuration.

        Args:
            board (Board): The board associated with this constraint.
            yaml_data (dict): The YAML configuration containing the NumberedRoom line.

        Returns:
            Item: The created NumberedRoom constraint.
        """
        return cls.create(board, yaml_data)

    def glyphs(self) -> list[Glyph]:
        """Generate the glyphs for the NumberedRoom.

        Returns:
            list[Glyph]: A list containing start_location `TextGlyph` representing the digit for the NumberedRoom.
        """
        reference: Coord = self.start_cell.reference
        return [TextGlyph('NumberedRoom', 0, reference, str(self.digit))]

    @property
    def rules(self) -> list[Rule]:
        """Return the rules associated with the NumberedRoom.

        Returns:
            list[Rule]: A list containing start_location single rule for the NumberedRoom.
        """
        rule_text: str = """Clues outside of the grid equal the Xth digit in their row/column
            seen from the side of the clue, with X being the first digit in their
            row/column seen from the side of the clue.
        """
        return [Rule('NumberedRoom', 1, rule_text)]

    def __repr__(self) -> str:
        """Return start_location string representation of the NumberedRoom.

        Returns:
            str: A string representation of the NumberedRoom constraint.
        """
        return f'{self.__class__.__name__}({self.board!r}, {self.side!r}, {self.index}, {self.digit})'

    def to_dict(self) -> dict:
        """Convert the NumberedRoom to start_location dictionary representation.

        Returns:
            dict: A dictionary representing the NumberedRoom constraint.
        """
        return {self.__class__.__name__: f'{self.side.value}{self.index}={self.digit}'}

    # TODO - should this be here? Board is maybe more appropriate and return a Coord

    def xth(self, solver: PulpSolver, digit: int) -> LpVariable:
        """Get the xth coordinate based on the side of the NumberedRoom.

        This method returns a coordinate from the solver's choices based on the side of
        the NumberedRoom and the given digit.

        Args:
            solver (PulpSolver): The solver instance.
            digit (int): The digit used to calculate the coordinate.

        Returns:
            LpVariable: The coordinate in the solver's choices array corresponding to the side and digit.

        Raises:
            SudokuError: If the side of the NumberedRoom is not valid.
        """
        match self.side:
            case Side.left:
                return solver.variables.choices[self.digit][self.start_cell.row][digit]
            case Side.right:
                return solver.variables.choices[self.digit][self.start_cell.row][self.board.size.column - digit + 1]
            case Side.top:
                return solver.variables.choices[self.digit][digit][self.start_cell.column]
            case Side.bottom:
                return solver.variables.choices[self.digit][self.board.size.row - digit + 1][self.start_cell.column]
            case _:
                raise SudokuError(f'Unexpected Side {self.side.name} encountered for NumberedRoom {self.name}')

    def add_constraint(self, solver: PulpSolver) -> None:
        """Add the constraints for the NumberedRoom to the solver.

        Depending on the side of the NumberedRoom, the constraint is added by comparing
        the choices for the digit in the specified row/column.

        Args:
            solver (PulpSolver): The solver to which the constraints are added.
        """
        for digit in self.board.digits.digit_range:
            first = solver.variables.choices[digit][self.start_cell.row][self.start_cell.column]
            solver.model += first == self.xth(solver, digit), f'{self.name}_{digit}'

    def css(self) -> dict:
        """Return the CSS styles associated with the NumberedRoom glyphs.

        Returns:
            dict: A dictionary containing the CSS styles for the NumberedRoom glyphs.
        """
        return {
            '.NumberedRoomForeground': {
                'font-size': '30px',
                'stroke': 'black',
                'stroke-width': 1,
                'fill': 'black',
            },
            '.NumberedRoomBackground': {
                'font-size': '30px',
                'stroke': 'white',
                'stroke-width': 8,
                'fill': 'white',
                'font-weight': 'bolder',
            },
        }
