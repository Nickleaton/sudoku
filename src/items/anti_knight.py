from typing import List, Any, Dict

from src.items.anti import Anti
from src.items.board import Board
from src.items.item import Item
from src.utils.coord import Coord
from src.utils.rule import Rule


class AntiKnight(Anti):

    def __init__(self, board: Board):
        super().__init__(board, list(board.digit_range))

    def offsets(self) -> List[Coord]:
        return \
            [
                Coord(-1, -2),
                Coord(1, -2),
                Coord(-2, -1),
                Coord(-2, 1),
                Coord(-1, 2),
                Coord(1, 2),
                Coord(2, 1),
                Coord(2, -1)
            ]

    @property
    def tags(self) -> set[str]:
        return super().tags.union({'Knight'})

    @classmethod
    def create(cls, board: Board, yaml: Dict) -> Item:
        return AntiKnight(board)

    @property
    def rules(self) -> List[Rule]:
        return [
            Rule("AntiKnight", 1, "Identical digits cannot be separated by a knight's move")
        ]

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.board!r})"

    def to_dict(self) -> Dict:
        return {self.__class__.__name__: None}
