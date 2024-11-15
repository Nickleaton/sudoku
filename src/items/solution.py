"""Solution."""
from itertools import product
from typing import List, Any, Dict

from strictyaml import Seq, Optional

from src.items.board import Board
from src.items.cell_reference import CellReference
from src.items.composed_item import ComposedItem
from src.items.known_cell import KnownCell
from src.items.simple_cell_reference import SimpleCellReference
from src.parsers.solution_parser import SolutionParser
from src.solvers.answer import Answer


class Solution(ComposedItem):
    """Represents a solution composed of known cells for a given board."""

    def __init__(self, board: Board, rows: List[str]):
        """Initialize the Solution with a board and row data.

        Args:
            board (Board): The board associated with this solution.
            rows (List[str]): A list of strings representing rows of digits.
        """
        super().__init__(board, [])
        self.rows = rows
        parts: List[CellReference] = []
        for y, data in enumerate(self.rows):
            row = y + 1
            for x, digit in enumerate(data):
                column = x + 1
                parts.append(KnownCell(board, row, column, int(digit), 'Verify'))
        self.add_items(parts)

    @classmethod
    def schema(cls) -> Dict:
        """Return the schema for the Solution class.

        Returns:
            Dict: A dictionary defining the YAML schema for Solution.
        """
        return {Optional("Solution"): Seq(SolutionParser())}

    def __hash__(self):
        """Return a hash of the Solution.

        Returns:
            int: A hash value for the Solution instance.
        """
        return hash("Solution")

    def get_value(self, row: int, column: int) -> int:
        """Get the digit value at the specified row and column.

        Args:
            row (int): The row number (1-based).
            column (int): The column number (1-based).

        Returns:
            int: The digit at the specified cell.
        """
        return int(self.rows[row - 1][column - 1])

    @classmethod
    def extract(cls, board: Board, yaml: Dict) -> Any:
        """Extract solution rows from the given YAML dictionary.

        Args:
            board (Board): The board associated with this solution.
            yaml (Dict): The YAML dictionary containing solution data.

        Returns:
            Any: A list of lists representing the solution rows.
        """
        return [list(str(y)) for y in yaml[cls.__name__]]

    @classmethod
    def create(cls, board: Board, yaml: Dict) -> 'Solution':
        """Create a Solution instance from the given board and YAML.

        Args:
            board (Board): The board associated with this solution.
            yaml (Dict): The YAML dictionary containing solution data.

        Returns:
            Solution: A new Solution instance.
        """
        items = Solution.extract(board, yaml)
        return Solution(board, items)

    def line_str(self) -> List[str]:
        """Return a list of row strings representing the board layout for known items.

        Returns:
            List[str]: A list of strings, each representing a row on the board.
        """
        # Initialize a 2D list with placeholders for each cell on the board
        lines = [['.' for _ in self.board.column_range] for _ in self.board.row_range]

        # Iterate over each item in Known and place the correct symbol if it inherits from CellReference
        for item in self:
            if not isinstance(item, CellReference):
                continue  # Ignore items that do not inherit from CellReference
            if isinstance(item, SimpleCellReference):
                lines[item.row - 1][item.column - 1] = item.letter()
            if isinstance(item, KnownCell):
                lines[item.row - 1][item.column - 1] = str(item.digit)

        # Join each row's list into a single string
        return ["".join(line) for line in lines]

    def __repr__(self) -> str:
        """Return a string representation of the Solution instance.

        Returns:
            str: A string representation of the Solution.
        """
        return f"{self.__class__.__name__}({self.board!r}, {self.line_str()})"

    def to_dict(self) -> Dict:
        """Convert the Solution instance to a dictionary.

        Returns:
            Dict: A dictionary representation of the Solution.
        """
        return {self.__class__.__name__: self.line_str()}

    def __eq__(self, other: object) -> bool:
        """Check if two Solution instances are equal based on their values.

        Args:
            other (object): The other object to compare.

        Returns:
            bool: True if the objects are equal, False otherwise.

        Raises:
            Exception: If the other object is neither an Answer nor a Solution.
        """
        if isinstance(other, Answer) or isinstance(other, Solution):
            for row, column in product(self.board.row_range, self.board.column_range):
                if self.get_value(row, column) != other.get_value(row, column):
                    return False
            return True
        raise Exception(f"Cannot compare {self} {other} {other.__class__.__name__} with {self.__class__.__name__}")

