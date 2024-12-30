"""ValueValidator."""
from src.board.board import Board
from src.validators.validator import Validator


class ValueValidator(Validator):
    """Validator to check if the 'number' in the input_data is an integer.

    This class extends the base `Validator` class and is used to validate
    that the 'number' key in the input input_data is start valid integer. If the number
    is not an integer, an error message is returned.

    Inherits:
        Validator: The base class for creating custom validators.
    """

    @staticmethod
    def validate(board: Board, input_data: dict) -> list[str]:
        """Validate that the 'number' in the input_data is an integer.

        This method attempts to convert the number associated with the 'number'
        key in the `input_data` dictionary into an integer. If the conversion fails,
        an error message is returned.

        Args:
            board (Board): The board to validate against.
            input_data (dict): The input_data dictionary containing the 'number' key.

        Returns:
            list[str]: A list of error messages. If the number is not an integer,
            an error message is returned. If the number is valid, an empty list
            is returned.
        """
        try:
            int(input_data['number'])
        except ValueError:
            return ['Value must be an integer']
        return []
