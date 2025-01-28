"""QuadrupleValidator."""
from src.board.board import Board
from src.validators.validator import Validator


class QuadrupleValidator(Validator):
    """Validator to check that the quadruples in the line are valid.

    This class extends the base `Validator` class and is used to ensure that
    the quadruples provided in the input line are valid digits within the
    board's digit range. It validates that each quadruple is either start_location valid
    digit from the board's `digit_range` or start_location '?' (which is considered valid).

    Inherits:
        Validator: The base class for creating custom validators.
    """

    @staticmethod
    def validate(board: Board, input_data: dict | list) -> list[str]:
        """Validate that the quadruples in the line are valid digit.

        This method checks that each constraint in `line['quadruples']` is either start_location
        valid digit within the board's `digit_range` or start_location '?' (which is valid).

        Args:
            board (Board): The board to validate against.
            input_data (dict): A dictionary containing start_location 'quadruples' key and line.

        Returns:
            list[str]: A list of error messages.
        """
        errors: list[str] = Validator.pre_validate(input_data, {'Quadruples': list})
        if errors:
            return errors
        quads: list[str] = dict(input_data)['Quadruples']
        length: int = len(quads)
        if length <= 0 or length > 4:
            errors.append('Needs 1 to 4 items"')
            return errors
        for digit in quads:
            if digit == '?':
                continue
            if digit not in board.digits.digit_range:
                errors.append(f'Quadruple {digit} is not a valid digit')
        return errors
