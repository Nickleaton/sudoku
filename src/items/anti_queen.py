from typing import List, Dict

from src.items.anti import Anti
from src.items.board import Board
from src.items.constraint_exception import ConstraintException
from src.items.item import Item
from src.utils.coord import Coord
from src.utils.rule import Rule


class AntiQueen(Anti):

    def __init__(self, board: Board, digits: List[int]):
        super().__init__(board, digits)
        self.digits = digits

    def offsets(self) -> List[Coord]:
        results = []
        for distance in self.board.digit_range:
            results.append(Coord(-1, -1) * distance)
            results.append(Coord(1, -1) * distance)
            results.append(Coord(-1, 1) * distance)
            results.append(Coord(1, 1) * distance)
        return results

    @property
    def tags(self) -> set[str]:
        return super().tags.union({'Queen'})

    @classmethod
    def create(cls, name: str, board: Board, yaml: Dict | List | str | int | None) -> Item:
        if not isinstance(yaml, list):
            raise ConstraintException(f"Expecting list, got {yaml!r}")
        return AntiQueen(board, yaml)

    @property
    def rules(self) -> List[Rule]:
        digit_str = ' '.join([str(digit) for digit in self.digits])
        return [
            Rule("AntiQueen", 1, f"Digits [{digit_str}] cannot be separated by a Queen's move")
        ]

    def __repr__(self) -> str:
        return f"{self.name}({self.board!r}, {self.digits!r})"
