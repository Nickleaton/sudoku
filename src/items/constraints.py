from typing import Dict

from src.items.board import Board
from src.items.composed_item import ComposedItem
from src.items.item import Item
from src.items.known import Known
from src.utils.sudoku_exception import SudokuException


class Constraints(ComposedItem):

    def __init__(self, board: Board):
        super().__init__(board, [])
        self._n = 0

    @classmethod
    def create(cls, board: Board, yaml: Dict) -> Item:
        result = cls(board)
        for name, value in yaml[cls.__name__].items():
            if name not in cls.classes:
                raise SudokuException(f"Unknown constraint class {name}")
            elif name == 'Known':
                result.add(Known.create(board, {name: value}))
            elif isinstance(value, list):
                for item in value:
                    result.add(cls.classes[name].create(board, item))
            # Exception for Known which takes a list in one chunk

            else:
                result.add(cls.classes[name].create(board, {name:value}))
        return result
