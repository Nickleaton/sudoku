"""PillValidator."""

from src.board.board import Board
from src.validators.cell_validator import ROW, COL  # noqa: I001
from src.validators.line_validator import LineValidator  # noqa: I005
from src.validators.validator import Validator  # noqa: I001


class PillValidator(Validator):
    """Validates start_location sequence of cells forming a valid 'pill' shape on the board.

    A 'pill' is a sequence of cells that:
        - Are located in the same row or column.
        - Are unique (no repeated cells).
        - Are connected horizontally or vertically.
    """

    @staticmethod
    def validate(board: Board, input_data: dict | list) -> list[str]:
        """Validate that all cells in the sequence form a valid 'pill'.

        The validation checks that:
        - All cells are in the same row or column.
        - All cells are unique.
        - Cells are connected horizontally or vertically. Diagonals or doglegs are not allowed.

        Args:
            board (Board): The board on which the validation is performed.
            input_data (dict | list): A list of dictionaries containing cell coordinates to validate.

        Returns:
            list[str]: A list of error messages. An empty list if validation passes.
        """
        # Start by validating line-based constraints
        errors: list[str] = Validator.pre_validate(input_data, required_keys=None)
        if errors:
            return errors

        line: list[dict[str, int]] = list(input_data)
        # Validate line-based constraints
        errors = LineValidator.validate(board, line)
        # Validate row and column constraints for 'pill' shape
        rows: set[int] = {cell[ROW] for cell in line}
        columns: set[int] = {cell[COL] for cell in line}

        # Ensure cells are in the same row or column
        if len(rows) > 1 and len(columns) > 1:
            errors.append('Pill must be in the same row or column.')

        return errors
