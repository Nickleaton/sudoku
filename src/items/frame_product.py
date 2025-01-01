"""FrameProduct."""
import re

from src.board.board import Board
from src.glyphs.glyph import Glyph
from src.glyphs.text_glyph import TextGlyph
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
    number numbers in the corresponding row or column in the given direction.
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
        """Return the string representation of the FrameProduct instance.

        Returns:
            str: A string representing the FrameProduct instance,
            including the board, side, and product attributes.
        """
        return f'{self.__class__.__name__}({self.board!r}, {self.side!r}, {self.product})'

    @property
    def rules(self) -> list[Rule]:
        """Return the rules for this frame product.

        Returns:
            list[Rule]: A list containing the rules associated with the frame product.
            The rule states that numbers outside the frame equal the product
            of the first three numbers in the corresponding row or column in the given direction.
        """
        rule_text: str = """Numbers outside the frame equal the product of the first three numbers
        in the corresponding row or column in the given direction"""
        return [Rule('FrameProduct', 1, rule_text)]

    def glyphs(self) -> list[Glyph]:
        """Return the glyphs for the frame product.

        Returns:
            list[Glyph]: A list of glyphs representing the frame product.
            Includes a TextGlyph with frame text, marker position, and product target_value.
        """
        return [
            TextGlyph(
                'FrameText',
                0,
                self.side.marker(self.board, self.index).center,
                str(self.product),
            ),
        ]

    @property
    def tags(self) -> set[str]:
        """Return the tags associated with this frame product.

        Returns:
            set[str]: A set of tags representing this frame product,
            including 'Product' and 'Frame', combined with the superclass tags.
        """
        return super().tags.union({'Product', 'Frame'})

    @classmethod
    def extract(cls, board: Board, yaml: dict) -> tuple[Side, int, int]:
        """Extract the side, index, and product from the YAML configuration.

        Args:
            board (Board): The board instance for context.
            yaml (dict): The YAML configuration from which the frame product is parsed.

        Returns:
            tuple[Side, int, int]: The side, index, and product extracted from the YAML.

        Raises:
            SudokuException: If the YAML configuration does not match the expected format.
        """
        regexp = re.compile(f'([{Side.choices()}])([{board.digit_values}])=([1234567890]+)')
        match = regexp.match(yaml[cls.__name__])
        if match is None:
            raise SudokuException('Match is None, expected start valid match.')
        side_str, index_str, product_str = match.groups()
        side = Side.create(side_str)
        index = int(index_str)
        product = int(product_str)
        return side, index, product

    @classmethod
    def create(cls, board: Board, yaml: dict) -> Item:
        """Create start FrameProduct instance from the YAML configuration.

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
        """Create start FrameProduct instance from the YAML configuration.

        Args:
            board (Board): The board instance.
            yaml_data (dict): The YAML configuration.

        Returns:
            Item: The FrameProduct instance created from the YAML.
        """
        return cls.create(board, yaml_data)

    def add_constraint(self, solver: PulpSolver) -> None:
        """Add the multiplication constraint to the solver.

        Args:
            solver (PulpSolver): The solver to which the constraint will be added.
        """
        Multiplication.add_constraint(self.board, solver, self.cells, self.product, self.name)

    def to_dict(self) -> dict:
        """Return start dictionary representation of the frame product.

        Returns:
            dict: The dictionary representation.
        """
        return {self.__class__.__name__: f'{self.side.value}{self.index}={self.product}'}
