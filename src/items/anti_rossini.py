"""AntiRossini."""
import re
from typing import Any

from src.glyphs.arrow_glyph import ArrowGlyph
from src.glyphs.glyph import Glyph
from src.items.board import Board
from src.items.first_n import FirstN
from src.items.item import Item
from src.items.rossini import Rossini
from src.solvers.pulp_solver import PulpSolver
from src.utils.order import Order
from src.utils.rule import Rule
from src.utils.side import Side


class AntiRossini(FirstN):
    """Represent the Anti-Rossini rule in a puzzle.

    The three digits nearest an arrow must strictly increase in the direction of the arrow.
    """

    def __init__(self, board: Board, side: Side, index: int, order: Order) -> None:
        """Initialize the AntiRossini rule with the specified board, side, index, and order.

        Args:
            board (Board): The game board.
            side (Side): The side of the arrow.
            index (int): The index for the arrow placement.
            order (Order): The order direction for the arrow.
        """
        super().__init__(board, side, index)
        self.order = order
        self.direction = self.side.order_direction(self.order)

    def __repr__(self) -> str:
        """Return a string representation of the AntiRossini instance.

        Returns:
            str: A string representation of the instance.
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
        """Return the rules associated with the AntiRossini class.

        Returns:
            list[Rule]: The list of rules.
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
        """Generate glyphs for visual representation of the rule.

        Returns:
            list[Glyph]: A list of glyphs, specifically an ArrowGlyph.
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
        """Return the tags associated with this rule.

        Returns:
            set[str]: A set of tags for the AntiRossini rule.
        """
        return super().tags.union({'Comparison', 'Rossini'})

    @classmethod
    def extract(cls, board: Board, yaml: dict) -> Any:
        """Extract the side, index, and order from the YAML configuration.

        Args:
            board (Board): The game board.
            yaml (dict): The YAML dictionary containing the rule configuration.

        Returns:
            tuple[Side, int, Order]: The extracted side, index, and order.
        """
        regexp = re.compile(f"([{Side.values()}])([{board.digit_values}])=([{Order.values()}])")
        match = regexp.match(yaml[cls.__name__])
        if not match:
            raise ValueError(f"Invalid format for {cls.__name__} in YAML: {yaml[cls.__name__]}")

        side_str, index_str, order_str = match.groups()
        side = Side.create(side_str)
        index = int(index_str)
        order = Order(order_str)
        return side, index, order

    @classmethod
    def create(cls, board: Board, yaml: dict) -> Item:
        """Create an AntiRossini instance from the YAML configuration.

        Args:
            board (Board): The game board.
            yaml (dict): The YAML dictionary containing the rule configuration.

        Returns:
            Item: An instance of the AntiRossini class.
        """
        side, index, order = Rossini.extract(board, yaml)
        return cls(board, side, index, order)

    @classmethod
    def create2(cls, board: Board, yaml_data: dict) -> Item:
        return cls.create(board, yaml_data)

    def add_constraint(self, solver: PulpSolver) -> None:
        """Add the necessary constraints for this rule to the solver.

        Args:
            solver (PulpSolver): The solver instance.
        """
        self.add_sequence_constraint(solver, self.order)

    def to_dict(self) -> dict:
        """Convert the AntiRossini instance to a dictionary representation.

        Returns:
            dict: A dictionary representation of the instance.
        """
        return {self.__class__.__name__: f"{self.side.value}{self.index}={self.order.value}"}

    def css(self) -> dict:
        """Return the CSS styling for this rule.

        Returns:
            dict: A dictionary containing CSS properties.
        """
        return {
            ".Rossini": {
                "stroke": "black",
                "fill": "black",
                "font-size": "30px"
            }
        }
