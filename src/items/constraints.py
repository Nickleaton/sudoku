from typing import Dict

from src.items.board import Board
from src.items.composed_item import ComposedItem
from src.items.item import Item


class Constraints(ComposedItem):

    def __init__(self, board: Board):
        super().__init__(board, [])
        self._n = 0

    @classmethod
    def create(cls, board: Board, yaml: Dict) -> Item:
        result = cls(board)
        for part in yaml[cls.__name__]:
            result.add(Item.create(board, part))
        return result
