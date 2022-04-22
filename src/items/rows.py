from src.items.board import Board
from src.items.item import Item, YAML
from src.items.region_sets import StandardRegionSet
from src.items.row import Row


class Rows(StandardRegionSet):

    def __init__(self, board: Board):
        super().__init__(board, [Row(board, i) for i in board.row_range])

    @classmethod
    def create(cls, name: str, board: Board, yaml: YAML) -> Item:
        cls.validate(board, yaml)
        return Rows(board)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.board!r})"
