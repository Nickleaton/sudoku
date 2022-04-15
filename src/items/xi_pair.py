from src.items.sum_pair import SumPair


class XIPair(SumPair):

    @property
    def total(self) -> int:
        return 11

    @property
    def tags(self) -> set[str]:
        return super().tags.union({'XI'})

    @property
    def label(self) -> str:
        return "XI"
