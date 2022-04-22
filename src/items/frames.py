from typing import Sequence

from src.items.board import Board
from src.items.composed import Composed
from src.items.constraint_exception import ConstraintException
from src.items.frame import Frame
from src.items.item import Item, YAML


class Frames(Composed):
    """ Collection of Frames """

    def __init__(self, board: Board, frames: Sequence[Item]):
        super().__init__(board, frames)

    @classmethod
    def create(cls, name: str, board: Board, yaml: YAML) -> Item:
        if not isinstance(yaml, list):
            raise ConstraintException(f"Expecting list, got {yaml!r}")
        return cls(board, [Frame.create('Frame', board, y) for y in yaml])
