"""PencilMark."""
import re

from src.glyphs.glyph import Glyph
from src.items.board import Board
from src.items.cell_reference import CellReference
from src.items.item import Item
from src.utils.rule import Rule
from src.utils.sudoku_exception import SudokuException


class PencilMarkCell(CellReference):
    """Represents a cell with pencil-marked digits in a Sudoku puzzle."""

    def __init__(self, board: Board, row: int, column: int, digits: list[int]):
        """Initialize a PencilMarkCell.

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
            list[Rule]: A list of rules, including a restriction on the digits.
        """
        return [Rule("PencilMark", 1, "Digits restricted")]

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
            ".PencilMarkCell": {
                "fill": "gainsboro"
            }
        }

    def __repr__(self) -> str:
        """Return a string representation of the PencilMarkCell.

        Returns:
            str: A string representation of the pencil-marked cell.
        """
        return f"{self.__class__.__name__}({self.board!r}, {self.cell!r}, {self.digits!r})"

    def to_dict(self) -> dict:
        """Convert the pencil-marked cell to a dictionary representation.

        Returns:
            dict: A dictionary containing the cell's row, column, and digits.
        """
        return {self.__class__.__name__: f"{self.cell.row_column_string}={''.join([str(d) for d in self.digits])}"}

    @classmethod
    def extract(cls, board: Board, yaml: dict) -> tuple:
        """Extract the parameter_types needed to create a PencilMarkCell from YAML data.

        Args:
            board (Board): The Sudoku board instance.
            yaml (dict): The YAML configuration for the cell.

        Returns:
            tuple: A tuple containing the row, column, and pencil-marked digits.
        """
        regex = re.compile(f"([{board.digit_values}])([{board.digit_values}])=([{board.digit_values}]+)")
        match = regex.match(yaml[cls.__name__])
        if match is None:
            raise SudokuException("Match is None, expected a valid match.")
        row_str, column_str, digits = match.groups()
        return int(row_str), int(column_str), [int(s) for s in digits]

    @classmethod
    def create(cls, board: Board, yaml: dict) -> Item:
        """Create a PencilMarkCell from YAML data.

        Args:
            board (Board): The Sudoku board instance.
            yaml (dict): The YAML configuration for the cell.

        Returns:
            Item: An instance of PencilMarkCell.
        """
        row, column, digits = cls.extract(board, yaml)
        return cls(board, row, column, digits)

    def bookkeeping(self) -> None:
        """Update the bookkeeping for the cell to reflect its pencil-marked digits.

        This sets the possible digits for the cell in the board's bookkeeping system.
        """
        self.cell.book.set_possible(self.digits)
