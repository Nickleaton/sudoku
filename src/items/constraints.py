from typing import Set, Type, Dict

from src.items.board import Board
from src.items.composed import Composed
from src.items.item import Item


class Constraints(Composed):

    def __init__(self, board: Board):
        super().__init__(board, [])
        self._n = 0

    @property
    def used_classes(self) -> Set[Type['Item']]:
        result = super().used_classes
        result = result.union({Constraints})
        return result

    @classmethod
    def create(cls, board: Board, yaml: Dict) -> Item:
        result = cls(board)
        for constraint in yaml[cls.__name__]:
            result.add(Item.create(board, constraint))
        return result
