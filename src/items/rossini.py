import re
from typing import List, Any, Dict, Callable

from src.glyphs.glyph import Glyph
from src.glyphs.arrow_glyph import ArrowGlyph
from src.items.board import Board
from src.items.first_n import FirstN
from src.items.item import Item
from src.solvers.pulp_solver import PulpSolver
from src.utils.order import Order
from src.utils.rule import Rule
from src.utils.side import Side


class Rossini(FirstN):

    def __init__(self, board: Board, side: Side, index: int, order: Order):
        super().__init__(board, side, index)
        # Increasing or decreasing
        self.order = order
        # Which direction for the arrow
        self.direction = self.side.order_direction(self.order)

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}"
            f"("
            f"{self.board!r}, "
            f"{self.side!r}, "
            f"{self.index!r}, "
            f"{self.order!r}"
            f")"
        )

    @property
    def rules(self) -> List[Rule]:
        return [
            Rule(
                'Rossini',
                1,
                "If an arrow appears outside the grid, then the three digits nearest the arrow must "
                "strictly increase in the direction of the arrow."
            )
        ]

    def glyphs(self) -> List[Glyph]:
        return [
            ArrowGlyph(
                'Rossini',
                self.direction.angle.angle,
                self.side.marker(self.board, self.index)
            )
        ]

    @property
    def tags(self) -> set[str]:
        return super().tags.union({'Comparison', 'Rossini'})

    @classmethod
    def extract(cls, board: Board, yaml: Dict) -> Any:
        regexp = re.compile(f"([{Side.values()}])([{board.digit_values}])=([{Order.values()}])")
        match = regexp.match(yaml[cls.__name__])
        assert match is not None
        side_str, index_str, order_str = match.groups()
        side = Side.create(side_str)
        index = int(index_str)
        order = Order.create(order_str)
        return side, index, order

    @classmethod
    def create(cls, board: Board, yaml: Dict) -> Item:
        side, index, order = Rossini.extract(board, yaml)
        return cls(board, side, index, order)

    def add_constraint(self, solver: PulpSolver) -> None:
        self.add_sequence_constraint(solver, self.order)

    def to_dict(self) -> Dict:
        return {self.__class__.__name__: f"{self.side.value}{self.index}={self.order.value}"}

    def css(self) -> Dict:
        return {
            ".Rossini": {
                "stroke": "black",
                "fill": "black",
                "font-size": "30px"
            }
        }
