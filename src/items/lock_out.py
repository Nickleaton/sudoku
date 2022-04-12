from typing import List

from src.items.line import Line
from src.utils.rule import Rule


class LockOut(Line):

    @property
    def rules(self) -> List[Rule]:
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
        return super().tags.union({'LockOut', 'Comparison'})
