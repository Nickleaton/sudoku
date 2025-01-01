"""Answer class."""
from itertools import product

from src.board.board import Board
from src.utils.sudoku_exception import SudokuException


class Answer:
    """Represents the solution (input_data) for a Sudoku board."""

    def __init__(self, board: Board, input_data: list[str] | None = None):
        """Initialize the Answer object with the given board and optional input_data.

        Args:
            board (Board): The board associated with this input_data.
            input_data (list[str] | None): A list of strings representing the initial board configuration.
        """
        self.board = board
        self.digits: list[list[int]] = [
            [0 for _ in board.column_range]
            for _ in board.row_range
        ]
        if input_data is not None:
            for row, column in product(board.row_range, board.column_range):
                digit = int(input_data[row - 1][column - 1])
                self[row, column] = digit

    def __getitem__(self, indices: tuple[int, int]) -> int:
        """Get the digit at a specific position on the board.

        Args:
            indices (tuple[int, int]): A tuple containing (row, column) indices.

        Returns:
            int: The digit at the specified position on the board.

        Raises:
            ValueError: If the row or column index is invalid.
        """
        row, column = indices
        if not self.board.is_valid(row, column):
            raise ValueError(f'Invalid row or column index: {row}, {column}')
        return self.digits[row - 1][column - 1]

    def __setitem__(self, indices: tuple[int, int], digit: int) -> None:
        """Set the digit at a specific position on the board.

        Args:
            indices (tuple[int, int]): A tuple containing (row, column) indices.
            digit (int): The digit to set at the specified position.

        Raises:
            ValueError: If the row or column index is invalid.
        """
        row, column = indices
        if not self.board.is_valid(row, column):
            raise ValueError(f'Invalid row or column index: {row}, {column}')
        self.digits[row - 1][column - 1] = digit

    def __repr__(self) -> str:
        """Return a string representation of the Answer object, including the board and its input_data.

        Returns:
            str: A string representation of the Answer object.
        """
        lines = [
            ''.join([str(digit) for digit in self.digits[row - 1]])
            for row in self.board.row_range
        ]
        return f'Answer({self.board!r} {lines!r})'

    def __str__(self) -> str:
        """Return a string representation of the Answer object for display purposes.

        Returns:
            str: A formatted string of the board with its cell_values.
        """
        lines: list[str] = ['Answer:']
        for row in self.board.row_range:
            digits: str = ''.join([str(digit) for digit in row])
            lines.append(f'  - {digits}')
        return '\n'.join(lines)

    def __eq__(self, other: object) -> bool:
        """Check equality between two Answer objects.

        Args:
            other (object): The object to compare with this Answer.

        Returns:
            bool: True if both Answer objects are identical, False otherwise.

        Raises:
            SudokuException: If the other object is not an Answer.
        """
        if isinstance(other, Answer):
            for row, column in product(self.board.row_range, self.board.column_range):
                if self[row, column] != other[row, column]:
                    return False
            return True
        raise SudokuException(f'Cannot compare {other.__class__.__name__} with {self.__class__.__name__}')

    @classmethod
    def extract(cls, _: Board, yaml: dict) -> list[str]:
        """Extract the input_data from the YAML dictionary.

        Args:
            _ (Board): The board object (unused here).
            yaml (dict): A dictionary containing the board's configuration.

        Returns:
            list[str]: A list of strings representing the board input_data.
        """
        return [str(line) for line in yaml]

    @classmethod
    def create(cls, board: Board, yaml: dict) -> 'Answer':
        """Create an Answer object from the given board and YAML input_data.

        Args:
            board (Board): The board associated with this input_data.
            yaml (dict): A dictionary containing the board configuration.

        Returns:
            Answer: A newly created Answer object.
        """
        return Answer(board, Answer.extract(board, yaml))

    def standard_string(self) -> str:
        """Return the board as a formatted string with separators for rows and boxes.

        Returns:
            str: A formatted string of the board with separators.
        """
        lines: list[str] = []
        for row in self.board.row_range:
            if (row - 1) % self.board.box_rows == 0:
                lines.append(self.line_separator())
            row_content: str = ' '.join(
                f'{self.digits[row - 1][column - 1]}'
                for column in self.board.column_range
            )
            row_with_borders: str = f'| {row_content} |'
            lines.append(row_with_borders)
        lines.append(self.line_separator())
        return '\n'.join(lines)

    def line_separator(self) -> str:
        """Generate a separator string for the board layout.

        Returns:
            str: A string representing a separator line between rows/boxes.
        """
        line_parts: list[str] = [
            '+-' if (column - 1) % self.board.box_columns == 0 else '--'
            for column in self.board.column_range
        ]
        line_parts.append('+\n')
        return ''.join(line_parts)
