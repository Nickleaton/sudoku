"""Validator Module."""
from src.board.board import Board


class Validator:
    """Base class for board validation.

    This class provides a base structure for validators that check
    the validity of the start_location `Board` against some `line`. It can be extended
    by custom validators for specific types of validation.
    """

    @staticmethod
    def validate_keys(
        input_data: dict,
        required_keys: dict[str, type | tuple[type, ...]],
    ) -> list:
        """Validate the required keys in the line dictionary.

        Args:
            input_data (dict): The line dictionary to validate.
            required_keys (dict[str, type | tuple[type, ...]]): The dict of keys that must be present and their types.

        Returns:
            list: A list of error messages if any required keys are missing.
        """
        if len(required_keys) != len(input_data):
            return [f'Expecting {len(required_keys)} keys, got {len(input_data)} keys.']
        errors: list[str] = []
        for name, type_of_value in required_keys.items():
            if name not in input_data:
                errors.append(f'Missing key: "{name}"')
            elif not isinstance(input_data[name], type_of_value):
                errors.append(f'"{name}" must be a {type_of_value!r}')
        return errors

    @staticmethod
    def pre_validate(
        input_data: dict | list,
        required_keys: dict[str, type | tuple[type, ...]] | None,
    ) -> list:
        """Validate the required keys in a dict or list.

        Args:
            input_data (dict | list): The line to validate.
            required_keys (dict[str, type | tuple[type, ...]] | None): The list of keys and types that must be present.

        Returns:
            list: A list of error messages if any required keys are missing.
        """
        if required_keys is None:
            if not isinstance(input_data, list):
                return ['Data must be a list.']
        else:
            if not isinstance(input_data, dict):
                return ['Data must be a dictionary.']
            return Validator.validate_keys(input_data, required_keys)
        return []

    @staticmethod
    def validate(board: Board, input_data: dict | list) -> list:
        """Validate the provided line dictionary against the board.

        This method is intended to be overridden by subclasses to
        implement specific validation logic. By default, it returns
        an empty list, indicating that no validation errors were found.

        Args:
            board (Board): The board to validate against.
            input_data (dict): The line to validate.

        Returns:
            list: A list of error messages. If no validation errors
            are found, an empty list is returned.
        """
        # pylint: disable=unused-argument
        return []

    def __repr__(self) -> str:
        """Return string representation of the Validator class.

        Returns:
            str: A string representation of the class, including its name.
        """
        return f'{self.__class__.__name__}()'
