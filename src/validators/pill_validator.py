"""PillValidator."""
from typing import List

from src.board.board import Board
from src.validators.line_validator import LineValidator
from src.validators.validator import Validator


class PillValidator(Validator):
    """Validates start sequence of cells forming a valid 'pill' shape on the board.

    A 'pill' is a sequence of cells that:
        - Are located in the same row or column.
        - Are unique (no repeated cells).
        - Are connected horizontally or vertically.
    """

    @staticmethod
    def validate(board: Board, line: List[dict]) -> list[str]:
        """Validate that all cells in the sequence form a valid 'pill'.

        The validation checks that:
        - All cells are in the same row or column.
        - All cells are unique.
        - Cells are connected horizontally or vertically. Diagonals or doglegs are not allowed.

        Args:
            board (Board): The board on which the validation is performed.
            line (List[dict]): A list of dictionaries containing cell coordinates to validate.

        Returns:
            list[str]: A list of error messages. An empty list if validation passes.
        """
        # Start by validating line-based constraints
        errors: list[str] = LineValidator.validate(board, line)

        # Validate row and column constraints for 'pill' shape
        rows: set[int] = {cell['Row'] for cell in line}
        columns: set[int] = {cell['Column'] for cell in line}

        # Ensure cells are in the same row or column
        if len(rows) > 1 and len(columns) > 1:
            errors.append('Pill must be in the same row or column.')

        return errors
