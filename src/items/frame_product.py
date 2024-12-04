"""FrameProduct."""

import re
from typing import Any

from src.glyphs.glyph import Glyph
from src.glyphs.text_glyph import TextGlyph
from src.items.board import Board
from src.items.first_n import FirstN
from src.items.item import Item
from src.items.multiplication import Multiplication
from src.solvers.pulp_solver import PulpSolver
from src.utils.rule import Rule
from src.utils.side import Side
from src.utils.sudoku_exception import SudokuException


class FrameProduct(FirstN):
    """Handle frame sudoku.

    Numbers outside the frame equal the product of the first
    n numbers in the corresponding row or column in the given direction.
    """

    def __init__(self, board: Board, side: Side, index: int, product: int):
        """Initialize the FrameProduct instance.

        Args:
            board (Board): The Sudoku board being used.
            side (Side): The side where the product constraint applies.
            index (int): The index of the row or column.
            product (int): The product to be applied outside the frame.
        """
        super().__init__(board, side, index)
        self.product = product

    def __repr__(self) -> str:
        """Return a string representation of the FrameProduct instance."""
        return f"{self.__class__.__name__}({self.board!r}, {self.side!r}, {self.product})"

    @property
    def rules(self) -> list[Rule]:
        """Return the rule for this frame product."""
        return [
            Rule(
                'FrameProduct',
                1,
                "Numbers outside the frame equal the product of the first three numbers in the "
                "corresponding row or column in the given direction"
            )
        ]

    def glyphs(self) -> list[Glyph]:
        """Return the glyphs for the frame product."""
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
        """Return the tags associated with this frame product."""
        return super().tags.union({'Product', 'Frame'})

    @classmethod
    def extract(cls, board: Board, yaml: dict) -> Any:
        """Extract the side, index, and product from the YAML configuration.

        Args:
            board (Board): The board instance for context.
            yaml (dict): The YAML configuration from which the frame product is parsed.

        Returns:
            tuple[Side, int, int]: The side, index, and product extracted from the YAML.
        """
        regexp = re.compile(f"([{Side.values()}])([{board.digit_values}])=([1234567890]+)")
        match = regexp.match(yaml[cls.__name__])
        if match is None:
            raise SudokuException("Match is None, expected a valid match.")
        side_str, index_str, product_str = match.groups()
        side = Side.create(side_str)
        index = int(index_str)
        product = int(product_str)
        return side, index, product

    @classmethod
    def create(cls, board: Board, yaml: dict) -> Item:
        """Create a FrameProduct instance from the YAML configuration.

        Args:
            board (Board): The board instance.
            yaml (dict): The YAML configuration.

        Returns:
            Item: The FrameProduct instance created from the YAML.
        """
        side, index, product = FrameProduct.extract(board, yaml)
        return cls(board, side, index, product)

    @classmethod
    def create2(cls, board: Board, yaml_data: dict) -> Item:
        return cls.create(board, yaml_data)

    def add_constraint(self, solver: PulpSolver) -> None:
        """Add the multiplication constraint to the solver.

        Args:
            solver (PulpSolver): The solver to which the constraint will be added.
        """
        Multiplication.add_constraint(self.board, solver, self.cells, self.product, self.name)

    def to_dict(self) -> dict:
        """Return a dictionary representation of the frame product.

        Returns:
            dict: The dictionary representation.
        """
        return {self.__class__.__name__: f"{self.side.value}{self.index}={self.product}"}
