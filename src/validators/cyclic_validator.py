"""CyclicValidator."""

from src.board.board import Board
from src.utils.cyclic import Cyclic
from src.validators.validator import Validator


class CyclicValidator(Validator):
    """Validator for a Cyclic."""

    @staticmethod
    def validate(board: Board, input_data: dict[str, str]) -> list[str]:
        """Validate a Cyclic.

        Args:
            board (Board): The Sudoku board that the constraint applies to.
            input_data (dict[str, str]): A dictionary containing the constraint line to be validated.

        Returns:
            list[str]: A list of error messages, or an empty list if the line is valid.
                Each string in the list corresponds to a specific validation failure.
        """
        errors: list[str] = []

        if len(input_data) != 1:
            errors.append(f'To many items {input_data!r}.')
            return errors
        if 'Cyclic' not in input_data:
            errors.append(f'Missing key: {input_data!r}.')
            return errors
        if not isinstance(input_data['Cyclic'], str):
            errors.append(f'Value must be a string {input_data!r}.')
            return errors
        if input_data['Cyclic'] not in {member.value for member in Cyclic}:
            errors.append(f'Value must be a Cyclic {input_data!r}.')
            return errors
        return []
