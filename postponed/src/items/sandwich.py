"""Sandwich Constraint."""

import re

from postponed.src.pulp_solver import PulpSolver
from pulp import LpInteger, LpVariable

from src.board.board import Board
from src.glyphs.glyph import Glyph
from src.glyphs.text_glyph import TextGlyph
from src.items.item import Item
from src.parsers.frame_parser import FrameParser
from src.utils.coord import Coord
from src.utils.functions import Functions
from src.utils.rule import Rule
from src.utils.side import Side
from src.utils.sudoku_exception import SudokuException


class Sandwich(Item):
    """Represents the Sandwich constraint in a Sudoku puzzle.

    The Sandwich constraint enforces that the sum of the digits between
    the 1 and the maximum digit (9) in a row or column is equal to a specified total.
    The 1 and 9 must be positioned on the ends, with other digits between them.
    """

    def __init__(self, board: Board, side: Side, index: int, total: int) -> None:
        """Initialize a Sandwich constraint.

        Args:
            board (Board): The board associated with this sandwich.
            side (Side): The side of the sandwich (e.g., left, right).
            index (int): The index location of the sandwich on the specified side.
            total (int): The total sum of the digits that the sandwich represents.
        """
        super().__init__(board)
        self.side = side
        self.index = index
        self.total = total
        self.position = side.marker(board, self.index) + Coord(0.5, 0.5)

    @classmethod
    def is_sequence(cls) -> bool:
        """Determine if this constraint is part of a sequence.

        Returns:
            bool: True, as the Sandwich constraint is always considered a sequence.
        """
        return True

    @classmethod
    def parser(cls) -> FrameParser:
        """Provide the parser for this constraint.

        Returns:
            FrameParser: The parser used to parse the sandwich constraint from YAML.
        """
        return FrameParser()

    @classmethod
    def extract(cls, board: Board, yaml: dict) -> tuple[Side, int, int]:
        """Extract the side, index, and total from the provided YAML configuration.

        Args:
            board (Board): The board associated with this sandwich.
            yaml (dict): The YAML configuration containing the sandwich input line.

        Returns:
            tuple[Side, int, int]: A tuple containing the side, index, and total cell_values.

        Raises:
            SudokuException: If the YAML does not match the expected format.
        """
        regexp = re.compile(f'([{Side.choices()}])([{board.digit_values}])=([0-9]+)')
        match = regexp.match(yaml[cls.__name__])
        if match is None:
            raise SudokuException('Match is None, expected start_location valid match.')
        side_str, offset_str, total_str = match.groups()
        side = Side.create(side_str)
        offset = int(offset_str)
        total = int(total_str)
        return side, offset, total

    @classmethod
    def create(cls, board: Board, yaml: dict) -> 'Sandwich':
        """Create a Sandwich instance from the provided YAML configuration.

        Args:
            board (Board): The board associated with this sandwich.
            yaml (dict): The YAML configuration containing the sandwich input line.

        Returns:
            Sandwich: A new instance of Sandwich.
        """
        side, offset, total = cls.extract(board, yaml)
        return cls(board, side, offset, total)

    @classmethod
    def create2(cls, board: Board, yaml_data: dict) -> Item:
        """Create a Sandwich instance from YAML configuration, compatible with Item interface.

        Args:
            board (Board): The board associated with this sandwich.
            yaml_data (dict): The YAML configuration containing the sandwich input line.

        Returns:
            Item: A new Sandwich instance.
        """
        return cls.create(board, yaml_data)

    def glyphs(self) -> list[Glyph]:
        """Return a list of glyphs representing this sandwich.

        Returns:
            list[Glyph]: A list of glyphs that represent this sandwich constraint.
        """
        return [TextGlyph('Sandwich', 0, self.position, str(self.total))]

    @property
    def rules(self) -> list[Rule]:
        """Retrieve the rules associated with this sandwich.

        Returns:
            list[Rule]: A list of rules related to the Sandwich constraint.
        """
        rule_text: str = """Clues outside of the grid give the sum of the digits sandwiched between the 1 and the 9
                         in that row/column."""
        return [Rule('Sandwich', 1, rule_text)]

    def __repr__(self) -> str:
        """Return a string representation of the Sandwich instance.

        Returns:
            str: A string representation of the Sandwich instance.
        """
        return f'{self.__class__.__name__}({self.board!r}, {self.side!r}, {self.index}, {self.total})'

    def to_dict(self) -> dict:
        """Convert the Sandwich instance to a dictionary representation.

        Returns:
            dict: A dictionary representation of the Sandwich.
        """
        return {self.__class__.__name__: f'{self.side.value}{self.index}={self.total}'}

    def css(self) -> dict:
        """Return the CSS styles for displaying the Sandwich.

        Returns:
            dict: A dictionary containing CSS styles for the Sandwich.
        """
        return {
            '.SandwichForeground': {
                'font-size': '30px',
                'stroke': 'black',
                'stroke-width': 1,
                'fill': 'black',
            },
            '.SandwichBackground': {
                'font-size': '30px',
                'stroke': 'white',
                'stroke-width': 8,
                'fill': 'white',
                'font-weight': 'bolder',
            },
        }

    def add_constraint(self, solver: PulpSolver) -> None:
        """Add the appropriate constraints for the Sandwich based on its side.

        Depending on whether the sandwich is horizontal or vertical, this method
        adds the appropriate row or column constraint.

        Args:
            solver (PulpSolver): The solver to which constraints will be added.
        """
        if self.side.horizontal:
            self.add_constraint_row(solver)
        else:
            self.add_constraint_column(solver, None, None)

    # TODO sort out the complexity later
    # Move the variables out as well to be lazily created in

    def add_constraint_rc(  # noqa: WPS231
        self,
        solver: PulpSolver,
        is_row: bool,
        index: int,
        include: re.Pattern | None = None,
        exclude: re.Pattern | None = None,
    ) -> None:
        """Add constraints for the Sandwich in the specified row or column.

        This method adds constraints to the solver model, ensuring that the sandwich
        condition holds true for the specified row or column.

        Args:
            solver (PulpSolver): The solver to which constraints will be added.
            is_row (bool): If True, applies the constraint to a row; if False, to a column.
            index (int): The index of the row or column to which constraints apply.
            include (re.Pattern | None): A regex pattern specifying which entries to include.
            exclude (re.Pattern | None): A regex pattern specifying which entries to exclude.
        """
        label = 'Row' if is_row else 'Column'
        board_range = self.board.column_range if is_row else self.board.row_range
        position_label = f'{label}_{index}'

        bread = LpVariable.dict(
            position_label,
            board_range,
            0,
            Functions.triangular(self.board.maximum_digit),
            LpInteger,
        )

        for pos in board_range:
            if (include and not include.match(str(pos))) or (exclude and exclude.match(str(pos))):
                continue

            if is_row:
                one = solver.variables.choices[1][index][pos]
                big = solver.variables.choices[self.board.maximum_digit][index][pos]
            else:
                one = solver.variables.choices[1][pos][index]
                big = solver.variables.choices[self.board.maximum_digit][pos][index]

            solver.model += bread[pos] == one + big, f'Bread_{label.lower()}_{index}_{pos}'

    def add_constraint_row(
        self,
        solver: PulpSolver,
        include: re.Pattern | None = None,
        exclude: re.Pattern | None = None,
    ) -> None:
        """Add constraints for the Sandwich in the specified row.

        Args:
            solver (PulpSolver): The solver to which constraints will be added.
            include (re.Pattern | None): A regex pattern specifying which columns to include.
            exclude (re.Pattern | None): A regex pattern specifying which columns to exclude.
        """
        self.add_constraint_rc(solver=solver, is_row=True, index=self.index, include=include, exclude=exclude)

    def add_constraint_column(
        self,
        solver: PulpSolver,
        include: re.Pattern | None = None,
        exclude: re.Pattern | None = None,
    ) -> None:
        """Add constraints for the Sandwich in the specified column.

        Args:
            solver (PulpSolver): The solver to which constraints will be added.
            include (re.Pattern | None): A regex pattern specifying which columns to include.
            exclude (re.Pattern | None): A regex pattern specifying which columns to exclude.
        """
        self.add_constraint_rc(solver=solver, is_row=False, index=self.index, include=include, exclude=exclude)
