from typing import List, Any, Dict

from src.glyphs.glyph import Glyph, TextGlyph
from src.items.board import Board
from src.items.first_n import FirstN
from src.items.item import Item
from src.solvers.pulp_solver import PulpSolver
from src.utils.coord import Coord
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

    @classmethod
    def extract(cls, board: Board, yaml: Any) -> Any:
        data = yaml['Outside']
        side = Side.create(data[0])
        index = int(data[1])
        digits = [int(digit) for digit in data[3:]]
        return side, index, digits

    @classmethod
    def create(cls, board: Board, yaml: Any) -> Item:
        side, index, digits = Outside.extract(board, yaml)
        return cls(board, side, index, digits)

    def add_constraint(self, solver: PulpSolver) -> None:
        self.add_contains_constraint(solver, self.digits)

    def to_dict(self) -> Dict:
        return {self.__class__.__name__: f"{self.side.value}{self.index}={''.join([str(d) for d in self.digits])}"}
