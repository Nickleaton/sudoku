"""KnownValidator."""
from src.items.board import Board
from src.items.known import CELL_TYPE_MAP
from src.validators.validator import Validator


class KnownValidator(Validator):
    """Validator for the 'Known' section in the YAML configuration.

    This validator checks that:
    1. Each 'digit' is either a valid digit (matching the board's digit range)
    or a valid string from a predefined set of allowed lower-case strings.
    2. The number of rows in the 'Known' data matches the number of rows on the board.
    3. Each row in 'Known' has the same number of columns as the board.
    """

    @staticmethod
    def validate_row(allowed_characters: set, row: str, row_idx: int, board: Board) -> list:
        """Validate a single row of 'Known' data.

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
            errors.append(
                f"Row {row_idx + 1} has {len(row)} columns, "
                f"but the board expects {board.cols} columns."
            )

        # Validate each character in the row
        for col_idx, char in enumerate(row):
            if char not in allowed_characters:
                location: str = f"row {row_idx + 1}, column {col_idx + 1}"
                allowed: str = ", ".join(allowed_characters)
                errors.append(
                    f"Invalid digit/type '{char}' at {location}. "
                    f"Allowed characters: {allowed}"
                )

        return errors

    @staticmethod
    def validate(board: Board, data: dict) -> list[str]:
        """Validate the 'Known' section in the YAML data.

        Args:
            board (Board): The board instance to validate against.
            data (dict): The YAML data containing the 'Known' key.

        Returns:
            list[str]: A list of error messages. An empty list indicates that
            the validation was successful.
        """
        errors: list[str] = []

        # Check if 'Known' key exists in the data
        if "Known" not in data:
            errors.append("Missing 'Known' key in the data.")
            return errors

        known_rows = data["Known"]
        allowed_characters: set[str] = {'.'}
        allowed_characters |= set(board.digit_range)
        allowed_characters |= set(CELL_TYPE_MAP.keys())

        # Check the number of rows matches the board
        if len(known_rows) != board.rows:
            errors.append(
                f"Number of rows in 'Known' ({len(known_rows)}) "
                f"does not match the board's row count ({board.rows})."
            )

        # Validate each row and its columns
        for row_idx, row in enumerate(known_rows):
            # Check the number of columns matches the board
            errors.extend(KnownValidator.validate_row(allowed_characters, row, row_idx, board))

        return errors
