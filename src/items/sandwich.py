"""Sandwich."""
import re
from typing import Dict, Tuple, List, Optional

from pulp import LpVariable, LpInteger

from src.glyphs.glyph import Glyph
from src.glyphs.text_glyph import TextGlyph
from src.items.board import Board
from src.items.item import Item
from src.parsers.frame_parser import FrameParser
from src.solvers.pulp_solver import PulpSolver
from src.utils.coord import Coord
from src.utils.functions import Functions
from src.utils.rule import Rule
from src.utils.side import Side


class Sandwich(Item):
    """Sandwich Constraint."""

    def __init__(self, board: Board, side: Side, index: int, total: int):
        """Initialize a Sandwich instance.

        Args:
            board (Board): The board associated with this sandwich.
            side (Side): The side of the sandwich (e.g., left, right).
            index (int): The index position of the sandwich on the specified side.
            total (int): The total sum of the digits that the sandwich represents.
        """
        super().__init__(board)
        self.side = side
        self.index = index
        self.total = total
        self.position = side.marker(board, self.index) + Coord(0.5, 0.5)

    @classmethod
    def is_sequence(cls) -> bool:
        """Check if this item is a sequence.

        Returns:
            bool: True if this item is a sequence, False otherwise.
        """
        return True

    @classmethod
    def parser(cls) -> FrameParser:
        """Get the parser for this item.

        Returns:
            FrameParser: The parser associated with this sandwich.
        """
        return FrameParser()

    @classmethod
    def extract(cls, board: Board, yaml: Dict) -> Tuple:
        """Extract side, index, and total from the provided YAML configuration.

        Args:
            board (Board): The board associated with this sandwich.
            yaml (Dict): The YAML configuration containing the sandwich data.

        Returns:
            Tuple[Side, int, int]: A tuple containing the side, index, and total.

        Raises:
            AssertionError: If the regex match fails.
        """
        regexp = re.compile(f"([{Side.values()}])([{board.digit_values}])=([0-9]+)")
        match = regexp.match(yaml[cls.__name__])
        assert match is not None
        side_str, offset_str, total_str = match.groups()
        side = Side.create(side_str)
        offset = int(offset_str)
        total = int(total_str)
        return side, offset, total

    @classmethod
    def create(cls, board: Board, yaml: Dict) -> 'Sandwich':
        """Create a Sandwich instance from YAML configuration.

        Args:
            board (Board): The board associated with this sandwich.
            yaml (Dict): The YAML configuration containing the sandwich data.

        Returns:
            Sandwich: A new instance of Sandwich.
        """
        side, offset, total = cls.extract(board, yaml)
        return cls(board, side, offset, total)

    def glyphs(self) -> List[Glyph]:
        """Return a list of glyphs associated with this sandwich.

        Returns:
            List[Glyph]: A list of glyphs representing this sandwich.
        """
        return [TextGlyph('Sandwich', 0, self.position, str(self.total))]

    @property
    def rules(self) -> List[Rule]:
        """Retrieve the rules associated with this sandwich.

        Returns:
            List[Rule]: A list of rules related to this sandwich.
        """
        return [
            Rule(
                'Sandwich',
                1,
                (
                    'Clues outside of the grid give the sum of the digits sandwiched between the 1 and the 9 '
                    'in that row/column '
                )
            )
        ]

    def __repr__(self) -> str:
        """Return a string representation of the Sandwich instance.

        Returns:
            str: A string representation of the Sandwich.
        """
        return f"{self.__class__.__name__}({self.board!r}, {self.side!r}, {self.index}, {self.total})"

    def to_dict(self) -> Dict:
        """Convert the Sandwich instance to a dictionary representation.

        Returns:
            Dict: A dictionary representation of the Sandwich.
        """
        return {self.__class__.__name__: f"{self.side.value}{self.index}={self.total}"}

    def css(self) -> Dict:
        """Get CSS styles for the Sandwich.

        Returns:
            Dict: A dictionary containing CSS styles for the Sandwich.
        """
        return {
            ".SandwichForeground": {
                "font-size": "30px",
                "stroke": "black",
                "stroke-width": 1,
                "fill": "black"
            },
            ".SandwichBackground": {
                "font-size": "30px",
                "stroke": "white",
                "stroke-width": 8,
                "fill": "white",
                "font-weight": "bolder"
            }
        }

    def add_constraint_rc(self,
                          solver: PulpSolver,
                          is_row: bool,
                          index: int,
                          include: Optional[re.Pattern] = None,
                          exclude: Optional[re.Pattern] = None
                          ) -> None:
        """Add constraints for the sandwich in the specified row or column.

        Sets up boolean variables indicating the positions of the digits 1 and the
        maximum digit in the row or column to fulfill the sandwich constraint.
        Optional patterns can be applied to specify inclusion or exclusion of
        specific constraints.

        Args:
            solver (PulpSolver): The solver to which constraints will be added.
            is_row (bool): Indicates whether to apply the constraint to a row
                (True) or column (False).
            index (int): The index of the row or column to which constraints apply.
            include (Optional[re.Pattern]): A regex pattern specifying which entries
                to include in the constraint setup (if any).
            exclude (Optional[re.Pattern]): A regex pattern specifying which entries
                to exclude from the constraint setup (if any).
        """
        label = "Row" if is_row else "Column"
        board_range = self.board.column_range if is_row else self.board.row_range
        position_label = f"{label}_{index}"

        # Set up boolean variables for positions containing 1 or the maximum digit
        bread = LpVariable.dict(
            position_label,
            board_range,
            0,
            Functions.triangular(self.board.maximum_digit),
            LpInteger
        )

        for pos in board_range:
            # Check if the position matches the include or exclude pattern, if provided
            if (include and not include.match(str(pos))) or (exclude and exclude.match(str(pos))):
                continue

            if is_row:
                one = solver.choices[1][index][pos]
                big = solver.choices[self.board.maximum_digit][index][pos]
            else:
                one = solver.choices[1][pos][index]
                big = solver.choices[self.board.maximum_digit][pos][index]

            # Ensure that bread[pos] is 1 if pos has a 1 or the maximum digit
            solver.model += bread[pos] == one + big, f"Bread_{label.lower()}_{index}_{pos}"

    def add_constraint_row(self,
                           solver: PulpSolver,
                           include: Optional[re.Pattern] = None,
                           exclude: Optional[re.Pattern] = None
                           ) -> None:
        """Add constraints for the sandwich in the specified row.

        Args:
            solver (PulpSolver): The solver to which constraints will be added.
            include (Optional[re.Pattern]): A regex pattern specifying which columns
                to include in the constraint setup (if any).
            exclude (Optional[re.Pattern]): A regex pattern specifying which columns
                to exclude from the constraint setup (if any).
        """
        self.add_constraint_rc(solver, True, self.index, include, exclude)

    def add_constraint_column(self,
                              solver: PulpSolver,
                              include: Optional[re.Pattern] = None,
                              exclude: Optional[re.Pattern] = None
                              ) -> None:
        """Add constraints for the sandwich in the specified column.

        Args:
            solver (PulpSolver): The solver to which constraints will be added.
            include (Optional[re.Pattern]): A regex pattern specifying which columns
                to include in the constraint setup (if any).
            exclude (Optional[re.Pattern]): A regex pattern specifying which columns
                to exclude from the constraint setup (if any).

        """
        self.add_constraint_rc(solver, False, self.index, include, exclude)

    def add_constraint(self, solver: PulpSolver) -> None:
        """Add the appropriate constraints for the sandwich based on its orientation.

        Args:
            solver (PulpSolver): The solver to which constraints will be added.
        """
        if self.side.horizontal:
            self.add_constraint_row(solver)
        else:
            self.add_constraint_column(solver, None, None)
