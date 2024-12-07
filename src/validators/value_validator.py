"""ValueValidator."""
from src.items.board import Board
from src.validators.validator import Validator


class ValueValidator(Validator):
    """Validator to check if the 'value' in the data is an integer.

    This class extends the base `Validator` class and is used to validate
    that the 'value' key in the input data is a valid integer. If the value
    is not an integer, an error message is returned.

    Inherits:
        Validator: The base class for creating custom validators.
    """

    @staticmethod
    def validate(board: Board, data: dict) -> list[str]:
        """Validate that the 'value' in the data is an integer.

        This method attempts to convert the value associated with the 'value'
        key in the `data` dictionary into an integer. If the conversion fails,
        an error message is returned.

        Args:
            board (Board): The board to validate against.
            data (dict): The data dictionary containing the 'value' key.

        Returns:
            list[str]: A list of error messages. If the value is not an integer,
            an error message is returned. If the value is valid, an empty list
            is returned.
        """
        try:
            int(data['value'])
        except ValueError:
            return ["Value must be an integer"]
        return []
