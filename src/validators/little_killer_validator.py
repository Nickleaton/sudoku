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
        errors: list[str] = []

        if len(input_data) != 4:
            errors.append(f"To few items {input_data!r}. Expecting 4")
        if 'Side' not in input_data:
            errors.append(f"Missing key: {input_data!r}.")
        if 'Cyclic' not in input_data:
            errors.append(f"Missing key: {input_data!r}.")
        if 'Value' not in input_data:
            errors.append(f"Missing key: {input_data!r}.")
        if 'Index' not in input_data:
            errors.append(f"Missing key: {input_data!r}.")
        if len(errors) > 0:
            return errors
        errors.extend(LittleKillerValidator.side_validator.validate(board, {'Side': input_data['Side']}))
        errors.extend(LittleKillerValidator.cyclic_validator.validate(board, {'Cyclic': input_data['Cyclic']}))
        errors.extend(LittleKillerValidator.value_validator.validate(board, {'Value': input_data['Value']}))
        if len(errors) > 0:
            return errors
        if not isinstance(input_data['Index'], int):
            errors.append(f"Index must be an integer {input_data['Index']}")
            return errors
        index: int = int(input_data['Index'])
        if input_data['Side'] in ['T', 'B']:
            if index < 0 or index > board.board_rows + 1:
                errors.append(f"Invalid index: {input_data['Index']}")
        else:
            if index < 0 or index > board.board_columns + 1:
                errors.append(f"Invalid index: {input_data['Index']}")
        return errors
