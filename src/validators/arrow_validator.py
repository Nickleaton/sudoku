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
    def validate(board: Board, input_data: dict | list) -> list[str]:
        """Validate that all cells in the sequence are valid, connected, and unique.

        Args:
            board (Board): The board on which the validation is performed.
            input_data (dict): A dictionary containing the constraint line to be validated.

        Returns:
            list[str]: A list of error messages. An empty list if validation passes, otherwise a list of errors.
        """
        errors: list[str] = Validator.pre_validate(input_data, {SHAFT: dict, PILL: dict})
        if errors:
            return errors
        pill: list[dict] = dict(input_data)[PILL]
        shaft: list[dict] = dict(input_data)[SHAFT]
        errors.extend(LineValidator.validate_cells(board, pill))
        errors.extend(PillValidator.validate(board, pill))
        errors.extend(LineValidator.validate_cells(board, shaft))
        errors.extend(LineValidator.validate_unique(pill + shaft))
        return errors
