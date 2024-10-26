import logging

from src.commands.command import CommandException
from src.commands.problem import Problem
from src.commands.simple_command import SimpleCommand
from src.solvers.pulp_solver import PulpSolver


class CreateSolverCommand(SimpleCommand):
    """
    Command for creating a solver instance based on the given configuration and board.
    """

    def __init__(self, config: str = 'config', board: str = 'board', target: str = 'solver'):
        """
        Initializes a CreateSolverCommand instance.

        Args:
            config (str): The attribute in the problem containing the configuration.
            board (str): The attribute in the problem containing the board.
            target (str): The attribute name in the problem where the solver will be stored.
        """
        super().__init__()
        self.config: str = config
        self.board: str = board
        self.target: str = target

    def precondition_check(self, problem: Problem) -> None:
        """
        Checks preconditions for command execution.

        Ensures that the config and board attributes exist in the problem and that the
        target attribute does not already exist.

        Args:
            problem (Problem): The problem instance to check.

        Raises:
            CommandException: If the config or board attributes are missing or if the
                              target attribute already exists in the problem.
        """
        if self.config not in problem:
            raise CommandException(f'{self.__class__.__name__} - {self.config} not loaded')
        if self.board not in problem:
            raise CommandException(f'{self.__class__.__name__} - {self.board} not loaded')
        if self.target in problem:
            raise CommandException(f'{self.__class__.__name__} - {self.target} already in problem')

    def execute(self, problem: Problem) -> None:
        """
        Builds the solver and stores it in the problem instance.

        This method creates a new PulpSolver instance using the provided board and configuration,
        and stores it in the target attribute within the problem instance.

        Args:
            problem (Problem): The problem instance where the solver will be created.
        """
        super().execute(problem)
        logging.info(f"Creating {self.target}")
        problem[self.target] = PulpSolver(
            board=problem[self.board],
            name=problem[self.board].title
        )

    def __repr__(self) -> str:
        """
        Returns a string representation of the CreateSolverCommand instance.

        Returns:
            str: A string representation of the object.
        """
        return f'{self.__class__.__name__}({self.config!r}, {self.board!r}, {self.target!r})'
