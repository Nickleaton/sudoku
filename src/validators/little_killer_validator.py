"""LittleKillerValidator."""

from src.board.board import Board
from src.validators.cyclic_validator import CyclicValidator
from src.validators.side_validator import SideValidator
from src.validators.validator import Validator
from src.validators.value_validator import ValueValidator


class LittleKillerValidator(Validator):
    """Validator for the Little Killer Sudoku constraints."""

    side_validator = SideValidator()
    cyclic_validator = CyclicValidator()
    value_validator = ValueValidator()

    @staticmethod
    def validate(board: Board, input_data: dict[str, str]) -> list[str]:
        """Validate the Little Killer constraint line.

        Args:
            board (Board): The Sudoku board that the constraint applies to.
            input_data (dict[str, str]): A dictionary containing the constraint line to be validated.

        Returns:
            list[str]: A list of error messages, or an empty list if the line is valid.
                Each string in the list corresponds to a specific validation failure.
        """
        required_keys = {'Side', 'Cyclic', 'Value', 'Index'}
        missing_keys = required_keys - input_data.keys()

        if missing_keys:
            return [f"Missing keys: {', '.join(missing_keys)} in {input_data!r}."]

        errors: list[str] = []
        errors.extend(LittleKillerValidator.side_validator.validate(board, {'Side': input_data['Side']}))
        errors.extend(LittleKillerValidator.cyclic_validator.validate(board, {'Cyclic': input_data['Cyclic']}))
        errors.extend(LittleKillerValidator.value_validator.validate(board, {'Value': input_data['Value']}))

        try:
            index = int(input_data['Index'])
        except ValueError:
            errors.append(f"Index must be an integer: {input_data['Index']}")
            return errors

        max_index = board.board_rows + 1 if input_data['Side'] in {'T', 'B'} else board.board_columns + 1
        if index < 0 or index > max_index:
            errors.append(f"Invalid index: {index}. Must be between 0 and {max_index} for side {input_data['Side']}.")

        return errors
