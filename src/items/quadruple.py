from typing import List, Any

from pulp import lpSum

from src.glyphs.glyph import Glyph, QuadrupleGlyph
from src.items.board import Board
from src.items.item import Item, YAML
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

    @staticmethod
    def validate(board: Board, yaml: Any) -> List[str]:
        if not isinstance(yaml, str):
            return [f"Expecting str, got {yaml!r}"]
        results: List[str] = []
        if "=" not in yaml:
            return [f"Expecting position=digits, got {yaml}"]
        position_str: str = yaml.split("=")[0]
        digits: str = yaml.split("=")[1]
        if len(position_str) != 2:
            results.append(f"Expecting rc for position got {position_str}")
            return results
        if not position_str.isnumeric():
            results.append(f"Expecting rc for position got {position_str}")
            return results
        row = int(position_str[0])
        if row not in board.row_range:
            results.append(f"Expected valid row, got {row} ")
        column = int(position_str[1])
        if column not in board.column_range:
            results.append(f"Expected valid column, got {column} ")
        if len(digits) > 4:
            results.append(f"Too many digits, got {digits}")
        if len(digits) == 0:
            results.append(f"Too few digits, got '{digits}'")
        if not digits.isnumeric():
            results.append(f"Expecting numbers, got '{digits}'")
        if len(results) > 0:
            return results
        for d in digits:
            if int(d) not in board.digit_range:
                results.append(f"Invalid digit {d}")
        return results

    @staticmethod
    def extract(board: Board, yaml: Any) -> Any:
        position_str, digits = yaml.split("=")
        position = Coord(int(position_str[0]), int(position_str[1]))
        return position, digits

    @classmethod
    def create(cls, name: str, board: Board, yaml: YAML) -> Item:
        Quadruple.validate(board, yaml)
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
