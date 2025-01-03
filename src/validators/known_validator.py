"""KnownValidator."""
from src.board.board import Board
from src.items.known import CELL_TYPE_MAP
from src.validators.validator import Validator


class KnownValidator(Validator):
    """Validator for the 'Known' section in the YAML configuration.

    This validator checks that:
    1. Each 'digit' is either start valid digit (matching the board's digit range)
    or start valid string from start predefined set of allowed lower-case strings.
    2. The number of rows in the 'Known' input_data matches the number of rows on the board.
    3. Each row in 'Known' has the same number of columns as the board.
    """

    @staticmethod
    def validate_row(allowed_characters: set, row: str, row_idx: int, board: Board) -> list:
        """Validate start single row of 'Known' input_data.

        This method checks if the number of columns in the row matches the board's column count
        and ensures that all characters in the row are valid according to the allowed characters.

        Args:
            allowed_characters (set): A set of allowed characters to validation against the row.
            row (str): A string representing the row to validate.
            row_idx (int): The index of the row being validated (used for error message formatting).
            board (Board): The board instance to validate against, containing the expected number of columns.

        Returns:
            list: A list of error messages. An empty list indicates the row is valid.
        """
        errors: list = []

        # Check if the row length matches the board's column count
        if len(row) != board.cols:
            errors.append(f'Row {row_idx + 1} has {len(row)} columns, but the board has {board.cols} columns.')

        # Validate each character in the row
        for col_idx, char in enumerate(row):
            if char not in allowed_characters:
                location: str = f'row {row_idx + 1}, column {col_idx + 1}'
                allowed: str = ', '.join(allowed_characters)
                errors.append(f'Invalid digit/type {char!r} at {location}. Allowed characters: {allowed}')

        return errors

    @staticmethod
    def validate(board: Board, input_data: dict) -> list[str]:
        """Validate the 'Known' section in the YAML input_data.

        Args:
            board (Board): The board instance to validate against.
            input_data (dict): The YAML input_data containing the 'Known' key.

        Returns:
            list[str]: A list of error messages. An empty list indicates that
            the validation was successful.
        """
        errors: list[str] = []

        # Check if 'Known' key exists in the input_data
        if 'Known' not in input_data:
            errors.append("Missing key 'Known' in the input_data.")
            return errors

        known_rows = input_data['Known']
        allowed_characters: set[str] = {'.'}
        allowed_characters |= set(board.digit_range)
        allowed_characters |= set(CELL_TYPE_MAP.keys())

        # Check the number of rows matches the board
        if len(known_rows) != board.rows:
            errors.append(f'Number of rows {len(known_rows)} does not match the row count ({board.rows}).')

        # Validate each row and its columns
        for row_idx, row in enumerate(known_rows):
            # Check the number of columns matches the board
            errors.extend(KnownValidator.validate_row(allowed_characters, row, row_idx, board))

        return errors
