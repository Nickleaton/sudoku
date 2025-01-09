"""Validator module."""
from src.board.board import Board
from src.validators.validator import Validator


class DigitsValidator(Validator):
    """A class to validate board line."""

    @staticmethod
    def validate(board: Board, input_data: dict | list) -> list[str]:
        """Validate the provided line against the board's digit range.

        Args:
            board (Board): The board instance containing the valid digit range.
            input_data (dict | list): The line to validate, which includes a list of digits.

        Returns:
            list[str]: A list of error messages. If no errors, the list will be empty.
        """
        errors: list[str] = Validator.pre_validate(input_data, {'digits': list})
        if errors:
            return errors
        digits: list = dict(input_data)['digits']
        for digit in digits:
            if not isinstance(digit, int):
                error1: str = f'Invalid digit: {digit}. Valid range: {board.digit_range}'
                errors.append(error1)
            elif digit not in board.digit_range:
                error2: str = f'Invalid digit: {digit}. Valid range: {board.digit_range}'
                errors.append(error2)
        if errors:
            return errors
        if len(digits) != len(set(digits)):
            errors.append('Digits must be unique')
        return errors
