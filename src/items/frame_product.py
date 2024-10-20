""" Frame Sudoku """

import re
from typing import List, Any, Dict, Callable

from src.glyphs.glyph import Glyph
from src.glyphs.text_glyph import TextGlyph
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
        regexp = re.compile(f"([{Side.values()}])([{board.digit_values}])=([1234567890]+)")
        match = regexp.match(yaml[cls.__name__])
        assert match is not None
        side_str, index_str, product_str = match.groups()
        side = Side.create(side_str)
        index = int(index_str)
        product = int(product_str)
        return side, index, product

    @classmethod
    def create(cls, board: Board, yaml: Dict) -> Item:
        side, index, product = FrameProduct.extract(board, yaml)
        return cls(board, side, index, product)

    def add_constraint(self, solver: PulpSolver) -> None:
        Multiplication.add_constraint(self.board, solver, self.cells, self.product, self.name)

    def to_dict(self) -> Dict:
        return {self.__class__.__name__: f"{self.side.value}{self.index}={self.product}"}
