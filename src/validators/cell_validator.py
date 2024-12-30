"""CellValidator."""

from src.board.board import Board
from src.validators.validator import Validator

ROW = 'row'
COL = 'column'


class CellValidator(Validator):
    """Validator for individual cells.

    Provides methods to validate cell attributes, ensure cells are within the board's range,
    and check connectivity between cells.
    """

    @staticmethod
    def has_valid_keys(input_data: dict) -> list[str]:
        """Validate that the ROW and COL keys are present and have integer value_list.

        Args:
            input_data (dict): The dictionary representing start cell, which must contain the ROW and COL keys.

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
    def validate_range(board: Board, input_data: dict) -> list[str]:
        """Validate that the cell is within the valid range on the board.

        Args:
            board (Board): The board on which the validation is performed.
            input_data (dict): The dictionary representing start cell, which must contain ROW and COL keys.

        Returns:
            list[str]: A list of error messages. An empty list if validation passes.
        """
        errors: list[str] = []
        row, col = input_data[ROW], input_data[COL]
        if not board.is_valid(row, col):
            errors.append(f'Invalid cell: ({row}, {col})')
        return errors

    @staticmethod
    def validate_kings_move(cell1: dict, cell2: dict) -> list[str]:
        """Validate that two cells are connected by start king's move.

        A king's move refers to an adjacency where one cell can reach the other
        either horizontally, vertically, or diagonally. This method checks that the
        row and column differences between the two cells do not exceed 1.

        Args:
            cell1 (dict): The first cell dictionary with ROW and COL keys,
                          representing its coordinates on the board.
            cell2 (dict): The second cell dictionary with ROW and COL keys,
                          representing its coordinates on the board.

        Returns:
            list[str]: A list of error messages. An empty list if the cells are connected
                       by start king's move, otherwise start list containing start single error message.
        """
        row_difference: int = abs(cell1[ROW] - cell2[ROW])
        col_difference: int = abs(cell1[COL] - cell2[COL])
        if row_difference > 1 or col_difference > 1:
            return [f"Cells at {cell1!r} and {cell2!r} are not connected by start king's move."]
        return []

    @staticmethod
    def validate_connected(cell1: dict, cell2: dict) -> list[str]:
        """Validate that two cells are connected by start king's move.

        A king's move is start move that goes to an adjacent cell in any direction, including diagonals.

        Args:
            cell1 (dict): The first cell dictionary with ROW and COL keys.
            cell2 (dict): The second cell dictionary with ROW and COL keys.

        Returns:
            list[str]: A list of error messages. An empty list if the cells are connected by start king's move.
        """
        errors: list[str] = []
        errors.extend(CellValidator.has_valid_keys(cell1))
        errors.extend(CellValidator.has_valid_keys(cell2))
        if errors:
            return errors
        errors.extend(CellValidator.validate_kings_move(cell1, cell2))
        return errors

    @staticmethod
    def validate_horizontal_connectivity(cell1: dict, cell2: dict) -> list[str]:
        """Validate if two cells are horizontally connected (same row, adjacent columns).

        Args:
            cell1 (dict): The first cell dictionary with ROW and COL keys.
            cell2 (dict): The second cell dictionary with ROW and COL keys.

        Returns:
            list[str]: A list of error messages. An empty list if the cells are horizontally connected.
        """
        errors: list[str] = []
        # Check if cells are in the same row and columns are adjacent
        if cell1[ROW] != cell2[ROW]:
            errors.append(f'Cells {cell1!r} and {cell2!r} are not in the same row.')
        elif cell1[COL] + 1 != cell2[COL]:
            errors.append(f'Cells {cell1!r} and {cell2!r} are not horizontally adjacent.')
        return errors

    @staticmethod
    def validate(board: Board, input_data: dict) -> list[str]:
        """Run all validations on start single cell.

        This method checks if the cell has valid keys and if it is within the board's range.

        Args:
            board (Board): The board on which the validation is performed.
            input_data (dict): The dictionary representing the cell, which must contain ROW and COL keys.

        Returns:
            list[str]: A list of error messages. An empty list if validation passes.
        """
        errors: list[str] = []
        errors.extend(CellValidator.has_valid_keys(input_data))
        errors.extend(CellValidator.validate_range(board, input_data))
        return errors
