from typing import List, Dict

from src.glyphs.glyph import Glyph
from src.glyphs.rect_glyph import RectGlyph
from src.items.board import Board
from src.items.cell import Cell
from src.items.indexing import Indexer
from src.solvers.pulp_solver import PulpSolver
from src.utils.coord import Coord


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

    def css(self) -> Dict:
        return {
            '.RowIndexer': {
                'fill': 'pink'
            }
        }
