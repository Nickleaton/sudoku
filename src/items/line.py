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

    @property
    def name(self) -> str:
        return f"{self.__class__.__name__}_{self.identity}"

    @staticmethod
    def validate(board: Board, yaml: Any) -> List[str]:
        result = []
        if not isinstance(yaml, list):
            result.append(f"Expecting list, got {yaml!r}")
            return result
        for item in yaml:
            if not isinstance(item, list):
                result.append(f"Expecting list pair, got {item!r}")
                return result
            if len(item) != 2:
                result.append(f"Expecting pair, got {item!r}")
            if not isinstance(item[0], int):
                result.append(f"Expecting int, got {item[0]!r}")
            if not isinstance(item[1], int):
                result.append(f"Expecting int, got {item[1]!r}")
        if len(result) > 0:
            return result
        for item in yaml:
            if not board.is_valid(item[0], item[1]):
                result.append(f"Invalid row, column got {item!r}")
        return result

    @staticmethod
    def extract(board: Board, yaml: Any) -> List[Cell]:
        return [Cell.make(board, r, c) for r, c in yaml]

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
