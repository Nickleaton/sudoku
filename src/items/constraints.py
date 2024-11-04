from typing import Dict, Type

from src.items.board import Board
from src.items.composed_item import ComposedItem
from src.items.item import Item


class Constraints(ComposedItem):

    def __init__(self, board: Board):
        super().__init__(board, [])
        self._n = 0

    # Creation and schema

    @classmethod
    def create(cls, board: Board, yaml: Dict) -> 'Constraints':
        result = cls(board)
        for key, value in yaml[cls.__name__].items():
            sub_yaml: Dict = {} if value is None else value
            sub_class: Type[Item] = Item.classes[key]
            if sub_class.is_composite():
                result.add(sub_class.create(board, sub_yaml))
            elif isinstance(sub_yaml, list):
                for data in sub_yaml:
                    result.add(sub_class.create(board, data))
        return result
