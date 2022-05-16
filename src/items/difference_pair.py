from typing import List, Tuple, Dict

from src.items.board import Board
from src.items.cell import Cell
from src.items.item import Item
from src.items.pair import Pair
from src.utils.rule import Rule


class DifferencePair(Pair):

    def __init__(self, board: Board, cell_1: Cell, cell_2: Cell, difference: int):
        super().__init__(board, cell_1, cell_2)
        self.difference = difference

    @classmethod
    def extract(cls, board: Board, yaml: Dict) -> Tuple:
        cell_string, data_string = yaml[cls.__name__].split('=')
        cell_string_1, cell_string_2 = cell_string.split("-")
        cell_1 = Cell.make(board, int(cell_string_1[0]), int(cell_string_1[1]))
        cell_2 = Cell.make(board, int(cell_string_2[0]), int(cell_string_2[1]))
        return cell_1, cell_2, int(data_string)

    @classmethod
    def create(cls, board: Board, yaml: Dict) -> Item:
        cell_1, cell_2, difference = cls.extract(board, yaml)
        return cls(board, cell_1, cell_2, difference)

    @property
    def rules(self) -> List[Rule]:
        return []

    @property
    def tags(self) -> set[str]:
        return super().tags.union({'Difference'})

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.board!r}, {self.cell_1!r}, {self.cell_2!r}, {self.difference!r})"

    def to_dict(self) -> Dict:
        return {
            self.__class__.__name__: (
                f"{self.cell_1.row_column_string}"
                f"-"
                f"{self.cell_2.row_column_string}"
                f"="
                f"{self.difference}"
            )
        }
