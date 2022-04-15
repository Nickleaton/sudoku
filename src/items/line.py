from typing import List, Dict

from src.items.board import Board
from src.items.cell import Cell
from src.items.item import Item
from src.items.region import Region
from src.utils.rule import Rule


class Line(Region):

    def __init__(self, board: Board, cells: List[Cell]):
        super().__init__(board)
        self.add_items(cells)

    @property
    def name(self) -> str:
        return f"{self.__class__.__name__}_{self.cells[0].row}_{self.cells[0].column}"

    @classmethod
    def create(cls, name: str, board: Board, yaml: Dict | List | str | int | None) -> Item:
        Item.check_yaml_list(yaml)
        cells = [Cell.make(board, r, c) for r, c in yaml]
        return cls(board, cells)

    def __repr__(self) -> str:
        item_str = ", ".join(repr(item) for item in self.items)
        return f"{self.__class__.__name__}({self.board!r}, [{item_str}])"

    @property
    def rules(self) -> List[Rule]:
        return []

    @property
    def tags(self) -> set[str]:
        return super().tags.union({'Line'})
