from src.validators.cell_validator import CellValidator
from src.validators.line_validator import LineValidator


class PillValidator(LineValidator):
    """Validates a sequence of cells forming a 'pill' on the board."""

    @staticmethod
    def validate(board: 'Board', data: list[dict]) -> list[str]:
        """Validate that all cells in the answer are valid, on the same row, unique, and connected horizontally.

        Args:
            board (Board): The board on which the validation is performed.
            data (list[dict]): A list of dictionaries containing cell coordinates to validate.

        Returns:
            list[str]: A list of error messages. Empty if validation passes.
        """

        errors: list[str] = LineValidator.validate(board, data)

        # Validate horizontal connectivity using CellValidator's method
        for i in range(len(data) - 1):
            errors.extend(CellValidator.validate_horizontal_connectivity(data[i], data[i + 1]))

        return errors
