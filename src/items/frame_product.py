""" Frame Sudoku """

import re
from typing import List, Any, Dict

from src.glyphs.glyph import Glyph, TextGlyph
from src.items.board import Board
from src.items.first_n import FirstN
from src.items.item import Item
from src.items.multiplication import Multiplication
from src.solvers.pulp_solver import PulpSolver
from src.utils.rule import Rule
from src.utils.side import Side


class FrameProduct(FirstN):
    """
    Handle frame sudoku:
        Numbers outside the frame equal the product first three numbers in the
        corresponding row or column in the given direction
    """

    def __init__(self, board: Board, side: Side, index: int, product: int):
        """
        Construct
        :param board: board being used
        :param side: the side where the total is to go
        :param index: the row or column of the total
        :param product: the actual product
        """
        super().__init__(board, side, index)
        self.product = product

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
            f"{self.product}"
            f")"
        )

    @property
    def rules(self) -> List[Rule]:
        return [
            Rule(
                'FrameProduct',
                1,
                "Numbers outside the frame equal the product of the first three numbers in the "
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
                str(self.product)
            )
        ]

    @property
    def tags(self) -> set[str]:
        return super().tags.union({'Product', 'Frame'})

    @classmethod
    def extract(cls, board: Board, yaml: Dict) -> Any:
        data = yaml[cls.__name__]
        ref_str: str = data.split("=")[0]
        total_str: str = data.split("=")[1]
        side = Side.create(ref_str[0])
        index = int(ref_str[1])
        product = int(total_str)
        return side, index, product

    @classmethod
    def create(cls, board: Board, yaml: Dict) -> Item:
        side, index, product = FrameProduct.extract(board, yaml)
        return cls(board, side, index, product)

    def add_constraint(self, solver: PulpSolver, include: re.Pattern, exclude: re.Pattern) -> None:
        Multiplication.add_constraint(self.board, solver, self.cells, self.product, self.name)

    def to_dict(self) -> Dict:
        return {self.__class__.__name__: f"{self.side.value}{self.index}={self.product}"}
