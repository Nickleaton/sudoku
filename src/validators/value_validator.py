"""ValueValidator."""
from src.board.board import Board
from src.validators.validator import Validator


class ValueValidator(Validator):
    """Validator to check if the 'Value' in the input data is a valid integer.

    This class extends the base `Validator` class and is used to validate
    that the 'Value' key in the input data contains a positive integer.

    Inherits:
        Validator: The base class for creating custom validators.
    """

    @staticmethod
    def validate(board: Board, input_data: dict | list) -> list[str]:
        """Validate that the 'Value' in the input data is a positive integer.

        Args:
            board (Board): The board to validate against (not used in this validator).
            input_data (dict | list): A dictionary containing the key 'Value' to validate.

        Returns:
            list[str]: A list of error messages. If the 'Value' is missing, not an integer,
            or negative, appropriate error messages are returned. Otherwise, an empty list.
        """
        errors: list[str] = Validator.pre_validate(input_data, required_keys={'Value': int})
        if errors:
            return errors
        data_value = dict(input_data)['Value']
        if not isinstance(data_value, int):
            return [f'Value must be an integer, got {type(data_value).__name__}: {data_value!r}.']
        if data_value < 0:
            return [f'Value must be a positive integer, got {data_value!r}.']
        return []
