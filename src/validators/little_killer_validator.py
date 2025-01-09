"""LittleKillerValidator."""

from src.board.board import Board
from src.validators.cyclic_validator import CyclicValidator
from src.validators.side_validator import SideValidator
from src.validators.validator import Validator
from src.validators.value_validator import ValueValidator


class LittleKillerValidator(Validator):
    """Validator for the Little Killer Sudoku constraints."""

    @staticmethod
    def validate(board: Board, input_data: dict | list) -> list:
        """Validate the Little Killer constraint line.

        Args:
            board (Board): The Sudoku board that the constraint applies to.
            input_data (dict[str, str]): A dictionary containing the constraint line to be validated.

        Returns:
            list[str]: A list of error messages, or an empty list if the line is valid.
                Each string in the list corresponds to a specific validation failure.
        """
        required_keys: dict[str, type | tuple[type, ...]] = {'Side': str, 'Cyclic': str, 'Value': int, 'Index': int}
        errors: list[str] = Validator.pre_validate(input_data, required_keys)
        if errors:
            return errors
        values = dict(input_data)
        errors.extend(SideValidator.validate(board, {'Side': values['Side']}))
        errors.extend(CyclicValidator.validate(board, {'Cyclic': values['Cyclic']}))
        errors.extend(ValueValidator.validate(board, {'Value': values['Value']}))
        index: int = values['Index']
        side: str = values['Side']
        max_index = board.board_rows + 1 if side in {'T', 'B'} else board.board_columns + 1
        if index < 0 or index > max_index:
            errors.append(f"Invalid index: {index}. Must be between 0 and {max_index} for side {side!r}.")
        return errors
