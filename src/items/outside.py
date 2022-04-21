from typing import List, Dict, Any

from src.glyphs.glyph import Glyph, TextGlyph
from src.items.board import Board
from src.items.cell import Cell
from src.items.first_n import FirstN
from src.items.region import Region
from src.solvers.pulp_solver import PulpSolver
from src.utils.coord import Coord
from src.utils.order import Order
from src.utils.rule import Rule
from src.utils.side import Side


class Outside(FirstN):

    def __init__(self, board: Board, side: Side, index: int, digits: List[int]):
        super().__init__(board, side, index)
        self.digits = digits

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
        self.add_contains_constraint(solver, self.digits)
