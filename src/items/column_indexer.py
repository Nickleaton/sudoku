from typing import List, Any

from src.glyphs.glyph import Glyph, RectGlyph
from src.items.board import Board
from src.items.cell import Cell
from src.items.indexing import Indexer
from src.solvers.pulp_solver import PulpSolver
from src.utils.coord import Coord


class ColumnIndexer(Indexer):

    def __init__(self, board: Board, index: int):
        super().__init__(board, index)
        self.add_items([Cell.make(board, row, index) for row in board.row_range])

    @staticmethod
    def validate(board: Board, yaml: Any) -> List[str]:
        error = f"Expecting ColumnIndexer: index, got {yaml!r}"
        if not isinstance(yaml, dict):
            return [error]
        if len(yaml) != 1:
            return [error]
        for k, v in yaml.items():
            if k != 'ColumnIndexer':
                return [error]
            if not isinstance(v, int):
                return [error]
            if v not in board.row_range:
                return [error]
        return []

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
