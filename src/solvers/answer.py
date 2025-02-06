"""Answer."""

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
            wrong_row_size: bool = len(input_data) != board.size.row
            wrong_col_size: bool = any(len(row) != board.size.column for row in input_data)
            if wrong_col_size or wrong_row_size:
                raise ValueError('Input data dimensions do not match the board size.')

            for row in board.row_range:
                row_digits = [int(input_data[row - 1][col - 1]) for col in board.column_range]
                self.digits.append(row_digits)

    def __getitem__(self, index: int | tuple[int, int]) -> int:
        """Get the digit at a specific location on the board.

        Args:
            index (int | tuple[int, int]): Row and column as a tuple or a single index.

        Returns:
            int: The digit at the specified location on the board.

        Raises:
            ValueError: If the row or column index is invalid.
        """
        row: int
        col: int
        if isinstance(index, tuple):
            row, col = index
        else:
            row, col = divmod(index, self.board.size.column)
        if not self.board.is_valid(row, col):
            raise ValueError(f'Invalid row or column index: {row}, {col}')
        return self.digits[row - 1][col - 1]

    def __setitem__(self, index: int | tuple[int, int], digit: int) -> None:
        """Set the digit at a specific location on the board.

        Args:
            index (int | tuple[int, int]): Row and column as a tuple or a single index.
            digit (int): The digit to set at the specified location.

        Raises:
            ValueError: If the row or column index is invalid.
        """
        row: int
        col: int
        if isinstance(index, tuple):
            row, col = index
        else:
            row, col = divmod(index, self.board.size.column)

        if not self.board.is_valid(row, col):
            raise ValueError(f'Invalid row or column index: {row}, {col}')
        self.digits[row - 1][col - 1] = digit

    def __repr__(self) -> str:
        """Return a string representation of the Answer object, including the board and its line.

        Returns:
            str: A string representation of the Answer object.
        """
        lines: list[str] = [
            f"'{''.join([str(digit) for digit in self.digits[row]])}'"
            for row in range(self.board.size.row)
        ]
        string_line: str = ',\n    '.join(lines)
        return f'Answer(\n    {self.board!r},\n    [\n    {string_line}\n    ]\n)'

    def __str__(self) -> str:
        """Return a string representation of the Answer object for display purposes.

        Returns:
            str: A string representation of the Answer object.
        """
        lines: list[str] = ['Answer:']
        for row in self.board.row_range:
            digits: str = ''.join([str(self[row, col]) for col in self.board.column_range])
            lines.append(f'  - {digits}')
        return '\n'.join(lines)
