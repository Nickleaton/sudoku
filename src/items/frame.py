""" Frame Sudoku """

from typing import List, Dict, Any

from src.glyphs.glyph import Glyph, TextGlyph
from src.items.board import Board
from src.items.first_n import FirstN
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

    @staticmethod
    def validate(board: Board, yaml: Any) -> List[str]:
        if not isinstance(yaml, str):
            return [f"Expected str, got {yaml!r}"]
        if "=" not in yaml:
            return [f"Expecting {{sidr}}{{index}}={{order}}, got {yaml!r}"]
        ref_str: str = yaml.split("=")[0]
        total_str: str = yaml.split("=")[1]
        result = FirstN.validate(board, ref_str)
        if len(result) > 0:
            return result
        if not total_str.isnumeric():
            result.append(f"Invalid total {total_str}")
        return result

    @staticmethod
    def extract(board: Board, yaml: Any) -> Any:
        ref_str: str = yaml.split("=")[0]
        total_str: str = yaml.split("=")[1]
        side, index = FirstN.extract(board, ref_str)
        total = int(total_str)
        return side, index, total

    @classmethod
    def create(cls, name: str, board: Board, yaml: Dict | List | str | int | None) -> 'Frame':
        Frame.validate(board, yaml)
        side, index, total = Frame.extract(board, yaml)
        return cls(board, side, index, total)

    def add_constraint(self, solver: PulpSolver) -> None:
        self.add_total_constraint(solver, self.total)
