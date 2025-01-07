"""LineValidator."""
from src.board.board import Board
from src.validators.arrow_validator import ArrowValidator
from src.validators.validator import Validator


class ArrowsValidator(Validator):
    """Validator for repeats of arrows.

    Inherits:
        Validator: The base class for creating custom validators.
    """

    @staticmethod
    def validate(board: Board, input_data: dict) -> list[str]:
        """Validate that all cells in the sequence are valid, connected, and unique.

        Args:
            board (Board): The board on which the validation is performed.
            input_data (dict): A dictionary containing the constraint line to be validated.

        Returns:
            list[str]: A list of error messages. An empty list if validation passes, otherwise a list of errors.
        """
        errors: list[str] = []
        for arrow in next(iter(input_data.values())):
            errors.extend(ArrowValidator.validate(board, arrow))
        return errors
