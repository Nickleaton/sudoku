from typing import List

from pulp import lpSum

from src.glyphs.glyph import Glyph, ArrowGlyph, TextGlyph
from src.items.board import Board
from src.items.cell import Cell
from src.items.composed import Composed
from src.items.item import Item
from src.solvers.pulp_solver import PulpSolver
from src.utils.order import Order
from src.utils.rule import Rule
from src.utils.side import Side


class Frame(Item):

    def __init__(self, board: Board, side: Side, index: int, total: int):
        super().__init__(board)
        self.side = side
        self.index = index
        self.total = total
        self.direction = self.side.order_direction(Order.INCREASING)
        self.offset = self.side.order_offset(Order.INCREASING)
        self.coords = []
        self.coords.append(self.side.start_cell(self.board, self.index))
        self.coords.append(self.coords[0] + self.offset)
        self.coords.append(self.coords[1] + self.offset)
        self.cells = [Cell.make(self.board, coord.row, coord.column) for coord in self.coords]

    @property
    def name(self) -> str:
        return f"{self.__class__.__name__}_{self.side.name}_{self.index}"

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}"
            f"("
            f"{self.board!r}, "
            f"{self.side!r}, "
            f"{self.total}"
            f")"
        )

    @property
    def rules(self) -> List[Rule]:
        return [
            Rule(
                'Frame',
                1,
                "Numbers outside the frame equal the sum of the first three numbers in the "
                "corresponding row or column in the given direction"
            )
        ]

    @property
    def glyphs(self) -> List[Glyph]:
        return [
            TextGlyph(
                'FrameText',
                0,
                self.side.marker(self.board, self.index).center,
                str(self.total)
            )
        ]

    @property
    def tags(self) -> set[str]:
        return super().tags.union({'Comparison', 'Frame'})

    @classmethod
    def create(cls, name: str, board: Board, yaml: str) -> Item:
        side = Side.create(yaml[0])
        index = int(yaml[1])
        total = int(yaml.split('=')[1])
        return cls(board, side, index, total)

    def add_constraint(self, solver: PulpSolver) -> None:
        values = [
            solver.values[self.cells[0].row][self.cells[0].column],
            solver.values[self.cells[1].row][self.cells[1].column],
            solver.values[self.cells[2].row][self.cells[2].column]
        ]
        solver.model += lpSum(values) == self.total, f"{self.name}"


class Frames(Composed):
    """ Collection of Frames """

    def __init__(self, board: Board, items: List[Frame]):
        super().__init__(board, items)

    @classmethod
    def create(cls, name: str, board: Board, yaml: List[str]) -> Item:
        return cls(board, [Frame.create('Frame', board, y) for y in yaml])
