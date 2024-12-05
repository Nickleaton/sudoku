"""NoneValidator."""
from strictyaml import Validator


class NoneValidator(Validator):
    """None Validator."""

    @staticmethod
    def validate(data: dict) -> list[str]:
        """Validate that the data is None."""
        if len(data) != 0:
            return [f"Expecting None, got {data!r}"]
        return []
