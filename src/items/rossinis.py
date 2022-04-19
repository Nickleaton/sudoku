from typing import Sequence, Dict, List

from src.items.board import Board
from src.items.composed import Composed
from src.items.constraint_exception import ConstraintException
from src.items.item import Item
from src.items.rossini import Rossini


class Rossinis(Composed):
    """ Collection of Rossini """

    def __init__(self, board: Board, rossinis: Sequence[Rossini]):
        super().__init__(board, rossinis)

    @classmethod
    def create(cls, name: str, board: Board, yaml: Dict | List | str | int | None) -> Item:
        if not isinstance(yaml, list):
            raise ConstraintException(f"Expecting list, got {yaml!r}")
        return cls(board, [Rossini.create('Rossini', board, y) for y in yaml])
