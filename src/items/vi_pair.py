from src.items.sum_pair import SumPair


class VIPair(SumPair):

    @property
    def total(self) -> int:
        return 6

    @property
    def tags(self) -> set[str]:
        return super().tags.union({'VI'})

    @property
    def label(self) -> str:
        return "VI"
