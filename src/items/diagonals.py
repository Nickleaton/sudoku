from typing import List, Dict

from src.items.board import Board
from src.items.item import Item
from src.items.region import Region
from src.utils.rule import Rule


class Diagonal(Region):

    @classmethod
    def create(cls, board: Board, yaml: Dict) -> Item:
        return cls(board)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.board!r})"

    @property
    def rules(self) -> List[Rule]:
        return [Rule('Diagonal', 1, "Digits along a blue diagonal cannot repeat")]

    @property
    def tags(self) -> set[str]:
        return super().tags.union({'Diagonal', 'Uniqueness'})

    def to_dict(self) -> Dict:
        return {self.__class__.__name__: None}

    def css(self) -> Dict:
        return {
            ".Diagonal": {
                "stroke": "blue",
                "stroke-width": "3px"
            }
        }
