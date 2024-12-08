"""Solver Class."""
from pathlib import Path

from src.board.board import Board
from src.solvers.answer import Answer


class Solver:
    """Solver class that manages the solving of a puzzle using a given board and data representation.

    Attributes:
        board (Board): The board object representing the puzzle layout.
        answer (Answer): The data object that will store and process the solution.
    """

    def __init__(self, board: Board):
        """Initialize the Solver with a given board.

        Args:
            board (Board): The board object representing the puzzle layout.
        """
        self.board: Board = board
        self.answer: Answer = Answer(self.board)

    def save_lp(self, filename: Path | str) -> None:
        """Save the puzzle in LP (Linear Programming) format.

        Args:
            filename (Path | str): The file config_file or name where the LP format will be saved.
        """

    def save_mps(self, filename: Path | str) -> None:
        """Save the puzzle in MPS (Mathematical Programming System) format.

        Args:
            filename (Path | str): The file config_file or name where the MPS format will be saved.
        """

    def solve(self) -> None:
        """Solve the puzzle using the defined board and data objects."""
