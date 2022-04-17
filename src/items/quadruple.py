from typing import List, Dict

from pulp import lpSum

from src.glyphs.glyph import Glyph, QuadrupleGlyph
from src.items.board import Board
from src.items.constraint_exception import ConstraintException
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

    @property
    def name(self) -> str:
        return f"{self.__class__.__name__}_{self.position.row}_{self.position.column}"

    def __repr__(self) -> str:
        digit_str = "".join([str(digit) for digit in self.digits])
        return f"{self.__class__.__name__}({self.board!r}, {self.position!r}, '{digit_str}')"

    @property
    def rules(self) -> List[Rule]:
        return [Rule('Quadruple', 3, 'Digits appearing in at last one of the cells adjacent to the circle')]

    @property
    def glyphs(self) -> List[Glyph]:
        return [
            QuadrupleGlyph(class_name="Quadruple", position=self.position, numbers=self.numbers)
        ]

    @classmethod
    def create(cls, name: str, board: Board, yaml: Dict | List | str | int | None) -> Item:
        if not isinstance(yaml, str):
            raise ConstraintException(f"Expecting str, got {yaml!r}")
        position_str, numbers = yaml.split("=")
        position = Coord(int(position_str[0]), int(position_str[1]))
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
