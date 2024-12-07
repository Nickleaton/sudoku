"""LineValidator."""

from src.items.board import Board
from src.validators.cell_validator import CellValidator
from src.validators.validator import Validator


class LineValidator(Validator):
    """Validator for a sequence of cells on the board.

    This class extends the base `Validator` class and ensures that the given
    sequence of cells is valid by checking the following conditions:
    - All cells must be valid and within the board's range.
    - All cells must be unique.
    - All cells must be connected by a king's move (i.e., each cell must be adjacent to the next cell,
    including diagonals).

    Inherits:
        Validator: The base class for creating custom validators.
    """

    @staticmethod
    def validate_cells(board: Board, data: dict) -> list[str]:
        """Validate the cells in the data list, checking for range, uniqueness, and key validity.

        This method performs several checks on each cell in `data`, including:
        - Ensuring the cell has valid keys (row and column).
        - Checking that the cell's coordinates are within the board's valid range.
        - Ensuring that no duplicate cells are present in the `data` list.

        Args:
            board (Board): The board to validate the cells against.
            data (dict): A list of dictionaries, each representing a cell with 'row' and 'column' keys.

        Returns:
            list[str]: The updated list of error messages.
        """
        errors: list[str] = []
        seen_cells: set[tuple[int, int]] = set()
        for cell in data:
            # Validate cell keys, range, and uniqueness
            errors.extend(CellValidator.has_valid_keys(cell))
            errors.extend(CellValidator.validate_range(board, cell))
            cell_tuple = (cell['row'], cell['column'])
            if cell_tuple in seen_cells:
                errors.append(f"Duplicate cell found: {cell_tuple:r}")
            seen_cells.add(cell_tuple)
        return errors

    @staticmethod
    def validate_connections(data: dict) -> list[str]:
        """Validate that the cells in the sequence are connected by a king's move.

        This method checks that each pair of consecutive cells in the `data` list are
        connected by a king's move, meaning each cell is adjacent (horizontally, vertically,
        or diagonally) to the next.

        Args:
            data (dict): A list of dictionaries, each representing a cell with 'row' and 'column' keys.

        Returns:
            list[str]: The updated list of error messages.
        """
        errors: list[str] = []
        for index in range(len(data) - 1):
            start = data[index]
            finish = data[index + 1]
            errors.extend(CellValidator.validate_connected(start, finish))
        return errors

    @staticmethod
    def validate(board: Board, data: dict) -> list[str]:
        """Validate that all cells in the sequence are valid, connected, and unique.

        The method ensures that:
            - All cells are within the board's range.
            - All cells are unique.
            - Cells are connected according to a king's move (each cell must be adjacent
              to the next, either horizontally, vertically, or diagonally).

        Args:
            board (Board): The board on which the validation is performed, containing
                           the board's range and other constraints.
            data (dict): A list of dictionaries, each representing a cell.
                                Each dictionary must contain the keys 'row' and 'column'
                                with integer values.

        Returns:
            list[str]: A list of error messages. An empty list is returned if the validation
                       passes, and error messages are returned if any validation check fails.
        """
        if not data:
            return ["The data cannot be empty."]
        errors: list[str] = []
        errors.extend(LineValidator.validate_cells(board, data))
        errors.extend(LineValidator.validate_connections(data))
        return errors
