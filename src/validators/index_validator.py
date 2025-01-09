"""IndexValidator."""
from src.board.board import Board
from src.validators.validator import Validator


class IndexValidator(Validator):
    """Validator for the 'Index' key in input data."""

    @staticmethod
    def validate(board: Board, input_data: dict | list) -> list[str]:
        """Validate the 'Index' key in the input data.

        Args:
            board (Board): The Sudoku board that the constraint applies to.
            input_data (dict[str, object]): A dictionary containing the 'Index' key to validate.

        Returns:
            list[str]: A list of error messages, or an empty list if the input is valid.
        """
        errors: list[str] = Validator.pre_validate(input_data, {'Index': int})
        if errors:
            return errors
        index: str = dict(input_data)['Index']
        if not isinstance(index, int):
            return [f'Index must be a int {int!r}.']
        if index < 0:
            return [f'Index must be a non-negative int {index!r}.']
        return []
