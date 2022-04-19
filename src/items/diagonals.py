from typing import List, Dict, Any

from src.items.board import Board
from src.items.item import Item
from src.items.region import Region
from src.utils.rule import Rule


class Diagonal(Region):

    @staticmethod
    def validate(board: Board, yaml: Any) -> List[str]:
        result = []
        if not isinstance(yaml, dict):
            result.append(f"Expecting a dict got, {yaml!r}")
            return result
        if len(yaml) != 1:
            result.append(f"Expecting one item got, {yaml!r}")
        for k, v in yaml.items():
            if k != 'Diagonal':
                result.append(f"Expecting Diagonal, got {yaml!r}")
            if v is not None:
                result.append(f"Expecting Diagonal with no values, got {yaml!r}")
        return result

    @classmethod
    def create(cls, name: str, board: Board, yaml: Dict | List | str | int | None) -> Item:
        cls.validate(board, yaml)
        return cls(board)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.board!r})"

    @property
    def rules(self) -> List[Rule]:
        return [Rule('Diagonal', 1, "Digits along a blue diagonal cannot repeat")]

    @property
    def tags(self) -> set[str]:
        return super().tags.union({'Diagonal', 'Uniqueness'})
