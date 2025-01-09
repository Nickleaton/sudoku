"""LineValidator."""
from src.board.board import Board
from src.validators.line_validator import LineValidator
from src.validators.validator import Validator


class LinesValidator(Validator):
    """Validator for repeats of arrows.

    Inherits:
        Validator: The base class for creating custom validators.
    """

    @staticmethod
    def validate(board: Board, input_data: dict | list) -> list:
        """Validate that all cells in the sequence are valid, connected, and unique.

        Args:
            board (Board): The board on which the validation is performed.
            input_data (dict | list): A dictionary containing the constraint line to be validated.

        Returns:
            list[str]: A list of error messages. An empty list if validation passes, otherwise a list of errors.
        """
        errors: list[str] = Validator.pre_validate(input_data, required_keys=None)
        lines: list = list(input_data.values())
        for arrow in lines:
            errors.extend(LineValidator.validate(board, arrow))
        return errors
