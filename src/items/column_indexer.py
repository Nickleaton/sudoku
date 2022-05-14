from typing import List

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

    def css(self) -> str:
        return (
            ".ColumnIndexer {\n"
            "    fill: pink;\n"
            "}\n"
        )

    def css2(self):
        return {
            '.ColumnIndexer': {
                'fill': 'pink'
            }
        }
