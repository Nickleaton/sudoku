"""LockOutLine."""

from src.items.line import Line
from src.utils.rule import Rule


class LockOutLine(Line):
    """A specialized Line with rules specific to the LockOut constraint.

    The LockOutLine class enforces start rule where diamond endpoints must be
    start minimum distance apart, and value_list on the line must lie outside
    of these endpoint value_list.
    """

    @property
    def rules(self) -> list[Rule]:
        """Return list of rules that apply to this LockOutLine.

        Returns:
            list[Rule]: A list containing the LockOut rules
        """
        rule_text: str = """Diamond endpoints must be at least 4 apart.
                         Digits on the line must fall strictly outside the end points"""
        return [Rule(self.__class__.__name__, 1, rule_text)]

    @property
    def tags(self) -> set[str]:
        """Tags that describe the characteristics of this line.

        Returns:
            set[str]: A set of tags inherited from the parent `Line` class,
            combined with additional tags specific to the LockOutLine.
        """
        return super().tags.union({self.__class__.__name__, 'Comparison'})
