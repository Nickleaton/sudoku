from src.validators.validator import Validator
from src.items.board import Board


class CellValidator(Validator):

    @staticmethod
    def has_valid_keys(data: dict) -> list[str]:
        """Validate that the 'row' and 'column' keys are present and have integer values.

        Args:
            data (dict): The dictionary representing a cell, which must contain the 'row' and 'column' keys.

        Returns:
            List[str]: A list of error messages. An empty list if validation passes.
        """
        errors: list[str] = []
        if 'row' not in data or 'column' not in data:
            errors.append("Cell is missing 'row' or 'column' keys.")
        elif not isinstance(data['row'], int) or not isinstance(data['column'], int):
            errors.append("Cell must have integer 'row' and 'column' values.")
        return errors

    @staticmethod
    def validate_range(board: Board, data: dict) -> list[str]:
        """Validate that the cell is within the valid range on the board.

        Args:
            board (Board): The board on which the validation is performed.
            data (dict): The dictionary representing a cell, which must contain 'row' and 'column' keys.

        Returns:
            List[str]: A list of error messages. An empty list if validation passes.
        """
        errors: list[str] = []
        row, col = data['row'], data['column']
        if not board.is_valid(row, col):
            errors.append(f"Invalid cell: ({row}, {col})")
        return errors

    @staticmethod
    def validate_connected(cell1: dict, cell2: dict) -> list[str]:
        """Validate that two cells are connected by a king's move.

        A king's move is a move that goes to an adjacent cell in any direction, including diagonals.

        Args:
            cell1 (dict): The first cell dictionary with 'row' and 'column' keys.
            cell2 (dict): The second cell dictionary with 'row' and 'column' keys.

        Returns:
            List[str]: A list of error messages. An empty list if the cells are connected by a king's move.
        """
        errors: list[str] = []

        # Ensure both cells are valid before comparing
        errors.extend(CellValidator.has_valid_keys(cell1))
        errors.extend(CellValidator.has_valid_keys(cell2))

        if errors:
            return errors

        row1, col1 = cell1['row'], cell1['column']
        row2, col2 = cell2['row'], cell2['column']
        if abs(row1 - row2) > 1 or abs(col1 - col2) > 1:
            errors.append(f"Cells at ({row1}, {col1}) and ({row2}, {col2}) are not connected by a king's move.")
        return errors

    @staticmethod
    def validate_horizontal_connectivity(cell1: dict, cell2: dict) -> list[str]:
        """Validate if two cells are horizontally connected (same row, adjacent columns)."""
        errors: list[str] = []
        row1, col1 = cell1['row'], cell1['column']
        row2, col2 = cell2['row'], cell2['column']

        # Check if cells are in the same row and columns are adjacent
        if row1 != row2:
            errors.append(f"Cells at ({row1}, {col1}) and ({row2}, {col2}) are not in the same row.")
        elif col1 + 1 != col2:
            errors.append(f"Cells at ({row1}, {col1}) and ({row2}, {col2}) are not horizontally adjacent.")

        return errors

    @staticmethod
    def validate(board: Board, data: dict) -> list[str]:
        """Run all validations on a single cell.

        This method checks if the cell has valid keys, if it is within the board's range, and if it is connected to the previous cell.

        Args:
            board (Board): The board on which the validation is performed.
            data (dict): The dictionary representing the cell, which must contain 'row' and 'column' keys.

        Returns:
            list[str]: A list of error messages. An empty list if validation passes.
        """
        errors: List[str] = []
        errors.extend(CellValidator.has_valid_keys(data))
        errors.extend(CellValidator.validate_range(board, data))
        return errors
