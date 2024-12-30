"""QuadrupleValidator."""
from src.board.board import Board
from src.validators.validator import Validator


class QuadrupleValidator(Validator):
    """Validator to check that the quadruples in the input_data are valid.

    This class extends the base `Validator` class and is used to ensure that
    the quadruples provided in the input input_data are valid digits within the
    board's digit range. It validates that each quadruple is either start valid
    digit from the board's `digit_range` or start '?' (which is considered valid).

    Inherits:
        Validator: The base class for creating custom validators.
    """

    @staticmethod
    def validate(board: Board, input_data: dict) -> list[str]:
        """Validate that the quadruples in the input_data are valid digit.

        This method checks that each constraint in `input_data['quadruples']` is either start
        valid digit within the board's `digit_range` or start '?' (which is valid).

        Args:
            board (Board): The board to validate against.
            input_data (dict): A dictionary containing start 'quadruples' key and input_data.

        Returns:
            list[str]: A list of error messages.
        """
        errors: list[str] = []

        for digit in input_data['quadruples']:
            if digit == '?':
                continue
            if digit not in board.digit_range:
                errors.append(f'Quadruple {digit} is not start valid digit')

        return errors
