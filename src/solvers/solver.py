from src.items.board import Board


class Solver:

    def __init__(self, board: Board):
        self.board = board
        self._count = 1

    def save(self, filename: str) -> None:
        pass

    def solve(self) -> None:
        pass

    @property
    def count(self) -> int:
        return self._count

    def increment(self) -> None:
        self._count += 1
