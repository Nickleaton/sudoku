import re
from typing import Dict, Tuple, List, Set, Type

from src.glyphs.glyph import Glyph, TextGlyph
from src.items.board import Board
from src.items.item import Item
from src.utils.coord import Coord
from src.utils.rule import Rule
from src.utils.side import Side


class Sandwich(Item):

    def __init__(self, board: Board, side: Side, index: int, total: int):
        super().__init__(board)
        self.side = side
        self.index = index
        self.total = total
        self.position = side.marker(board, self.index) + Coord(0.5, 0.5)

    @classmethod
    def extract(cls, board: Board, yaml: Dict) -> Tuple:
        regexp = re.compile(f"([{Side.values()}])([{board.digit_values}])=([0-9]+)")
        side_str, offset_str, total_str = regexp.match(yaml[cls.__name__]).groups()
        side = Side.create(side_str)
        offset = int(offset_str)
        total = int(total_str)
        return side, offset, total

    @classmethod
    def create(cls, board: Board, yaml: Dict) -> Item:
        side, offset, total = cls.extract(board, yaml)
        return cls(board, side, offset, total)

    @property
    def glyphs(self) -> List[Glyph]:
        return [
            TextGlyph('Sandwich', 0, self.position, str(self.total)),
        ]

    @property
    def rules(self) -> List[Rule]:
        return [
            Rule(
                'Sandwich',
                1,
                (
                    'Clues outside of the grid give the sum of the digits sandwiched between the 1 and the 9 '
                    'in that row/column '
                )
            )
        ]

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.board!r}, {self.side!r}, {self.index}, {self.total})"

    @property
    def used_classes(self) -> Set[Type['Item']]:
        result = super().used_classes
        result = result.union([self.__class__])
        return result

    def to_dict(self) -> Dict:
        return {self.__class__.__name__: f"{self.side.value}{self.index}={self.total}"}

    def css(self) -> Dict:
        return {
            ".SandwichForeground": {
                "font-size": "30px",
                "stroke": "black",
                "stroke-width": 1,
                "fill": "black"
            },
            ".SandwichBackground": {
                "font-size": "30px",
                "stroke": "white",
                "stroke-width": 8,
                "fill": "white",
                "font-weight": "bolder"
            }
        }
