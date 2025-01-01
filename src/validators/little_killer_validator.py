"""LittleKillerValidator."""

from src.board.board import Board
from src.validators.validator import Validator
from src.validators.value_validator import ValueValidator


class LittleKillerValidator(Validator):
    """Validator for the Little Killer Sudoku constraints."""

    required_keys: tuple[str, str, str, str] = ('side', 'index', 'direction', 'number')

    @staticmethod
    def validate(board: Board, input_data: dict[str, str]) -> list[str]:
        """Validate the Little Killer constraint input_data.

        This method performs several checks:
        1. It checks if all required keys are present in the `input_data` dictionary.
        2. It validates that the `index` is within the valid range for the board.
        3. It delegates digit validation to the `ValueValidator`.

        Args:
            board (Board): The Sudoku board that the constraint applies to.
            input_data (dict[str, str]): A dictionary containing the constraint input_data to be validated.

        Returns:
            list[str]: A list of error messages, or an empty list if the input_data is valid.
                Each string in the list corresponds to a specific validation failure.
        """
        errors: list[str] = []

        # Validate required keys in the input_data
        errors.extend(LittleKillerValidator.validate_keys(input_data, LittleKillerValidator.required_keys))
        if errors:
            return errors

        # Validate the 'index' field to ensure it's within the valid range
        index = int(input_data['index'])
        if index < 0 or index > board.rows + 1:
            errors.append(f"Invalid index: {input_data['index']}")

        # Use the ValueValidator to validate the cell_values in the input_data
        errors.extend(ValueValidator().validate(board, input_data))
        return errors
