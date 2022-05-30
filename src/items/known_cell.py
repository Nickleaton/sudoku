import re
from typing import List, Tuple, Dict

from src.glyphs.glyph import Glyph, KnownGlyph
from src.items.board import Board
from src.items.box import Box
from src.items.cell_reference import CellReference
from src.items.column import Column
from src.items.item import Item
from src.items.row import Row
from src.utils.coord import Coord


class KnownCell(CellReference):

    def __init__(self, board: Board, row: int, column: int, digit: int, prefix=None):
        super().__init__(board, row, column)
        self.digit = int(digit)
        self.prefix = "Known" if prefix is None else prefix

    @classmethod
    def extract(cls, board: Board, yaml: Dict) -> Tuple:
        regex = re.compile(f"([{board.digit_values}])([{board.digit_values}])=([{board.digit_values}]+)")
        match = regex.match(yaml[cls.__name__])
        assert match is not None
        row_str, column_string, digit_str = match.groups()
        return int(row_str), int(column_string), int(digit_str)

    @classmethod
    def create(cls, board: Board, yaml: Dict) -> Item:
        row, column, digit = KnownCell.extract(board, yaml)
        return cls(board, row, column, digit)

    def letter(self) -> str:
        return str(self.digit)

    @property
    def glyphs(self) -> List[Glyph]:
        return [KnownGlyph('Known', Coord(self.row, self.column), self.digit)]

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.board!r}, {self.cell!r}, {self.digit!r})"

    def to_dict(self) -> Dict:
        return {self.__class__.__name__: f"{self.row}{self.column}={self.digit}"}

    def css(self) -> Dict:
        return {
            ".Known": {
                'font-size': '70px',
                'fill': 'black',
                'font-weight': '500',
                'text-shadow': '-2px -2px 0 white, 2px -2px 0 white, -2px 2px 0 white, 2px 2px 0 white'
            },
            ".Unknown": {
                'font-size': '70px',
                'fill': 'blue',
                'font-weight': '500',
                'text-shadow': '-2px -2px 0 white, 2px -2px 0 white, -2px 2px 0 white, 2px 2px 0 white'
            },
            ".KnownForeground": {
                'font-size': '70px',
                'stroke': 'black',
                'fill': 'black'
            },
            ".KnownBackground": {
                'font-size': '70px',
                'stroke': 'white',
                'stroke-width': 8,
                'fill': 'white',
                'font-weight': 'bolder'
            },
            ".UnknownForeground": {
                'font-size': '70px',
                'stroke': 'blue',
                'fill': 'blue'
            },
            ".UnknownBackground": {
                'font-size': '70px',
                'stroke': 'white',
                'stroke-width': 8,
                'fill': 'white',
                'font-weight': 'bolder'
            }
        }

    def bookkeeping(self) -> None:
        self.cell.book.set_possible([self.digit])
        raw_regions = [region for region in self.cell.top.regions() if region.__class__ in [Box, Row, Column]]
        filtered_regions = [region for region in raw_regions if self.cell in region]
        for region in filtered_regions:
            for cell in region.cells:
                if cell == self.cell:
                    continue
                cell.book.set_impossible([self.digit])
