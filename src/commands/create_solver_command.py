"""CreateSolverCommand."""
import logging

import pydotted

from src.commands.key_type import KeyType
from src.commands.problem import Problem
from src.commands.simple_command import SimpleCommand
from src.items.board import Board
from src.solvers.pulp_solver import PulpSolver


class CreateSolverCommand(SimpleCommand):
    """Command for creating a solver instance based on the given configuration and board."""

    def __init__(self, config: str = 'config', board: str = 'board', target: str = 'solver'):
        """Initialize a CreateSolverCommand instance.

        Args:
            config (str): The attribute in the problem containing the configuration.
            board (str): The attribute in the problem containing the board.
            target (str): The attribute name in the problem where the solver will be stored.
        """
        super().__init__()
        self.config: str = config
        self.board: str = board
        self.target: str = target
        self.input_types: list[KeyType] = [
            KeyType(self.config, pydotted.pydot),
            KeyType(self.board, Board)
        ]
        self.output_types: list[KeyType] = [
            KeyType(self.target, PulpSolver)
        ]

    def work(self, problem: Problem) -> None:
        """Build the solver and stores it in the problem instance.

        This method creates a new PulpSolver instance using the provided board and configuration,
        and stores it in the target attribute within the problem instance.

        Args:
            problem (Problem): The problem instance where the solver will be created.
        """
        super().work(problem)
        logging.info(f"Creating {self.target}")
        problem[self.target] = PulpSolver(
            board=problem[self.board],
            name=problem[self.board].title
        )
