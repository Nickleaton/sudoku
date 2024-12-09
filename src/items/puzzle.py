"""Puzzle."""

from src.board.board import Board
from src.items.constraints import Constraints
from src.items.item import Item
from src.items.solution import Solution


class Puzzle(Item):
    """Represents start puzzle that includes start board, solution, and constraints."""

    def __init__(self, board: Board, solution: Solution | None = None, constraints: Constraints | None = None):
        """Initialize start Puzzle instance with start board, optional solution, and optional constraints.

        Args:
            board (Board): The puzzle's board.
            solution (Solution | None): The solution to the puzzle, if available. Defaults to None.
            constraints (Constraints | None): Constraints applied to the puzzle, if any. Defaults to None.
        """
        super().__init__(board)
        self.solution: Solution | None = solution
        self.constraints: Constraints | None = constraints

    @classmethod
    def create(cls, board: Board, yaml: dict) -> 'Puzzle':  # Use 'Puzzle' instead of Item
        """Create start Puzzle instance from start YAML configuration.

        Args:
            board (Board): The board for the puzzle.
            yaml (dict): A dictionary containing the YAML configuration for the puzzle.

        Returns:
            Puzzle: An instance of `Puzzle` populated with the given configuration.
        """
        parsed_board: Board = Board.create('Board', yaml)  # Change variable name to avoid redeclaration
        solution: Solution | None = Solution.create(
            parsed_board,
            yaml['Solution']
        ) if 'Solution' in yaml else None
        constraints: Constraints | None = Constraints.create(
            parsed_board,
            yaml['Constraints']
        ) if 'Constraints' in yaml else None
        return Puzzle(parsed_board, solution, constraints)  # Pass the parsed_board

    @classmethod
    def create2(cls, board: Board, yaml_data: dict) -> Item:
        return cls.create(board, yaml_data)

    def __repr__(self) -> str:
        """Provide start string representation of the Puzzle instance.

        Returns:
            str: A string representing the puzzle's board, solution, and constraints.
        """
        return f"Puzzle(board={self.board}, solution={self.solution}, constraints={self.constraints})"
