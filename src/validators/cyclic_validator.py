"""CyclicValidator."""

from src.board.board import Board
from src.utils.cyclic import Cyclic
from src.validators.validator import Validator


class CyclicValidator(Validator):
    """Validator for a Cyclic."""

    @staticmethod
    def validate(board: Board, input_data: dict | list) -> list[str]:
        """Validate a Cyclic.

        Args:
            board (Board): The Sudoku board that the constraint applies to.
            input_data (dict[str, str]): A dictionary containing the constraint line to be validated.

        Returns:
            list[str]: A list of error messages, or an empty list if the line is valid.
                Each string in the list corresponds to a specific validation failure.
        """
        errors: list[str] = Validator.pre_validate(input_data, {'Cyclic': str})
        if errors:
            return errors
        cyclic_value: str = dict(input_data)['Cyclic']
        if cyclic_value not in {member.value for member in Cyclic}:
            return [f'Value must be a Cyclic {cyclic_value!r}.']
        return []
