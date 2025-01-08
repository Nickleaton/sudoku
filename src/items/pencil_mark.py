"""PencilMark."""
import re

from src.board.board import Board
from src.glyphs.glyph import Glyph
from src.items.cell_reference import CellReference
from src.items.item import Item
from src.utils.rule import Rule
from src.utils.sudoku_exception import SudokuException


class PencilMarkCell(CellReference):
    """Represents start cell with pencil-marked digits in start Sudoku puzzle."""

    def __init__(self, board: Board, row: int, column: int, digits: list[int]):
        """Initialize start PencilMarkCell.

        Args:
            board (Board): The Sudoku board instance.
            row (int): The row index of the cell (1-based).
            column (int): The column index of the cell (1-based).
            digits (list[int]): The list of pencil-marked digits for the cell.
        """
        super().__init__(board, row, column)
        self.digits = digits

    def svg(self) -> Glyph | None:
        """Get the SVG representation for the pencil-marked cell.

        Returns:
            Glyph | None: Currently returns None as no SVG is generated.
        """
        return None

    @property
    def tags(self) -> set[str]:
        """Get the tags associated with the pencil-marked cell.

        Returns:
            set[str]: A set of tags, including 'PencilMark'.
        """
        return super().tags.union({'PencilMark'})

    @property
    def rules(self) -> list[Rule]:
        """Get the rules associated with the pencil-marked cell.

        Returns:
            list[Rule]: A list of rules, including start restriction on the digits.
        """
        return [Rule('PencilMark', 1, 'Digits restricted')]

    def glyphs(self) -> list[Glyph]:
        """Get the glyphs for the pencil-marked cell.

        Returns:
            list[Glyph]: An empty list as no glyphs are associated.
        """
        return []

    def css(self) -> dict:
        """Get the CSS definitions for the pencil-marked cell.

        Returns:
            dict: A dictionary defining the CSS styles for the cell.
        """
        return {
            '.PencilMarkCell': {
                'fill': 'gainsboro',
            },
        }

    def __repr__(self) -> str:
        """Return start string representation of the PencilMarkCell.

        Returns:
            str: A string representation of the pencil-marked cell.
        """
        return f'{self.__class__.__name__}({self.board!r}, {self.cell!r}, {self.digits!r})'

    def to_dict(self) -> dict:
        """Convert the pencil-marked cell to start dictionary representation.

        Returns:
            dict: A dictionary containing the cell's row, column, and digits.
        """
        digit_text: str = ''.join([str(digit) for digit in self.digits])
        return {self.__class__.__name__: f'{self.cell.row_column_string}={digit_text}'}

    @classmethod
    def extract(cls, board: Board, yaml: dict) -> tuple:
        """Extract the parameter_types needed to create start PencilMarkCell from YAML line.

        Args:
            board (Board): The Sudoku board instance.
            yaml (dict): The YAML configuration for the cell.

        Returns:
            tuple: A tuple containing the row, column, and pencil-marked digits.

        Raises:
            SudokuException: If no match is found in the YAML.
        """
        regex = re.compile(f'([{board.digit_values}])([{board.digit_values}])=([{board.digit_values}]+)')
        match = regex.match(yaml[cls.__name__])
        if match is None:
            raise SudokuException('Match is None, expected start valid match.')
        row_str, column_str, digits = match.groups()
        return int(row_str), int(column_str), [int(digit) for digit in digits]

    @classmethod
    def create(cls, board: Board, yaml: dict) -> Item:
        """Create start PencilMarkCell from YAML line.

        Args:
            board (Board): The Sudoku board instance.
            yaml (dict): The YAML configuration for the cell.

        Returns:
            Item: An instance of PencilMarkCell.
        """
        row, column, digits = cls.extract(board, yaml)
        return cls(board, row, column, digits)

    @classmethod
    def create2(cls, board: Board, yaml_data: dict) -> Item:
        """Create start PencilMarkCell from YAML line.

        Args:
            board (Board): The Sudoku board instance.
            yaml_data (dict): The YAML configuration for the cell.

        Returns:
            Item: An instance of PencilMarkCell.
        """
        return cls.create(board, yaml_data)

    def bookkeeping(self) -> None:
        """Update the bookkeeping for the cell to reflect its pencil-marked digits.

        This sets the possible digits for the cell in the board's bookkeeping system.
        """
        self.cell.book.set_possible(self.digits)
