"""NoneValidator."""
from strictyaml import Validator


class NoneValidator(Validator):
    """Validator to ensure that the data is None.

    This validator checks that the provided data is None and returns
    an error message if the data is not None.

    Attributes:
        None
    """

    @staticmethod
    def validate(data: dict) -> list[str]:
        """Validate that the data is None.

        Args:
            data (dict): The data to validate.

        Returns:
            list[str]: A list of error messages. An empty list indicates
            that the validation was successful (data is None), while a
            list with an error message is returned if data is not None.
        """
        if data:
            return [f"Expecting None, got {data!r}"]
        return []
