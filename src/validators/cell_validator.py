"""CellValidator."""

from src.board.board import Board
from src.validators.validator import Validator

ROW = 'Row'
COL = 'Column'


class CellValidator(Validator):
    """Validator for individual cells.

    Provides methods to validate cell attributes, ensure cells are within the board's range,
    and check connectivity between cells.
    """

    @staticmethod
    def has_valid_keys(input_data: dict[str, int]) -> list[str]:
        """Validate that the 'Row' and 'Column' keys are present and have integer values.

        Args:
            input_data (dict[str, int]): The dictionary representing a cell, which must contain 'Row' and 'Column' keys.

        Returns:
            list[str]: A list of error messages. An empty list if validation passes.
        """
        errors: list[str] = []
        if ROW not in input_data:
            errors.append(f'Cell is missing {ROW!r}.')
        elif not isinstance(input_data[ROW], int):
            errors.append(f'Cell must have integer {ROW!r}.')
        if COL not in input_data:
            errors.append(f'Cell is missing {COL!r}.')
        elif not isinstance(input_data[COL], int):
            errors.append(f'Cell must have integer {COL!r}.')
        return errors

    @staticmethod
    def validate_range(board: Board, input_data: dict[str, int]) -> list[str]:
        """Validate that the cell is within the valid range on the board.

        Args:
            board (Board): The board on which the validation is performed.
            input_data (dict[str, int]): The dictionary representing the cell.

        Returns:
            list[str]: A list of error messages. An empty list if validation passes.
        """
        errors: list[str] = []
        row, col = input_data[ROW], input_data[COL]
        if not isinstance(row, int) or not isinstance(col, int):
            errors.append(f'Cell must have integer {ROW!r} and {COL!r}.')
            return errors
        if not board.is_valid(row, col):
            errors.append(f'Invalid cell: ({row}, {col})')
        return errors

    @staticmethod
    def validate_kings_move(cell1: dict[str, int], cell2: dict[str, int]) -> list[str]:
        """Validate that two cells are connected by a king's move.

        Args:
            cell1 (dict[str, int]): The first cell dictionary with 'Row' and 'Column' keys.
            cell2 (dict[str, int]): The second cell dictionary with 'Row' and 'Column' keys.

        Returns:
            list[str]: A list of error messages. An empty list if the cells are connected
                       by a king's move, otherwise a list containing a single error message.
        """
        row_difference: int = abs(cell1[ROW] - cell2[ROW])
        col_difference: int = abs(cell1[COL] - cell2[COL])
        if row_difference > 1 or col_difference > 1:
            return [f"Cells at {cell1!r} and {cell2!r} are not connected by a king's move."]
        return []

    @staticmethod
    def validate_connected(cell1: dict[str, int], cell2: dict[str, int]) -> list[str]:
        """Validate that two cells are connected by a king's move.

        Args:
            cell1 (dict[str, int]): The first cell dictionary with 'Row' and 'Column' keys.
            cell2 (dict[str, int]): The second cell dictionary with 'Row' and 'Column' keys.

        Returns:
            list[str]: A list of error messages. An empty list if the cells are connected by a king's move,
                       otherwise a list containing error messages.
        """
        errors: list[str] = []
        errors.extend(CellValidator.has_valid_keys(cell1))
        errors.extend(CellValidator.has_valid_keys(cell2))
        if errors:
            return errors
        errors.extend(CellValidator.validate_kings_move(cell1, cell2))
        return errors

    @staticmethod
    def validate_horizontal_connectivity(cell1: dict[str, int], cell2: dict[str, int]) -> list[str]:
        """Validate if two cells are horizontally connected (same row, adjacent columns).

        Args:
            cell1 (dict[str, int]): The first cell dictionary with 'Row' and 'Column' keys.
            cell2 (dict[str, int]): The second cell dictionary with 'Row' and 'Column' keys.

        Returns:
            list[str]: A list of error messages. An empty list if the cells are horizontally connected.
        """
        errors: list[str] = []
        if cell1[ROW] != cell2[ROW]:
            errors.append(f'Cells {cell1!r} and {cell2!r} are not in the same row.')
        elif cell1[COL] + 1 != cell2[COL]:
            errors.append(f'Cells {cell1!r} and {cell2!r} are not horizontally adjacent.')
        return errors

    @staticmethod
    def validate(board: Board, input_data: dict[str, int]) -> list[str]:
        """Run all validations on a single cell.

        Args:
            board (Board): The board on which the validation is performed.
            input_data (dict[str, int]): The dictionary representing the cell.

        Returns:
            list[str]: A list of error messages. An empty list if validation passes.
        """
        errors: list[str] = []
        errors.extend(CellValidator.has_valid_keys(input_data))
        if errors:
            return errors
        errors.extend(CellValidator.validate_range(board, input_data))
        return errors
