from typing import List

from src.items.pair import Pair
from src.utils.rule import Rule


class DifferencePair(Pair):

    @property
    def difference(self) -> int:
        return 0

    @property
    def rules(self) -> List[Rule]:
        return []

    @property
    def tags(self) -> set[str]:
        return super().tags.union({'Difference'})
