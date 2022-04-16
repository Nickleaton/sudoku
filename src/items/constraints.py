from typing import Set, Type, Dict, List

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
    def create(cls, name: str, board: Board, yaml: Dict | List | str | int | None) -> Item:
        result = cls(board)
        Item.check_yaml_list(yaml)
        for constraint in yaml:
            if isinstance(constraint, str):
                result.add(Item.create(constraint, board, constraint))
            else:
                for name, sub_constraint in constraint.items():
                    result.add(Item.create(name, board, sub_constraint))

        return result
