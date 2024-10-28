from typing import List, Dict, Optional

from src.items.board import Board
from src.items.constraints import Constraints
from src.items.item import Item
from src.items.solution import Solution


class Puzzle(Item):
    def __init__(self, board: Board, solution: Optional[Solution] = None, constraints: Optional[Constraints] = None):
        super().__init__(board)
        self.solution: Solution = solution
        self.constraints: List[Item] = constraints if constraints is not None else []

    @classmethod
    def create(cls, board: Board, yaml: Dict) -> Item:
        board: Board = Board.create('Board', yaml)
        solution: Optional[Solution] = Solution.create(
            board,
            yaml['Solution']
        ) if 'Solution' in yaml else None
        constraints: Optional[Constraints] = Constraints.create(
            board,
            yaml['Constraints']
        ) if 'Constraints' in yaml else None
        return Puzzle(board, solution, constraints)

    def __repr__(self) -> str:
        return f"Puzzle(board={self.board}, solution={self.solution}, constraints={self.constraints})"