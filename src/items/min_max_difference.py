""" Min Max Difference Sudoku """

import re
from typing import List, Any, Dict, Optional

from src.glyphs.glyph import Glyph, TextGlyph
from src.items.board import Board
from src.items.first_n import FirstN
from src.items.item import Item
from src.solvers.formulations import Formulations
from src.solvers.pulp_solver import PulpSolver
from src.utils.rule import Rule
from src.utils.side import Side


class MinMaxDifference(FirstN):
    """
    Handle frame sudoku:
        Numbers outside the frame equal the difference of the minimum and maximum values in the first three cells
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
                'MinMaxDifference',
                1,
                "Numbers outside the frame equal the difference of the minimum and maximum number in the "
                "corresponding row or column in the given direction"
            )
        ]

    def glyphs(self) -> List[Glyph]:
        return [
            TextGlyph(
                'MinMaxDiffenceText',
                0,
                self.side.marker(self.board, self.index).center,
                str(self.total)
            )
        ]

    @property
    def tags(self) -> set[str]:
        return super().tags.union({'Comparison', 'MinMaxDifference', 'Minimum', 'Maximum', 'Difference'})

    @classmethod
    def extract(cls, board: Board, yaml: Dict) -> Any:
        regexp = re.compile(f"([{Side.values()}])([{board.digit_values}])=([0-9]+)")
        match = regexp.match(yaml[cls.__name__])
        assert match is not None
        side_str, offset_str, total_str = match.groups()
        side = Side.create(side_str)
        offset = int(offset_str)
        total = int(total_str)
        return side, offset, total

    @classmethod
    def create(cls, board: Board, yaml: Dict) -> Item:
        side, index, total = MinMaxDifference.extract(board, yaml)
        return cls(board, side, index, total)

    def add_constraint(self, solver: PulpSolver, include: Optional[re.Pattern], exclude: Optional[re.Pattern]) -> None:
        xi = [solver.values[cell.row][cell.column] for cell in self.cells]
        mini = Formulations.minimum(solver.model, xi, 1, self.board.maximum_digit)
        maxi = Formulations.maximum(solver.model, xi, 1, self.board.maximum_digit)
        solver.model += Formulations.abs(solver.model, mini, maxi, self.board.maximum_digit) == self.total, self.name

    def to_dict(self) -> Dict:
        return {self.__class__.__name__: f"{self.side.value}{self.index}={self.total}"}

    def css(self) -> Dict:
        return {
            ".MinMaxDifferenceTextForeground": {
                "fill": "black",
                "font-size": "30px",
                "stroke": "black",
                "stroke-width": 1
            },
            ".MinMaxDifferenceTextBackground": {
                "fill": "white",
                "font-size": "30px",
                "font-weight": "bolder",
                "stroke": "white",
                "stroke-width": 8
            }
        }
