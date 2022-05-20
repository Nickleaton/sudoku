import re
from typing import Dict, Tuple, List, Set, Type

from src.glyphs.glyph import Glyph, TextGlyph
from src.items.board import Board
from src.items.item import Item
from src.solvers.pulp_solver import PulpSolver
from src.utils.coord import Coord
from src.utils.cyclic import Cyclic
from src.utils.rule import Rule
from src.utils.side import Side


class NumberedRoom(Item):

    def __init__(self, board: Board, side: Side, index: int, digit: int):
        super().__init__(board)
        self.side = side
        self.index = index
        self.digit = digit
        self.direction = side.direction(Cyclic.CLOCKWISE)
        self.start_cell = side.start_cell(board, self.index)
        self.reference = self.start_cell - self.direction.offset + Coord(0.5, 0.5)

    @classmethod
    def extract(cls, board: Board, yaml: Dict) -> Tuple:
        parts = yaml[cls.__name__].split("=")
        side = Side.create(parts[0][0])
        offset = int(parts[0][1])
        digit = int(parts[1])
        return side, offset, digit

    @classmethod
    def create(cls, board: Board, yaml: Dict) -> Item:
        side, offset, digit = cls.extract(board, yaml)
        return cls(board, side, offset, digit)

    @property
    def glyphs(self) -> List[Glyph]:
        return [
            TextGlyph('NumberedRoom', 0, self.reference, str(self.digit)),
        ]

    @property
    def rules(self) -> List[Rule]:
        return [
            Rule(
                'NumberedRoom',
                1,
                (
                    'Clues outside of the grid equal the Xth digit in their row/column '
                    'seen from the side of the clue, with X being the first digit in their '
                    'row/column seen from the side of the clue'
                )
            )
        ]

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.board!r}, {self.side!r}, {self.index}, {self.digit})"

    @property
    def used_classes(self) -> Set[Type['Item']]:
        result = super().used_classes
        result = result.union([self.__class__])
        return result

    def to_dict(self) -> Dict:
        return {self.__class__.__name__: f"{self.side.value}{self.index}={self.digit}"}

    def add_constraint(self, solver: PulpSolver, include: re.Pattern, exclude: re.Pattern) -> None:
        if self.side == Side.LEFT:
            for d in self.board.digit_range:
                first = solver.choices[d][self.start_cell.row][self.start_cell.column]
                xth = solver.choices[self.digit][self.start_cell.row][d]
                solver.model += first == xth, f"{self.name}_{d}"
        elif self.side == Side.RIGHT:
            for d in self.board.digit_range:
                first = solver.choices[d][self.start_cell.row][self.start_cell.column]
                xth = solver.choices[self.digit][self.start_cell.row][self.board.board_columns - d + 1]
                solver.model += first == xth, f"{self.name}_{d}"
        elif self.side == Side.TOP:
            for d in self.board.digit_range:
                first = solver.choices[d][self.start_cell.row][self.start_cell.column]
                xth = solver.choices[self.digit][d][self.start_cell.column]
                solver.model += first == xth, f"{self.name}_{d}"
        elif self.side == Side.BOTTOM:
            for d in self.board.digit_range:
                first = solver.choices[d][self.start_cell.row][self.start_cell.column]
                xth = solver.choices[self.digit][self.board.board_rows - d + 1][self.start_cell.column]
                solver.model += first == xth, f"{self.name}_{d}"
        else:  # pragma: no cover
            raise Exception(f"Unexpected Side {self.side.name}")

    def css(self) -> Dict:
        return {
            '.NumberedRoomForeground': {
                'font-size': '30px',
                'stroke': 'black',
                'stroke-width': 1,
                'fill': 'black'
            },
            '.NumberedRoomBackground': {
                'font-size': '30px',
                'stroke': 'white',
                'stroke-width': 8,
                'fill': 'white',
                'font-weight': 'bolder'
            }
        }
