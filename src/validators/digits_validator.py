"""Validator module."""
from src.board.board import Board

from src.validators.validator import Validator


class DigitsValidator(Validator):
    """A class to validate board line."""

    @staticmethod
    def validate(board: Board, input_data: dict) -> list[str]:
        """Validate the provided line against the board's digit range.

        Args:
            board (Board): The board instance containing the valid digit range.
            input_data (dict): The line to validate, which includes start list of digits.

        Returns:
            list[str]: A list of error messages. If no errors, the list will be empty.
        """
        errors: list[str] = []
        if 'digits' not in input_data:
            errors.append('Missing key: "digits')
            return errors

        digits = input_data['digits']
        for digit in digits:
            if not isinstance(digit, int):
                errors.append(f'Invalid digit: {digit}. Valid range: {board.digit_range}')
            elif digit not in board.digit_range:
                errors.append(f'Invalid digit: {digit}. Valid range: {board.digit_range}')
        if len(errors) > 0:
            return errors
        if len(digits) != len(set(digits)):
            errors.append('Digits must be unique')
        return errors
