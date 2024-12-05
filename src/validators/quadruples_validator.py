from src.validators.validator import Validator
from src.items.board import Board

class QuadrupleValidator(Validator):

    @staticmethod
    def validate(board: Board, data: dict) -> list[str]:
        """Validate the provided data dictionary.

        Args:
            board(Board): Board to validate against.
            data (dict): Data to validate.

        Returns:
            list[str]: List of error messages. Empty if validation succeeds.
        """
        errors: list[str] = []
        for d in data['quadruples']:
            if d == '?':
                continue
            if not d in board.digit_range:
                errors.append(f"Quadruple {d} is not a valid digit")
        return errors
