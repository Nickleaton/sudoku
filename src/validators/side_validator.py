"""SideValidator."""

from src.board.board import Board
from src.utils.side import Side
from src.validators.validator import Validator


class SideValidator(Validator):
    """Validator for a Side."""

    @staticmethod
    def validate(board: Board, input_data: dict | list) -> list[str]:
        """Validate a Side.

        Args:
            board (Board): The Sudoku board that the constraint applies to.
            input_data (dict[str, str]): A dictionary containing the constraint line to be validated.

        Returns:
            list[str]: A list of error messages, or an empty list if the line is valid.
                Each string in the list corresponds to a specific validation failure.
        """
        errors: list[str] = Validator.pre_validate(input_data, {'Side': str})
        if errors:
            return errors
        side: str = dict(input_data)['Side']
        if not isinstance(side, str):
            return [f'Value must be a string {input_data!r}.']
        if side not in {member.value for member in Side}:
            return [f'Value must be a Side {side!r}.']
        return []
