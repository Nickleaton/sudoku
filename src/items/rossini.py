from typing import List, Dict, Any

from src.glyphs.glyph import Glyph, ArrowGlyph
from src.items.board import Board
from src.items.first_n import FirstN
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

    @staticmethod
    def validate(board: Board, yaml: Any) -> List[str]:
        if not isinstance(yaml, str):
            return [f"Expected str, got {yaml!r}"]
        if "=" not in yaml:
            return [f"Expecting {{sidr}}{{index}}={{order}}, got {yaml!r}"]
        ref_str, order_str = yaml.split("=")
        result = FirstN.validate(board, ref_str)
        if len(result) > 0:
            return result
        if not Order.valid(order_str):
            result.append(f"Invalid Order {order_str}")
        return result

    @staticmethod
    def extract(board: Board, yaml: Any) -> Any:
        ref_str, order_str = yaml.split("=")
        side, index = FirstN.extract(board, ref_str)
        order = Order.create(order_str)
        return side, index, order

    @classmethod
    def create(cls, name: str, board: Board, yaml: Dict | List | str | int | None) -> 'Rossini':
        Rossini.validate(board, yaml)
        side, index, order = Rossini.extract(board, yaml)
        return cls(board, side, index, order)

    def add_constraint(self, solver: PulpSolver) -> None:
        self.add_sequence_constraint(solver, self.order)
