from typing import List, Dict, Sequence

from src.glyphs.glyph import Glyph, ArrowGlyph
from src.items.board import Board
from src.items.cell import Cell
from src.items.composed import Composed
from src.items.constraint_exception import ConstraintException
from src.items.item import Item
from src.solvers.pulp_solver import PulpSolver
from src.utils.order import Order
from src.utils.rule import Rule
from src.utils.side import Side


class Rossini(Item):

    def __init__(self, board: Board, side: Side, index: int, order: Order):
        super().__init__(board)
        self.side = side
        self.index = index
        self.order = order
        self.direction = self.side.order_direction(self.order)
        self.offset = self.side.order_offset()
        self.coords = []
        self.coords.append(self.side.start_cell(self.board, self.index))
        self.coords.append(self.coords[0] + self.offset)
        self.coords.append(self.coords[1] + self.offset)
        self.cells = [Cell.make(self.board, int(coord.row), int(coord.column)) for coord in self.coords]

    @property
    def name(self) -> str:
        return f"{self.__class__.__name__}_{self.side.name}_{self.index}_{self.order.name}"

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
    def create(cls, name: str, board: Board, yaml: Dict | List | str | int | None) -> 'Rossini':
        if not isinstance(yaml, str):
            raise ConstraintException(f"Expecting str, got {yaml!r}")
        side = Side.create(yaml[0])
        index = int(yaml[1])
        order = Order.create(yaml[2])
        return cls(board, side, index, order)

    def add_constraint(self, solver: PulpSolver) -> None:
        values = [
            solver.values[self.cells[0].row][self.cells[0].column],
            solver.values[self.cells[1].row][self.cells[1].column],
            solver.values[self.cells[2].row][self.cells[2].column]
        ]
        if self.order == Order.INCREASING:
            solver.model += values[0] + 1 <= values[1], f"{self.name}_1"
            solver.model += values[1] + 1 <= values[2], f"{self.name}_2"
        else:
            solver.model += values[0] >= values[1] + 1, f"{self.name}_1"
            solver.model += values[1] >= values[2] + 1, f"{self.name}_2"


class Rossinis(Composed):
    """ Collection of Rossini """

    def __init__(self, board: Board, rossinis: Sequence[Rossini]):
        super().__init__(board, rossinis)

    @classmethod
    def create(cls, name: str, board: Board, yaml: Dict | List | str | int | None) -> Item:
        if not isinstance(yaml, list):
            raise ConstraintException(f"Expecting list, got {yaml!r}")
        return cls(board, [Rossini.create('Rossini', board, y) for y in yaml])
