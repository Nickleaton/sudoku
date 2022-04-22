from typing import Sequence

from src.items.board import Board
from src.items.composed import Composed
from src.items.constraint_exception import ConstraintException
from src.items.item import Item, YAML
from src.items.outside import Outside


class Outsides(Composed):
    """ Collection of Outside """

    def __init__(self, board: Board, outsides: Sequence[Item]):
        super().__init__(board, outsides)

    @classmethod
    def create(cls, name: str, board: Board, yaml: YAML) -> Item:
        if not isinstance(yaml, list):
            raise ConstraintException(f"Expecting list, got {yaml!r}")
        return cls(board, [Outside.create('Outside', board, y) for y in yaml])
