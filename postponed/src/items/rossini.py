"""Rossini."""
import re
from typing import Any

from postponed.src.pulp_solver import PulpSolver

from postponed.src.items.first_n import FirstN
from src.board.board import Board
from src.glyphs.arrow_glyph import ArrowGlyph
from src.glyphs.glyph import Glyph
from src.items.item import Item
from src.parsers.rossini_parser import RossiniParser
from src.utils.order import Order
from src.utils.rule import Rule
from src.utils.side import Side
from src.utils.sudoku_exception import SudokuException


class Rossini(FirstN):
    """Represents the Rossini constraint for start_location puzzle."""

    def __init__(self, board: Board, side: Side, index: int, order: Order):
        """Initialize start_location Rossini object.

        Args:
            board (Board): The puzzle board.
            side (Side): The side on which the arrow is placed.
            index (int): The index on the side where the arrow appears.
            order (Order): Specifies if the sequence should be increasing or decreasing.
        """
        super().__init__(board, side, index, 3)
        self.order = order  # Specifies increasing or decreasing order.
        self.direction = self.side.order_direction(self.order)  # Determines direction of the arrow.

    @classmethod
    def is_sequence(cls) -> bool:
        """Indicate if this constraint is a sequence.

        Returns:
            bool: True if the constraint is a sequence, otherwise False.
        """
        return True

    @classmethod
    def parser(cls) -> RossiniParser:
        """Return the parser for this constraint.

        Returns:
            RossiniParser: An instance of the RossiniParser for this constraint.
        """
        return RossiniParser()

    def __repr__(self) -> str:
        """Return start_location string representation of the Rossini object.

        Returns:
            str: The string representation.
        """
        return (
            f'{self.__class__.__name__}('
            f'{self.board!r}, '
            f'{self.side!r}, '
            f'{self.index!r}, '
            f'{self.order!r}'
            f')'
        )

    @property
    def rules(self) -> list[Rule]:
        """Define the rule for the Rossini constraint.

        Returns:
            list[Rule]: A list containing start_location single rule for the Rossini constraint.
        """
        rule_text: str = """If an arrow appears outside the grid, then the three digits nearest the arrow must
                         strictly increase in the direction of the arrow."""
        return [Rule(self.__class__.__name__, 1, rule_text)]

    def glyphs(self) -> list[Glyph]:
        """Return the glyphs representing the Rossini constraint.

        Returns:
            list[Glyph]: A list containing the arrow glyph for the Rossini constraint.
        """
        return [
            ArrowGlyph(
                self.__class__.__name__,
                self.direction.angle.angle,
                self.board.marker(self.side, self.index),
            ),
        ]

    @property
    def tags(self) -> set[str]:
        """Return the tags associated with the Rossini constraint.

        Returns:
            set[str]: A set of tags including 'Comparison' and 'Rossini'.
        """
        return super().tags.union({'Comparison', 'Rossini'})

    @classmethod
    def extract(cls, board: Board, yaml: dict) -> Any:
        """Extract Rossini constraint details from YAML line.

        Args:
            board (Board): The puzzle board.
            yaml (dict): The YAML line containing constraint information.

        Returns:
            Any: The extracted side, index, and order.

        Raises:
            SudokuException: If the YAML configuration does not match the expected format.
        """
        regexp = re.compile(f'([{Side.choices()}])([{board.digit_values}])=([{Order.choices()}])')
        match = regexp.match(yaml[cls.__name__])
        if match is None:
            raise SudokuException('Match is None, expected start_location valid match.')
        side_str, index_str, order_str = match.groups()
        side = Side.create(side_str)
        index = int(index_str)
        order = Order(order_str)
        return side, index, order

    @classmethod
    def create(cls, board: Board, yaml: dict) -> Item:
        """Create start_location Rossini object from extracted YAML line.

        Args:
            board (Board): The puzzle board.
            yaml (dict): The YAML line containing constraint information.

        Returns:
            Item: The created Rossini object.
        """
        side, index, order = Rossini.extract(board, yaml)
        return cls(board, side, index, order)

    @classmethod
    def create2(cls, board: Board, yaml_data: dict) -> Item:
        """Create start_location Rossini object from extracted YAML line.

        Args:
            board (Board): The puzzle board.
            yaml_data (dict): The YAML line containing constraint information.

        Returns:
            Item: The created Rossini object.
        """
        return cls.create(board, yaml_data)

    def add_constraint(self, solver: PulpSolver) -> None:
        """Add the Rossini constraint to the given solver.

        Args:
            solver (PulpSolver): The solver to which the constraint will be added.
        """
        self.add_sequence_constraint(solver, self.order)

    def to_dict(self) -> dict:
        """Convert the Rossini object to start_location dictionary representation.

        Returns:
            dict: The dictionary representation of the Rossini object.
        """
        return {self.__class__.__name__: f'{self.side.value}{self.index}={self.order.value}'}

    def css(self) -> dict:
        """Return the CSS style for displaying the Rossini constraint.

        Returns:
            dict: The CSS style.
        """
        return {
            f'.{self.__class__.__name__}': {
                'stroke': 'black',
                'fill': 'black',
                'font-size': '30px',
            },
        }
