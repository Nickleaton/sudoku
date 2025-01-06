from src.board.board import Board


class Answer:
    """Represents the solution (line) for a Sudoku board."""

    def __init__(self, board: Board, input_data: list[str] | None = None) -> None:
        """Initialize the Answer object with the given board and optional line.

        Args:
            board (Board): The board associated with this line.
            input_data (list[str] | None): A list of strings representing the initial board configuration.

        Raises:
            ValueError: If the input_data dimensions do not match the board's dimensions.
        """
        self.board: Board = board
        self.digits: list[list[int]] = []
        if input_data is not None:
            if len(input_data) != len(board.row_range) or any(
                len(row) != len(board.column_range) for row in input_data
            ):
                raise ValueError('Input data dimensions do not match the board size.')

            for row in board.row_range:
                row_digits = [int(input_data[row - 1][col - 1]) for col in board.column_range]
                self.digits.append(row_digits)

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
        """Return a string representation of the Answer object, including the board and its line.

        Returns:
            str: A string representation of the Answer object.
        """
        lines = [
            "'" + ''.join([str(digit) for digit in self.digits[row - 1]]) + "'"
            for row in self.board.row_range
        ]
        representation: str = 'Answer(\n'
        representation += f'    {self.board!r},\n'
        representation += f'    [\n    '
        representation += ',\n    '.join(lines)
        representation += f'    ]\n'
        representation += ')'
        return representation

    def __str__(self) -> str:
        """Return a string representation of the Answer object for display purposes.

        Returns:
            str: A formatted string of the board with its cell values.
        """
        lines: list[str] = ['Answer:']
        for row in self.board.row_range:
            digits: str = ''.join([str(self[row, column]) for column in self.board.column_range])
            lines.append(f'  - {digits}')
        return '\n'.join(lines)

    def __eq__(self, other: object) -> bool:
        """Check equality between two Answer objects.

        Args:
            other (object): The object to compare with this Answer.

        Returns:
            bool: True if both Answer objects are identical, False otherwise.
        """
        if not isinstance(other, Answer):
            return False
        return self.digits == other.digits

    @classmethod
    def extract(cls, _: Board, yaml: dict) -> list[str]:
        """Extract the line from the YAML dictionary.

        Args:
            _ (Board): The board object (unused here).
            yaml (dict): A dictionary containing the board's configuration.

        Returns:
            list[str]: A list of strings representing the board line.
        """
        return [str(line) for line in yaml]

    @classmethod
    def create(cls, board: Board, yaml: dict) -> 'Answer':
        """Create an Answer object from the given board and YAML line.

        Args:
            board (Board): The board associated with this line.
            yaml (dict): A dictionary containing the board configuration.

        Returns:
            Answer: A newly created Answer object.
        """
        return Answer(board, Answer.extract(board, yaml))
    #
    # def standard_string(self) -> str:
    #     """Return the board as a formatted string with separators for rows and boxes.
    #
    #     Returns:
    #         str: A formatted string of the board with separators.
    #     """
    #     separator: str = '+'.join(['-' * (board * 2 + (box_cols - 1))] * (total_cols // box_cols))
    #
    # def line_separator(self) -> str:
    #     """Generate a separator string for the board layout.
    #
    #     Returns:
    #         str: A string representing a separator line between rows/boxes.
    #     """
    #     line_parts: list[str] = []
    #     for column in self.board.column_range:
    #         if (column - 1) % self.board.box_columns == 0:
    #             line_parts.append('+-')
    #         line_parts.append('--')
    #     line_parts.append('+')
    #     return ''.join(line_parts)
