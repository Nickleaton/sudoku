from typing import Dict, List

from src.glyphs.glyph import Glyph, RectGlyph
from src.items.board import Board
from src.items.cell import Cell
from src.items.item import Item
from src.items.region import StandardRegion
from src.solvers.pulp_solver import PulpSolver
from src.utils.coord import Coord
from src.utils.rule import Rule


class Indexer(StandardRegion):

    @property
    def name(self) -> str:
        return f"{self.__class__.__name__}_{self.index}"

    @classmethod
    def create(cls, name: str, board: Board, yaml: Dict | List | str | int | None) -> Item:
        Item.check_yaml_int(yaml)
        index = yaml
        return cls(board, index)

    @staticmethod
    def variant() -> str:
        return ""

    @staticmethod
    def other_variant() -> str:
        return ""

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.board!r}, {self.index!r})"

    @property
    def rules(self) -> List[Rule]:
        return [
            Rule(
                f'{self.__class__.__name__}{self.index}',
                1,
                (
                    f"Digits in {self.variant()} {self.index} indicate the {self.variant()} "
                    f"in which the digit {self.index} appears in that {self.other_variant()}"
                )
            )
        ]

    @property
    def tags(self) -> set[str]:
        return super().tags.union({'Indexing'})


class ColumnIndexer(Indexer):

    def __init__(self, board: Board, index: int):
        super().__init__(board, index)
        self.add_items([Cell.make(board, row, index) for row in board.row_range])

    @staticmethod
    def variant() -> str:
        return "column"

    @staticmethod
    def other_variant() -> str:
        return "row"

    @property
    def glyphs(self) -> List[Glyph]:
        return [RectGlyph('ColumnIndexer', Coord(1, self.index), Coord(self.board.board_columns, 1))]

    def add_constraint(self, solver: PulpSolver) -> None:
        for cell in self.cells:
            for digit in solver.board.digit_range:
                indexer = solver.choices[digit][cell.row][cell.column]
                indexed = solver.choices[cell.column][cell.row][digit]
                solver.model += indexer == indexed, f"{self.name}_{cell.row}_{cell.column}_{digit}"


class RowIndexer(Indexer):

    def __init__(self, board: Board, index: int):
        super().__init__(board, index)
        self.add_items([Cell.make(board, column, index) for column in board.column_range])

    @staticmethod
    def variant() -> str:
        return "row"

    @staticmethod
    def other_variant() -> str:
        return "column"

    @property
    def glyphs(self) -> List[Glyph]:
        return [RectGlyph('RowIndexer', Coord(self.index, 1), Coord(1, self.board.board_rows))]

    @property
    def tags(self) -> set[str]:
        return super().tags.union({'Indexing'})

    def add_constraint(self, solver: PulpSolver) -> None:
        for cell in self.cells:
            for digit in solver.board.digit_range:
                indexer = solver.choices[digit][cell.row][cell.column]
                indexed = solver.choices[cell.row][digit][cell.column]
                solver.model += indexer == indexed, f"{self.name}_{cell.row}_{cell.column}_{digit}"
