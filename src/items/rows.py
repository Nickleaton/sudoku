from typing import Dict, List

from src.items.board import Board
from src.items.item import Item
from src.items.region_sets import StandardRegionSet
from src.items.row import Row


class Rows(StandardRegionSet):

    def __init__(self, board: Board):
        super().__init__(board, [Row(board, i) for i in board.row_range])

    @classmethod
    def create(cls, name: str, board: Board, yaml: Dict | List | str | int | None) -> Item:
        Item.check_yaml_none(yaml)
        return Rows(board)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.board!r})"
