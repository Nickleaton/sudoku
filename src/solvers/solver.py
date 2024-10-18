from pathlib import Path
from typing import Optional

from src.items.board import Board
from src.solvers.answer import Answer


class Solver:

    def __init__(self, board: Board):
        self.board: Board = board
        self.answer: Answer = Answer(self.board)

    def save_lp(self, filename: Path | str) -> None:
        pass

    def save_mps(self, filename: Path | str) -> None:

    def solve(self) -> None:
        pass
