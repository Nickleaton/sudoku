from typing import List, Sequence, Any

from src.items.board import Board
from src.items.cell import Cell
from src.items.item import Item, YAML
from src.items.region import Region
from src.utils.rule import Rule


class Line(Region):

    def __init__(self, board: Board, cells: Sequence[Cell]):
        super().__init__(board)
        self.add_items(cells)

    @staticmethod
    def validate(board: Board, yaml: Any) -> List[str]:
        result = []
        return result

    @staticmethod
    def extract(board: Board, yaml: Any) -> List[Cell]:
        return [Cell.make(board, int(part.strip()[0]), int(part.strip()[0])) for part in yaml.split(',')]

    @classmethod
    def create(cls, name: str, board: Board, yaml: YAML) -> Item:
        Line.validate(board, yaml)
        cells = Line.extract(board, yaml)
        return cls(board, cells)

    def __repr__(self) -> str:
        cell_str = ", ".join(repr(cell) for cell in self.cells)
        return f"{self.__class__.__name__}({self.board!r}, [{cell_str}])"

    @property
    def rules(self) -> List[Rule]:
        return []

    @property
    def tags(self) -> set[str]:
        return super().tags.union({'Line'})
