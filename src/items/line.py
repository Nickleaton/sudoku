from typing import List, Dict, Sequence, Any

from src.items.board import Board
from src.items.cell import Cell
from src.items.item import Item
from src.items.region import Region
from src.utils.rule import Rule


class Line(Region):

    def __init__(self, board: Board, cells: Sequence[Cell]):
        super().__init__(board)
        self.add_items(cells)

    @property
    def name(self) -> str:
        return f"{self.__class__.__name__}_{self.cells[0].row}_{self.cells[0].column}"

    @staticmethod
    def validate(yaml: Any) -> List[str]:
        result = []
        if not isinstance(yaml, list):
            result.append(f"Expecting list, got {yaml:r}")
            return result
        for item in yaml:
            if not isinstance(item, list):
                result.append(f"Expecting list pair, got {item:r}")
            else:
                if len(item) != 2:
                    result.append(f"Expecting pair, got {item:r}")
        return result

    @staticmethod
    def extract(board: Board, yaml: Any) -> List[Cell]:
        return [Cell.make(board, r, c) for r, c in yaml]

    @classmethod
    def create(cls, name: str, board: Board, yaml: Dict | List | str | int | None) -> Item:
        Line.validate(yaml)
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
