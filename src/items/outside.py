from typing import List, Dict, Any

from pulp import lpSum

from src.glyphs.glyph import Glyph, TextGlyph
from src.items.board import Board
from src.items.cell import Cell
from src.items.item import Item
from src.solvers.pulp_solver import PulpSolver
from src.utils.coord import Coord
from src.utils.order import Order
from src.utils.rule import Rule
from src.utils.side import Side


class Outside(Item):

    def __init__(self, board: Board, side: Side, index: int, digits: List[int]):
        super().__init__(board)
        self.side = side
        self.index = index
        self.digits = digits
        self.direction = self.side.order_direction(Order.INCREASING)
        self.offset = self.side.order_offset()
        self.reference = self.side.start_cell(self.board, self.index) - self.offset
        self.coords = []
        self.coords.append(self.side.start_cell(self.board, self.index))
        self.coords.append(self.coords[0] + self.offset)
        self.coords.append(self.coords[1] + self.offset)
        self.cells = [Cell.make(self.board, int(coord.row), int(coord.column)) for coord in self.coords]

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}"
            f"("
            f"{self.board!r}, "
            f"{self.side!r}, "
            f"{self.index!r}, "
            f"{self.digits!r}"
            f")"
        )

    @property
    def rules(self) -> List[Rule]:
        return [
            Rule(
                'Outside',
                1,
                "A clue outside of a row or column tells you some digits that must appear "
                "in the first three cells nearest the clue in that rwo or column."
            )
        ]

    @property
    def glyphs(self) -> List[Glyph]:
        return [
            TextGlyph('Outside', 0, self.reference + Coord(0.5, 0.5), "".join([str(digit) for digit in self.digits]))
        ]

    @property
    def tags(self) -> set[str]:
        return super().tags.union({'Comparison', 'Order'})

    @staticmethod
    def validate(board: Board, yaml: Any) -> List[str]:
        if not isinstance(yaml, str):
            return [f"Expected str, got {yaml!r}"]
        if len(yaml) < 4:
            return [f"Expected side|index|digits, got {yaml!r}"]
        result = []
        if not Side.valid(yaml[0]):
            result.append(f"Side not valid {yaml[0]}")
        if not yaml[1].isdigit():
            result.append(f"Index not valid {yaml[1]}")
            return result
        if int(yaml[1]) not in board.digit_range:
            result.append(f"Index outside range {yaml[1]}")
        digits = yaml[3:]
        for digit in digits:
            if int(digit) not in board.digit_range:
                result.append(f"Not a valid digit {digit}")
        return result

    @staticmethod
    def extract(board: Board, yaml: Any) -> Any:
        side = Side.create(yaml[0])
        index = int(yaml[1])
        digits = [int(digit) for digit in yaml[3:]]
        return side, index, digits

    @classmethod
    def create(cls, name: str, board: Board, yaml: Dict | List | str | int | None) -> 'Outside':
        Outside.validate(board, yaml)
        side, index, digits = Outside.extract(board, yaml)
        return cls(board, side, index, digits)

    def add_constraint(self, solver: PulpSolver) -> None:
        for digit in self.digits:
            choice_total = lpSum([solver.choices[digit][cell.row][cell.column] for cell in self.cells])
            solver.model += choice_total == 1, f"{self.name}_{digit}"
