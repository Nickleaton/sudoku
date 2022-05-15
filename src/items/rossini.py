from typing import List, Any, Dict

from src.glyphs.glyph import Glyph, ArrowGlyph
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

    @property
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
        ref_str, order_str = yaml[cls.__name__].split("=")
        side = Side.create(ref_str[0])
        index = int(ref_str[1])
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
                f"ont-size": "30px"
            }
        }
