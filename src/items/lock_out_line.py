from typing import List

from src.items.line import Line
from src.utils.rule import Rule


class LockOutLine(Line):
    """A specialized Line with rules specific to the LockOut constraint.

    The LockOutLine class enforces a rule where diamond endpoints must be
    a minimum distance apart, and values on the line must lie outside
    of these endpoint values.
    """

    @property
    def rules(self) -> List[Rule]:
        """Return list of rules that apply to this LockOutLine.

        Returns:
            List[Rule]: A list containing the LockOut rules
        """
        return [
            Rule(
                'LockOut',
                1,
                (
                    "Diamond endpoints must be at least 4 apart. "
                    "Digits on the line must fall strictly outside the end points"
                )
            )
        ]

    @property
    def tags(self) -> set[str]:
        """Tags that describe the characteristics of this line.

        Returns:
            set[str]: A set of tags inherited from the parent `Line` class,
            combined with additional tags specific to the LockOutLine.
        """
        return super().tags.union({'LockOut', 'Comparison'})
