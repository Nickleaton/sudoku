""" Frame Sudoku """

from typing import List, Dict, Any

from pulp import lpSum

from src.glyphs.glyph import Glyph, TextGlyph
from src.items.board import Board
from src.items.cell import Cell
from src.items.item import Item
from src.solvers.pulp_solver import PulpSolver
from src.utils.order import Order
from src.utils.rule import Rule
from src.utils.side import Side


class Frame(Item):
    """
    Handle frame sudoku:
        Numbers outside the frame equal the sum of the first three numbers in the
        corresponding row or column in the given direction
    """

    def __init__(self, board: Board, side: Side, index: int, total: int):
        """
        Construct
        :param board: board being used
        :param side: the side where the total is to go
        :param index: the row or column of the total
        :param total: the actual total
        """
        super().__init__(board)
        self.side = side
        self.index = index
        self.total = total
        self.direction = self.side.order_direction(Order.INCREASING)
        self.offset = self.side.order_offset()
        self.coords = []
        self.coords.append(self.side.start_cell(self.board, self.index))
        self.coords.append(self.coords[0] + self.offset)
        self.coords.append(self.coords[1] + self.offset)
        self.cells = [Cell.make(self.board, int(coord.row), int(coord.column)) for coord in self.coords]

    @property
    def name(self) -> str:
        """
        Name of the frame
        :return: string
        """
        return f"{self.__class__.__name__}_{self.side.name}_{self.index}"

    def __repr__(self) -> str:
        """
        representation of the frame
        :return: str
        """
        return (
            f"{self.__class__.__name__}"
            f"("
            f"{self.board!r}, "
            f"{self.side!r}, "
            f"{self.total}"
            f")"
        )

    @property
    def rules(self) -> List[Rule]:
        return [
            Rule(
                'Frame',
                1,
                "Numbers outside the frame equal the sum of the first three numbers in the "
                "corresponding row or column in the given direction"
            )
        ]

    @property
    def glyphs(self) -> List[Glyph]:
        return [
            TextGlyph(
                'FrameText',
                0,
                self.side.marker(self.board, self.index).center,
                str(self.total)
            )
        ]

    @property
    def tags(self) -> set[str]:
        return super().tags.union({'Comparison', 'Frame'})

    @staticmethod
    def validate(board: Board, yaml: Any) -> List[str]:
        if not isinstance(yaml, str):
            return [f"Expected str, got {yaml!r}"]
        if len(yaml) <= 4:
            return [f"Expected side|index|total, got {yaml!r}"]
        result = []
        if not Side.valid(yaml[0]):
            result.append(f"Side not valid {yaml[0]}")
        if not yaml[1].isdigit():
            result.append(f"Index not valid {yaml[1]}")
            return result
        index = int(yaml[1])
        if index not in board.row_range or index not in board.row_range:
            result.append(f"Index outside range {index}")
        if not yaml[3:].isnumeric():
            result.append(f"Invalid total {yaml[3:]}")
        return result

    @staticmethod
    def extract(board: Board, yaml: Any) -> Any:
        side = Side.create(yaml[0])
        index = int(yaml[1])
        total = int(yaml[3:])
        return side, index, total

    @classmethod
    def create(cls, name: str, board: Board, yaml: Dict | List | str | int | None) -> 'Frame':
        Frame.validate(board, yaml)
        side, index, total = Frame.extract(board, yaml)
        return cls(board, side, index, total)

    def add_constraint(self, solver: PulpSolver) -> None:
        values = [
            solver.values[self.cells[0].row][self.cells[0].column],
            solver.values[self.cells[1].row][self.cells[1].column],
            solver.values[self.cells[2].row][self.cells[2].column]
        ]
        solver.model += lpSum(values) == self.total, f"{self.name}"
