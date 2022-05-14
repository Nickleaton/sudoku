from typing import List, Tuple, Dict

from src.glyphs.glyph import Glyph, KnownGlyph
from src.items.board import Board
from src.items.cell_reference import CellReference
from src.items.item import Item
from src.solvers.pulp_solver import PulpSolver
from src.utils.coord import Coord


class KnownCell(CellReference):

    def __init__(self, board: Board, row: int, column: int, digit: int):
        super().__init__(board, row, column)
        self.digit = int(digit)

    @classmethod
    def extract(cls, board: Board, yaml: Dict) -> Tuple:
        row_column, digit = yaml[cls.__name__].split("=")
        return int(row_column[0]), int(row_column[1]), int(digit)

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

    def add_constraint(self, solver: PulpSolver) -> None:
        for digit in self.board.digit_range:
            target = 1 if digit == self.digit else 0
            name = f"Known_{self.row}_{self.column}_eq_{digit}"
            solver.model += solver.choices[digit][self.row][self.column] == target, name

    def css(self) -> str:
        return (
            ".Known {\n"
            "    font-size: 70px;\n"
            "    fill: black;\n"
            "    font-weight: 500;\n"
            "    text-shadow: -2px -2px 0 white, 2px -2px 0 white, -2px 2px 0 white, 2px 2px 0 white;\n"
            "}\n"
            ".Unknown {\n"
            "    font-size: 70px;\n"
            "    fill: blue;\n"
            "    font-weight: 500;\n"
            "    text-shadow: -2px -2px 0 white, 2px -2px 0 white, -2px 2px 0 white, 2px 2px 0 white;\n"
            "}\n"
            ".KnownForeground {\n"
            "    font-size: 70px;\n"
            "    stroke: black;\n"
            "    fill: black\n"
            "}\n"
            ".KnownBackground {\n"
            "    font-size: 70px;\n"
            "    stroke: white;\n"
            "    stroke-width: 8;\n"
            "    fill: white;\n"
            "    font-weight: bolder\n"
            "}\n"
            ".UnknownForeground {\n"
            "    font-size: 70px;\n"
            "    stroke: blue;\n"
            "    fill: blue\n"
            "}\n"
            ".UnknownBackground {\n"
            "    font-size: 70px;\n"
            "    stroke: white;\n"
            "    stroke-width: 8;\n"
            "    fill: white;\n"
            "    font-weight: bolder\n"
            "}\n"
        )
    
    def css2(self):
        return {
            ".Known" :{
                'font-size': '70px',
                'fill': 'black',
                'font-weight':'500',
                'text-shadow': '-2px -2px 0 white, 2px -2px 0 white, -2px 2px 0 white, 2px 2px 0 white'
            },
            ".Unknown":{
                'font-size': '70px',
                'fill': 'blue',
                'font-weight': '500',
                'text-shadow': '-2px -2px 0 white, 2px -2px 0 white, -2px 2px 0 white, 2px 2px 0 white'
            },
            ".KnownForeground" :{
                'font-size': '70px',
                'stroke': 'black',
                'fill': 'black'
            },
            ".KnownBackground" :{
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