"""PillValidator."""
from src.items.board import Board
from src.validators.cell_validator import CellValidator
from src.validators.line_validator import LineValidator


class PillValidator(LineValidator):
    """Validates a sequence of cells forming a 'pill' shape on the board.

    A 'pill' is a sequence of cells that are:
        - Located in the same row.
        - Unique (no repeated cells).
        - Connected horizontally.

    Inherits:
        LineValidator: The base class that provides line validation for cells.
    """

    @staticmethod
    def validate(board: Board, data: dict) -> list[str]:
        """Validate that all cells in the sequence form a valid 'pill'.

        The validation checks that:
        - All cells are in the same row.
        - All cells are unique.
        - Cells are connected horizontally (i.e., adjacent cells in the sequence).

        Args:
            board (Board): The board on which the validation is performed.
            data (dict): A list of dictionaries containing cell coordinates to validate.

        Returns:
            list[str]: A list of error messages. An empty list if validation passes.
        """
        # Start by validating line-based constraints
        errors: list[str] = LineValidator.validate(board, data)
        # Validate horizontal connectivity using CellValidator's method
        for index in range(len(data) - 1):
            start = data[index]
            finish = data[index + 1]
            errors.extend(CellValidator.validate_horizontal_connectivity(start, finish))

        return errors
