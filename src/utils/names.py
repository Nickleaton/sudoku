import re


class Name(object):

    @staticmethod
    def camel_to_snake(name: str) -> str:
        """Convert CamelCase to snake_case."""
        return re.sub(r'(?<!^)(?=[A-Z])', '_', name).lower()

    @staticmethod
    def snake_to_camel(name: str) -> str:
        """Convert snake_case to CamelCase."""
        return ''.join(word.capitalize() for word in name.split('_'))
