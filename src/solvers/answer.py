"""Answer class."""
from itertools import product

from src.items.board import Board
from src.utils.sudoku_exception import SudokuException


class Answer:
    """Represents the solution (answer) for a Sudoku board."""

    def __init__(self, board: Board, data: list[str] | None = None):
        """Initialize the Answer object with a given board and optional data.

        Args:
            board (Board): The board associated with this answer.
            data (Optional[list[str]]): A list of strings representing the initial board configuration.
        """
        self.board = board
        self.data: list[list[int]] = [
            [0 for _ in board.column_range]
            for _ in board.row_range
        ]
        if data is not None:
            for row, column in product(board.row_range, board.column_range):
                digit = int(data[row - 1][column - 1])
                self.set_value(row, column, digit)

    def set_value(self, row: int, column: int, value: int) -> None:
        """Set the value of a specific cell on the board.

        Args:
            row (int): The row number (1-based index).
            column (int): The column number (1-based index).
            value (int): The value to set at the specified position.
        """
        self.data[row - 1][column - 1] = value

    def get_value(self, row: int, column: int) -> int:
        """Get the value of a specific cell on the board.

        Args:
            row (int): The row number (1-based index).
            column (int): The column number (1-based index).

        Returns:
            int: The value at the specified position on the board.
        """
        return self.data[row - 1][column - 1]

    def __repr__(self) -> str:
        """Return a string representation of the Answer object, including the board and its data.

        Returns:
            str: A string representation of the Answer object.
        """
        lines = [
            "".join([str(d) for d in self.data[row - 1]])
            for row in self.board.row_range
        ]
        return (f"Answer("
                f"{self.board!r},"
                f"{lines!r}"
                ")"
                )

    def __str__(self) -> str:
        """Return a string view of the Answer object for display purposes.

        Returns:
            str: A formatted string of the board and its values.
        """
        result = "Answer:\n"
        for row in self.data:
            result += f"  - {''.join([str(int(d)) for d in row])}\n"
        return result

    # pylint: disable=loop-invariant-statement
    def __eq__(self, other: object) -> bool:
        """Check equality between two Answer objects.

        Args:
            other (object): The object to compare with this Answer.

        Returns:
            bool: True if both Answer objects are identical, False otherwise.
        """
        if isinstance(other, Answer):
            for row, column in product(self.board.row_range, self.board.column_range):
                if self.get_value(row, column) != other.get_value(row, column):
                    return False
            return True
        raise SudokuException(f"Cannot compare {other.__class__.__name__} with {self.__class__.__name__}")

    @classmethod
    def extract(cls, _: Board, yaml: dict) -> list[str]:
        """Extract the answer data from a YAML dictionary.

        Args:
            _ (Board): The board object (unused here).
            yaml (dict): A dictionary containing the board's configuration.

        Returns:
            list[str]: A list of strings representing the board data.
        """
        return [str(line) for line in yaml]

    @classmethod
    def create(cls, board: Board, yaml: dict) -> 'Answer':
        """Create an Answer object from a board and YAML data.

        Args:
            board (Board): The board associated with this answer.
            yaml (dict): A dictionary containing the board configuration.

        Returns:
            Answer: A newly created Answer object.
        """
        return Answer(board, Answer.extract(board, yaml))

    # pylint: disable=loop-invariant-statement
    def standard_string(self) -> str:
        """Return the board as a formatted string with separators for rows and boxes.

        Returns:
            str: A formatted string of the board with separators.
        """
        result = ""
        for row in self.board.row_range:
            if (row - 1) % self.board.box_rows == 0:
                result += self.separator()
            for column in self.board.column_range:
                if (column - 1) % self.board.box_columns == 0:
                    result += "| "
                result += f"{self.data[row - 1][column - 1]} "
            result += "|\n"
        result += self.separator()
        return result

    def separator(self) -> str:
        """Generate a separator string for the board layout.

        Returns:
            str: A string representing a separator line between rows/boxes.
        """
        res = ""
        for column in self.board.column_range:
            if (column - 1) % self.board.box_columns == 0:
                res += "+-"
            res += "--"
        return res + "+\n"
