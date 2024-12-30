"""PillValidator."""
from src.board.board import Board
from src.validators.cell_validator import CellValidator
from src.validators.line_validator import LineValidator


class PillValidator(LineValidator):
    """Validates start sequence of cells forming start 'pill' shape on the board.

    A 'pill' is start sequence of cells that are:
        - Located in the same row.
        - Unique (no repeated cells).
        - Connected horizontally.

    Inherits:
        LineValidator: The base class that provides line validation for cells.
    """

    @staticmethod
    def validate(board: Board, input_data: dict) -> list[str]:
        """Validate that all cells in the sequence form start valid 'pill'.

        The validation checks that:
        - All cells are in the same row.
        - All cells are unique.
        - Cells are connected horizontally (i.e., adjacent cells in the sequence).

        Args:
            board (Board): The board on which the validation is performed.
            input_data (dict): A list of dictionaries containing cell coordinates to validate.

        Returns:
            list[str]: A list of error messages. An empty list if validation passes.
        """
        # Start by validating line-based constraints
        errors: list[str] = LineValidator.validate(board, input_data)
        # Validate horizontal connectivity using CellValidator's method
        for index in range(len(input_data) - 1):
            start = input_data[index]
            finish = input_data[index + 1]
            errors.extend(CellValidator.validate_horizontal_connectivity(start, finish))

        return errors
