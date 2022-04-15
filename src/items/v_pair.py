from src.items.sum_pair import SumPair


class VPair(SumPair):

    @property
    def total(self) -> int:
        return 5

    @property
    def tags(self) -> set[str]:
        return super().tags.union({'V'})

    @property
    def label(self) -> str:
        return "V"
