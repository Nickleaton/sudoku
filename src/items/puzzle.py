from typing import Dict, Optional

from src.items.board import Board
from src.items.constraints import Constraints
from src.items.item import Item
from src.items.solution import Solution


class Puzzle(Item):
    """Represents a puzzle that includes a board, solution, and constraints."""

    def __init__(self, board: Board, solution: Optional[Solution] = None, constraints: Optional[Constraints] = None):
        """Initializes a Puzzle instance with a board, optional solution, and optional constraints.

        Args:
            board (Board): The puzzle's board.
            solution (Optional[Solution], optional): The solution to the puzzle, if available. Defaults to None.
            constraints (Optional[Constraints], optional): Constraints applied to the puzzle, if any. Defaults to None.
        """
        super().__init__(board)
        self.solution: Optional[Solution] = solution  # Change to Optional[Solution]
        self.constraints: Optional[Constraints] = constraints

    @classmethod
    def create(cls, board: Board, yaml: Dict) -> 'Puzzle':  # Use 'Puzzle' instead of Item
        """Creates a Puzzle instance from a YAML configuration.

        Args:
            board (Board): The board for the puzzle.
            yaml (Dict): A dictionary containing the YAML configuration for the puzzle.

        Returns:
            Puzzle: An instance of `Puzzle` populated with the given configuration.
        """
        parsed_board: Board = Board.create('Board', yaml)  # Change variable name to avoid redeclaration
        solution: Optional[Solution] = Solution.create(
            parsed_board,
            yaml['Solution']
        ) if 'Solution' in yaml else None
        constraints: Optional[Constraints] = Constraints.create(
            parsed_board,
            yaml['Constraints']
        ) if 'Constraints' in yaml else None
        return Puzzle(parsed_board, solution, constraints)  # Pass the parsed_board

    def __repr__(self) -> str:
        """Provides a string representation of the Puzzle instance.

        Returns:
            str: A string representing the puzzle's board, solution, and constraints.
        """
        return f"Puzzle(board={self.board}, solution={self.solution}, constraints={self.constraints})"
