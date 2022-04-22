from src.items.board import Board
from src.items.disjoint_group import DisjointGroup
from src.items.item import Item, YAML
from src.items.region_sets import StandardRegionSet


class DisjointGroups(StandardRegionSet):

    def __init__(self, board: Board):
        super().__init__(board, [DisjointGroup(board, i) for i in board.digit_range])

    @classmethod
    def create(cls, name: str, board: Board, yaml: YAML) -> Item:
        cls.validate(board, yaml)
        return DisjointGroups(board)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.board!r})"
