"""LineValidator."""

from src.board.board import Board
from src.validators.line_validator import LineValidator
from src.validators.pill_validator import PillValidator
from src.validators.validator import Validator

PILL = 'Pill'
SHAFT = 'Shaft'


class ArrowValidator(Validator):
    """Validator for an arrow on the board.

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
        if not input_data:
            return ['The arrow cannot be empty.']
        errors: list[str] = []
        if PILL not in input_data:
            errors.append('The arrow must have a pill.')
        if SHAFT not in input_data:
            errors.append('The arrow must have a shaft.')
        if errors:
            return errors
        if input_data[PILL]:
            errors.append('The pill cannot be empty.')
        if input_data[SHAFT]:
            errors.append('The shaft cannot be empty.')
        errors.extend(PillValidator.validate_cells(board, input_data[PILL]))
        errors.extend(LineValidator.validate_cells(board, input_data[SHAFT]))
        errors.extend(LineValidator.validate_unique(input_data[PILL] + input_data[SHAFT]))
        return errors
