"""Rossini."""
import re
from typing import Any

from src.glyphs.arrow_glyph import ArrowGlyph
from src.glyphs.glyph import Glyph
from src.items.board import Board
from src.items.first_n import FirstN
from src.items.item import Item
from src.parsers.rossini_parser import RossiniParser
from src.solvers.pulp_solver import PulpSolver
from src.utils.order import Order
from src.utils.rule import Rule
from src.utils.side import Side
from src.utils.sudoku_exception import SudokuException


class Rossini(FirstN):
    """Represents the Rossini constraint for a puzzle."""

    def __init__(self, board: Board, side: Side, index: int, order: Order):
        """Initialize a Rossini object.

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
        """Return True if this item is a sequence."""
        return True

    @classmethod
    def parser(cls) -> RossiniParser:
        """Return the parser for this item."""
        return RossiniParser()

    def __repr__(self) -> str:
        """Return a string representation of the Rossini object.

        Returns:
            str: The string representation.
        """
        return (
            f"{self.__class__.__name__}("
            f"{self.board!r}, "
            f"{self.side!r}, "
            f"{self.index!r}, "
            f"{self.order!r}"
            f")"
        )

    @property
    def rules(self) -> list[Rule]:
        """Define the rule for the Rossini constraint.

        Returns:
            list[Rule]: A list containing a single rule for the Rossini constraint.
        """
        return [
            Rule(
                'Rossini',
                1,
                "If an arrow appears outside the grid, then the three digits nearest the arrow must "
                "strictly increase in the direction of the arrow."
            )
        ]

    def glyphs(self) -> list[Glyph]:
        """Return the glyphs representing the Rossini constraint.

        Returns:
            list[Glyph]: A list containing the arrow glyph for the Rossini constraint.
        """
        return [
            ArrowGlyph(
                'Rossini',
                self.direction.angle.angle,
                self.side.marker(self.board, self.index)
            )
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
        """Extract Rossini constraint details from YAML data.

        Args:
            board (Board): The puzzle board.
            yaml (dict): The YAML data containing constraint information.

        Returns:
            Any: The extracted side, index, and order.
        """
        regexp = re.compile(f"([{Side.values()}])([{board.digit_values}])=([{Order.values()}])")
        match = regexp.match(yaml[cls.__name__])
        if match is None:
            raise SudokuException("Match is None, expected a valid match.")
        side_str, index_str, order_str = match.groups()
        side = Side.create(side_str)
        index = int(index_str)
        order = Order(order_str)
        return side, index, order

    @classmethod
    def create(cls, board: Board, yaml: dict) -> Item:
        """Create a Rossini object from extracted YAML data.

        Args:
            board (Board): The puzzle board.
            yaml (dict): The YAML data containing constraint information.

        Returns:
            Item: The created Rossini object.
        """
        side, index, order = Rossini.extract(board, yaml)
        return cls(board, side, index, order)

    def add_constraint(self, solver: PulpSolver) -> None:
        """Add the Rossini constraint to the given solver.

        Args:
            solver (PulpSolver): The solver to which the constraint will be added.
        """
        self.add_sequence_constraint(solver, self.order)

    def to_dict(self) -> dict:
        """Convert the Rossini object to a dictionary representation.

        Returns:
            dict: The dictionary representation of the Rossini object.
        """
        return {self.__class__.__name__: f"{self.side.value}{self.index}={self.order.value}"}

    def css(self) -> dict:
        """Return the CSS style for displaying the Rossini constraint.

        Returns:
            dict: The CSS style.
        """
        return {
            ".Rossini": {
                "stroke": "black",
                "fill": "black",
                "font-size": "30px"
            }
        }
