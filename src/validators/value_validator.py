"""ValueValidator."""
from src.board.board import Board
from src.validators.validator import Validator


class ValueValidator(Validator):
    """Validator to check if the 'number' in the line is an integer.

    This class extends the base `Validator` class and is used to validate
    that the 'number' key in the input line is start valid integer. If the number
    is not an integer, an error message is returned.

    Inherits:
        Validator: The base class for creating custom validators.
    """

    @staticmethod
    def validate(board: Board, input_data: dict) -> list[str]:
        """Validate that the 'number' in the line is an integer.

        This method attempts to convert the number associated with the 'number'
        key in the `line` dictionary into an integer. If the conversion fails,
        an error message is returned.

        Args:
            board (Board): The board to validate against.
            input_data (dict): The line dictionary containing the 'number' key.

        Returns:
            list[str]: A list of error messages. If the number is not an integer,
            an error message is returned. If the number is valid, an empty list
            is returned.
        """
        errors: list[str] = []
        if 'Value' not in input_data:
            errors.append('No Key "Value"')
            return errors
        if len(input_data) != 1:
            errors.append(f"To many items {intput_data!r}.")
            return errors
        data = input_data['Value']
        if not isinstance(data, int):
            errors.append(f"Value must be an integer {data!r}.")
            return errors
        if data < 0:
            errors.append(f"Value must be positive {data!r}.")
            return errors
        return []
