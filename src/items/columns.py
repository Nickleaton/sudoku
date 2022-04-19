from typing import Dict, List

from src.items.board import Board
from src.items.column import Column
from src.items.item import Item
from src.items.region_sets import StandardRegionSet


class Columns(StandardRegionSet):

    def __init__(self, board: Board):
        super().__init__(board, [Column(board, i) for i in board.column_range])

    @classmethod
    def create(cls, name: str, board: Board, yaml: Dict | List | str | int | None) -> Item:
        Item.check_yaml_none(yaml)
        return Columns(board)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.board!r})"
