from typing import List, Dict

from src.items.board import Board
from src.items.item import Item
from src.items.standard_region import StandardRegion
from src.utils.rule import Rule


class Indexer(StandardRegion):

    @classmethod
    def extract(cls, board: Board, yaml: Dict) -> int:
        return int(yaml[cls.__name__])

    @classmethod
    def create(cls, board: Board, yaml: Dict) -> Item:
        index = cls.extract(board, yaml)
        return cls(board, index)

    @staticmethod
    def variant() -> str:
        return ""

    @staticmethod
    def other_variant() -> str:
        return ""

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.board!r}, {self.index!r})"

    @property
    def rules(self) -> List[Rule]:
        return [
            Rule(
                f'{self.__class__.__name__}{self.index}',
                1,
                (
                    f"Digits in {self.variant()} {self.index} indicate the {self.variant()} "
                    f"in which the digit {self.index} appears in that {self.other_variant()}"
                )
            )
        ]

    @property
    def tags(self) -> set[str]:
        return super().tags.union({'Indexing'})
