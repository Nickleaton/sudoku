"""NoneValidator."""
from strictyaml import Validator

from src.board.board import Board


class NoneValidator(Validator):
    """Validator to ensure that the line is None.

    This validator checks that the provided line is None and returns
    an error message if the line is not None.

    Attributes:
        None
    """

    @staticmethod
    def validate(board: Board, input_data: dict | list) -> list:
        """Run all validations on start single cell.

        This method checks if the cell has valid keys and if it is within the board's range.

        Args:
            board (Board): The board on which the validation is performed.
            input_data (dict): The dictionary representing the cell, which must contain ROW and COL keys.

        Returns:
            list[str]: A list of error messages. An empty list if validation passes.
        """
        errors: list[str] = []
        if len(input_data) != 1:
            errors.append(f'Expecting 1 key, got {len(input_data)} keys.')
            return errors
        _, data_value = list(input_data.items())[0]
        if data_value is not None:
            errors.append(f'Data must be None, got {data_value!r}.')
            return errors
        return []
