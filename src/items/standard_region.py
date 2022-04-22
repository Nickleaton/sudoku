from typing import List, Any

from src.glyphs.glyph import Glyph
from src.items.board import Board
from src.items.item import Item, YAML
from src.items.region import Region


class StandardRegion(Region):

    def __init__(self, board: Board, index: int):
        super().__init__(board)
        self.index = index

    @property
    def name(self) -> str:
        return f"{self.__class__.__name__}_{self.index}"

    @property
    def glyphs(self) -> List[Glyph]:
        return []

    @staticmethod
    def validate(board: Board, yaml: Any) -> List[str]:
        results = []
        if not isinstance(yaml, int):
            results.append(f"Expecting int, got {yaml!r}")
            return results
        return results

    @staticmethod
    def extract(_: Board, yaml: Any) -> int:
        return int(yaml)

    @classmethod
    def create(cls, name: str, board: Board, yaml: YAML) -> Item:
        StandardRegion.validate(board, yaml)
        index = StandardRegion.extract(board, yaml)
        return cls(board, index)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.board!r}, {self.index!r})"

    @property
    def tags(self) -> set[str]:
        return super().tags.union({'Uniqueness', 'Standard Set'})
