from typing import List, Dict

from src.items.anti import Anti
from src.items.board import Board
from src.items.item import Item
from src.utils.coord import Coord
from src.utils.direction import Direction
from src.utils.rule import Rule


class AntiKing(Anti):

    def __init__(self, board: Board):
        super().__init__(board, list(board.digit_range))

    def offsets(self) -> List[Coord]:
        return Direction.kings()

    @classmethod
    def create(cls, board: Board, yaml: Dict) -> Item:
        return AntiKing(board)

    @property
    def tags(self) -> set[str]:
        return super().tags.union({'King'})

    @property
    def rules(self) -> List[Rule]:
        return [
            Rule("AntiKing", 1, "Identical digits cannot be separated by a King's move")
        ]

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.board!r})"

    def to_dict(self) -> Dict:
        return {self.__class__.__name__: None}
