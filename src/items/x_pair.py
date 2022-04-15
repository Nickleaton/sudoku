from src.items.sum_pair import SumPair


class XPair(SumPair):

    @property
    def total(self) -> int:
        return 10

    @property
    def tags(self) -> set[str]:
        return super().tags.union({'X'})

    @property
    def label(self) -> str:
        return "X"
