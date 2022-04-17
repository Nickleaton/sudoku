from typing import Dict, List

from src.items.board import Board
from src.items.box import Box
from src.items.column import Column
from src.items.composed import Composed
from src.items.disjoint_group import DisjointGroup
from src.items.item import Item
from src.items.row import Row


class RegionSet(Composed):
    pass


class StandardRegionSet(RegionSet):
    pass


class Columns(StandardRegionSet):

    def __init__(self, board: Board):
        super().__init__(board, [Column(board, i) for i in board.column_range])

    @classmethod
    def create(cls, name: str, board: Board, yaml: Dict | List | str | int | None) -> Item:
        Item.check_yaml_none(yaml)
        return Columns(board)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.board!r})"


class Rows(StandardRegionSet):

    def __init__(self, board: Board):
        super().__init__(board, [Row(board, i) for i in board.row_range])

    @classmethod
    def create(cls, name: str, board: Board, yaml: Dict | List | str | int | None) -> Item:
        Item.check_yaml_none(yaml)
        return Rows(board)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.board!r})"


class Boxes(StandardRegionSet):

    def __init__(self, board: Board):
        super().__init__(board, [Box(board, i) for i in board.box_range])

    @classmethod
    def create(cls, name: str, board: Board, yaml: Dict | List | str | int | None) -> Item:
        Item.check_yaml_none(yaml)
        return Boxes(board)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.board!r})"


class DisjointGroups(StandardRegionSet):

    def __init__(self, board: Board):
        super().__init__(board, [DisjointGroup(board, i) for i in board.digit_range])

    @classmethod
    def create(cls, name: str, board: Board, yaml: Dict | List | str | int | None) -> Item:
        Item.check_yaml_none(yaml)
        return DisjointGroups(board)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.board!r})"
