"""NoneValidator."""
from strictyaml import Validator

from src.board.board import Board


class NoneValidator(Validator):
    """Validator to ensure that the input_data is None.

    This validator checks that the provided input_data is None and returns
    an error message if the input_data is not None.

    Attributes:
        None
    """

    @staticmethod
    def validate(board: Board, input_data: dict) -> list[str]:
        """Run all validations on start single cell.

        This method checks if the cell has valid keys and if it is within the board's range.

        Args:
            board (Board): The board on which the validation is performed.
            input_data (dict): The dictionary representing the cell, which must contain ROW and COL keys.

        Returns:
            list[str]: A list of error messages. An empty list if validation passes.
        """
        if input_data:
            return [f'Expecting None, got {input_data!r}']
        return []
