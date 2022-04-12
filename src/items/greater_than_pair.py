from typing import List

from src.items.pair import Pair
from src.utils.rule import Rule


class GreaterThanPair(Pair):

    @property
    def rules(self) -> List[Rule]:
        return [
            Rule(
                "GreaterThanPair",
                1,
                (
                    "Where cells are separated by chevron "
                    "the arrow points at the smaller digit"
                )
            )
        ]

    @property
    def tags(self) -> set[str]:
        return super().tags.union({'Comparison'})
