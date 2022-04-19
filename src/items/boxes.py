from typing import Dict, List

from src.items.board import Board
from src.items.box import Box
from src.items.item import Item
from src.items.region_sets import StandardRegionSet


class Boxes(StandardRegionSet):

    def __init__(self, board: Board):
        assert board.box_range is not None
        super().__init__(board, [Box(board, i) for i in board.box_range])

    @classmethod
    def create(cls, name: str, board: Board, yaml: Dict | List | str | int | None) -> Item:
        Item.check_yaml_none(yaml)
        return Boxes(board)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.board!r})"
