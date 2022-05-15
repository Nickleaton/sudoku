""" Frame Sudoku """

from typing import List, Any, Dict

from src.glyphs.glyph import Glyph, TextGlyph
from src.items.board import Board
from src.items.first_n import FirstN
from src.items.item import Item
from src.solvers.pulp_solver import PulpSolver
from src.utils.rule import Rule
from src.utils.side import Side


class Frame(FirstN):
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
        super().__init__(board, side, index)
        self.total = total

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

    @classmethod
    def extract(cls, board: Board, yaml: Dict) -> Any:
        data = yaml[cls.__name__]
        ref_str: str = data.split("=")[0]
        total_str: str = data.split("=")[1]
        side = Side.create(ref_str[0])
        index = int(ref_str[1])
        total = int(total_str)
        return side, index, total

    @classmethod
    def create(cls, board: Board, yaml: Dict) -> Item:
        side, index, total = Frame.extract(board, yaml)
        return cls(board, side, index, total)

    def add_constraint(self, solver: PulpSolver) -> None:
        self.add_total_constraint(solver, self.total)

    def to_dict(self) -> Dict:
        return {self.__class__.__name__: f"{self.side.value}{self.index}={self.total}"}

    def css(self) -> Dict:
        return {
            ".FrameTextForeground":
                {
                    "font-size": "30px",
                    "stroke": "black",
                    "stroke-width": 1,
                    "fill": "black"
                },
            ".FrameTextBackground": {
                "font-size": "30px",
                "stroke": "white",
                "stroke-width": 8,
                "fill": "white",
                "font-weight": "bolder"
            }
        }
