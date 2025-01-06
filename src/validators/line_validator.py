"""LineValidator."""

from src.board.board import Board
from src.validators.cell_validator import CellValidator
from src.validators.validator import Validator


class LineValidator(Validator):
    """Validator for sequences of cells on the board.

    This class extends the base `Validator` class and ensures that the given sequence of cells is valid by
    checking the following conditions:
    - All cells must be valid and within the board's range.
    - All cells must be unique.
    - All cells must be connected by a king's move (i.e., each cell must be adjacent to the next cell,
      including diagonals).

    Inherits:
        Validator: The base class for creating custom validators.
    """

    @staticmethod
    def validate_cells(board: Board, input_data: list[dict[str, int]]) -> list[str]:
        """Validate the cells in the line list, checking for range, uniqueness, and key validity.

        Args:
            board (Board): The board to validate the cells against.
            input_data (list[dict[str, int]]): A list of dictionaries, each representing a cell with 'Row' and 'Column' keys.

        Returns:
            list[str]: A list of error messages. An empty list if validation passes.
        """
        errors: list[str] = []
        validator: CellValidator = CellValidator()
        for cell in input_data:
            errors.extend(validator.validate(board, cell))
        return errors

    @staticmethod
    def validate_unique(line: list[dict[str, int]]) -> list[str]:
        """Ensure that all cells in the line are unique.

        Args:
            line (list[dict[str, int]]): A list of dictionaries, each representing a cell with 'Row' and 'Column' keys.

        Returns:
            list[str]: A list of error messages. An empty list if all cells are unique.
        """
        errors: list[str] = []
        seen: set[tuple[int, int]] = set()
        for cell in line:
            coord = (cell['Row'], cell['Column'])
            if coord in seen:
                errors.append(f"Duplicate cell: {coord}")
            seen.add(coord)
        return errors

    @staticmethod
    def validate_connections(line: list[dict[str, int]]) -> list[str]:
        """Validate that the cells in the sequence are connected by a king's move.

        This method checks that each pair of consecutive cells in the `line` are connected by a king's move,
        meaning each cell is adjacent (horizontally, vertically, or diagonally) to the next.

        Args:
            line (list[dict[str, int]]): A list of dictionaries, each representing a cell with 'Row' and 'Column' keys.

        Returns:
            list[str]: A list of error messages. An empty list if all cells are connected by a king's move.
        """
        errors: list[str] = []
        for index in range(len(line) - 1):
            start = line[index]
            finish = line[index + 1]
            errors.extend(CellValidator.validate_connected(start, finish))
        return errors

    @staticmethod
    def validate(board: Board, line: list[dict[str, int]]) -> list[str]:
        """Validate that all cells in the sequence are valid, connected, and unique.

        Args:
            board (Board): The board on which the validation is performed, containing
                           the board's range and other constraints.
            line (dict[str, int]): A list of dictionaries, each representing a cell with 'Row' and 'Column' keys.

        Returns:
            list[str]: A list of error messages. An empty list if validation passes, otherwise a list of errors.
        """
        errors: list[str] = []
        errors.extend(LineValidator.validate_cells(board, line))
        errors.extend(LineValidator.validate_connections(line))
        errors.extend(LineValidator.validate_unique(line))
        return errors
