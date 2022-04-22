from typing import List, Any

from src.items.board import Board
from src.items.item import Item, YAML
from src.items.standard_region import StandardRegion
from src.utils.rule import Rule


class Indexer(StandardRegion):

    @property
    def name(self) -> str:
        return f"{self.__class__.__name__}_{self.index}"

    @staticmethod
    def validate(board: Board, yaml: Any) -> List[str]:
        error = f"Expecting Indexer: index, got {yaml!r}"
        if not isinstance(yaml, dict):
            return [error]
        if len(yaml) != 1:
            return [error]
        for k, v in yaml.items():
            if k != 'Indexer':
                return [error]
            if not isinstance(v, int):
                return [error]
            if v not in board.row_range:
                return [error]
        return []

    @staticmethod
    def extract(_: Board, yaml: Any) -> int:
        return int(yaml)

    @classmethod
    def create(cls, name: str, board: Board, yaml: YAML) -> Item:
        cls.validate(board, yaml)
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
