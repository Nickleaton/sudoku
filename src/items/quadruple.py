import re
from typing import List, Any, Dict, Callable

from pulp import lpSum

from src.glyphs.glyph import Glyph
from src.glyphs.quadruple_glyph import QuadrupleGlyph
from src.items.board import Board
from src.items.item import Item
from src.solvers.pulp_solver import PulpSolver
from src.utils.coord import Coord
from src.utils.rule import Rule


class Quadruple(Item):

    def __init__(self, board: Board, position: Coord, digits: str):
        super().__init__(board)
        self.position = position
        self.digits = digits
        self.numbers = "".join([str(d) for d in digits])

    def __repr__(self) -> str:
        digit_str = "".join([str(digit) for digit in self.digits])
        return f"{self.__class__.__name__}({self.board!r}, {self.position!r}, '{digit_str}')"

    @property
    def rules(self) -> List[Rule]:
        return [Rule('Quadruple', 3, 'Digits appearing in at last one of the cells adjacent to the circle')]

    def glyphs(self) -> List[Glyph]:
        return [
            QuadrupleGlyph(class_name="Quadruple", position=self.position, numbers=self.numbers)
        ]

    @classmethod
    def extract(cls, board: Board, yaml: Dict) -> Any:
        regex = re.compile(f"([{board.digit_values}])([{board.digit_values}])=([{board.digit_values}]+)")
        match = regex.match(yaml[cls.__name__])
        assert match is not None
        row_str, column_str, digits = match.groups()
        return Coord(int(row_str), int(column_str)), digits

    @classmethod
    def create(cls, board: Board, yaml: Dict) -> Item:
        position, numbers = Quadruple.extract(board, yaml)
        return cls(board, position, numbers)

    def add_constraint(self, solver: PulpSolver) -> None:
        offsets = [Coord(0, 0), Coord(0, 1), Coord(1, 0), Coord(1, 1)]
        for digit in self.digits:
            digit_sum = lpSum(
                [
                    solver.choices[int(digit)][(self.position + offset).row][(self.position + offset).column]
                    for offset in offsets
                ]
            )
            solver.model += digit_sum >= 1, f"{self.name}_{digit}"

    def to_dict(self) -> Dict:
        return {self.__class__.__name__: f"{self.position.row}{self.position.column}={''.join(self.digits)}"}

    def css(self) -> Dict:
        return {
            ".QuadrupleCircle": {
                "stroke-width": 2,
                "stroke": "black",
                "fill": "white"
            },
            ".QuadrupleText": {
                "stroke": "black",
                "fill": "black",
                "font-size": "30px"
            }
        }
