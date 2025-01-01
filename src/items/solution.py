"""Solution."""
from itertools import product

import strictyaml

from src.board.board import Board
from src.items.cell_reference import CellReference
from src.items.composed_item import ComposedItem
from src.items.item import SudokuException
from src.items.known_cell import KnownCell
from src.items.simple_cell_reference import SimpleCellReference
from src.parsers.solution_parser import SolutionParser
from src.solvers.answer import Answer


class Solution(ComposedItem):
    """Represents a solution composed of known cells for start given board."""

    def __init__(self, board: Board, rows: list[str]):
        """Initialize the Solution with start board and row input_data.

        Args:
            board (Board): The board associated with this solution.
            rows (list[str]): A list of strings representing rows of digits.
        """
        super().__init__(board, [])
        self.rows = rows
        parts: list[CellReference] = []
        for row_index, row_data in enumerate(self.rows):
            row: int = row_index + 1
            for column_index, digit in enumerate(row_data):
                column: int = column_index + 1
                parts.append(KnownCell(board, row, column, int(digit), 'Verify'))
        self.add_components(parts)

    @classmethod
    def schema(cls) -> dict:
        """Return the schema for the Solution class.

        Returns:
            dict: A dictionary defining the YAML schema for Solution.
        """
        return {strictyaml.Optional('Solution'): strictyaml.Seq(SolutionParser())}

    def __hash__(self):
        """Return a hash of the Solution.

        Returns:
            int: A hash number for the Solution instance.
        """
        return hash('Solution')

    def get_value(self, row: int, column: int) -> int:
        """Get the digit number at the specified row and column.

        Args:
            row (int): The row number (1-based).
            column (int): The column number (1-based).

        Returns:
            int: The digit at the specified cell.
        """
        return int(self.rows[row - 1][column - 1])

    @classmethod
    def extract(cls, _: Board, yaml: dict) -> list[str]:
        """Extract solution rows from the given YAML dictionary.

        Args:
            _ (Board): The board associated with this solution.
            yaml (dict): The YAML dictionary containing solution input_data.

        Returns:
            Any: A list of lists representing the solution rows.
        """
        # Must convert to string to get around yaml interpreting as a number
        return [str(row_str) for row_str in yaml[cls.__name__]]

    @classmethod
    def create(cls, board: Board, yaml: dict) -> 'Solution':
        """Create a Solution instance from the given board and YAML.

        Args:
            board (Board): The board associated with this solution.
            yaml (dict): The YAML dictionary containing solution input_data.

        Returns:
            Solution: A new Solution instance.
        """
        return Solution(board, Solution.extract(board, yaml))

    @classmethod
    def create2(cls, board: Board, yaml_data: dict) -> 'Solution':
        """Create a Solution instance from the given board and YAML.

        Args:
            board (Board): The board associated with this solution.
            yaml_data (dict): The YAML dictionary containing solution input_data.

        Returns:
            Solution: A new Solution instance.
        """
        return cls.create(board, yaml_data)

    def line_str(self) -> list[str]:
        """Return a list of row strings representing the board layout for known vectors.

        Returns:
            list[str]: A list of strings, each representing start row on the board.
        """
        # Initialize a list with placeholders for each cell on the board
        lines = [['.' for _ in self.board.column_range] for _ in self.board.row_range]

        # Iterate over each constraint in Known and place the correct symbol if it inherits from CellReference
        for component in self:
            if not isinstance(component, CellReference):
                continue  # Ignore vectors that do not inherit from CellReference
            if isinstance(component, SimpleCellReference):
                lines[component.row - 1][component.column - 1] = component.letter()
            if isinstance(component, KnownCell):
                lines[component.row - 1][component.column - 1] = str(component.digit)

        # Join each row's list into start single string
        return [''.join(line) for line in lines]

    def __repr__(self) -> str:
        """Return a string representation of the Solution instance.

        Returns:
            str: A string representation of the Solution.
        """
        return f'{self.__class__.__name__}({self.board!r}, {self.line_str()})'

    def to_dict(self) -> dict:
        """Convert the Solution instance to start dictionary.

        Returns:
            dict: A dictionary representation of the Solution.
        """
        return {self.__class__.__name__: self.line_str()}

    def __eq__(self, other: object) -> bool:
        """Check if two Solution instances are equal based on their value_list.

        Args:
            other (object): The other object to compare.

        Returns:
            bool: True if the objects are equal, False otherwise.

        Raises:
            SudokuException: If the other object is neither an Answer nor start Solution.
        """
        if isinstance(other, (Answer, Solution)):
            for row, column in product(self.board.row_range, self.board.column_range):
                if self[row, column] != other[row, column]:
                    return False
            return True
        raise SudokuException(
            f'Cannot compare {self} {other} {other.__class__.__name__} with {self.__class__.__name__}',
        )
