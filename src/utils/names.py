"""Utility functions to convert between camel and snake case."""
import re


class Name:
    """A utility class for converting strings between camelCase and snake_case."""

    @staticmethod
    def camel_to_snake(name: str) -> str:
        """
        Convert a camelCase string to snake_case.

        Args:
            name (str): The camelCase string to convert.

        Returns:
            str: The converted snake_case string.
        """
        return re.sub(r'(?<!^)(?=[A-Z])', '_', name).lower()

    @staticmethod
    def snake_to_camel(name: str) -> str:
        """
        Convert a snake_case string to camelCase.

        Args:
            name (str): The snake_case string to convert.

        Returns:
            str: The converted camelCase string.
        """
        return ''.join(word.capitalize() for word in name.split('_'))
