"""QuadrupleValidator."""
from src.items.board import Board
from src.validators.validator import Validator


class QuadrupleValidator(Validator):
    """Validator to check that the quadruples in the data are valid.

    This class extends the base `Validator` class and is used to ensure that
    the quadruples provided in the input data are valid digits within the
    board's digit range. It validates that each quadruple is either a valid
    digit from the board's `digit_range` or a '?' (which is considered valid).

    Inherits:
        Validator: The base class for creating custom validators.
    """

    @staticmethod
    def validate(board: Board, data: dict) -> list[str]:
        """Validate that the quadruples in the data are valid digit.

        This method checks that each item in `data['quadruples']` is either a
        valid digit within the board's `digit_range` or a '?' (which is valid).

        Args:
            board (Board): The board to validate against.
            data (dict): A dictionary containing a 'quadruples' key and data.

        Returns:
            list[str]: A list of error messages.
        """
        errors: list[str] = []

        for digit in data['quadruples']:
            if digit == '?':
                continue
            if digit not in board.digit_range:
                errors.append(f"Quadruple {digit} is not a valid digit")

        return errors
