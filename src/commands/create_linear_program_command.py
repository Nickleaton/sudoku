"""Produce the text in LP format for the problem."""
import logging

from src.commands.command import CommandException
from src.commands.problem import Problem
from src.commands.simple_command import SimpleCommand
from src.utils.temporary_file import TemporaryFile


class CreateLinearProgramCommand(SimpleCommand):
    """Produce the LP version of the problem."""

    def __init__(self,
                 board: str = 'board',
                 config: str = 'config',
                 constraints: str = 'constraints',
                 solver: str = 'solver',
                 target: str = 'linear_program'
                 ):
        """Initialize CreateLinearProgramCommand.

        Args:
            board (str): Field containing the board. Defaults to 'board'.
            config (str): Field containing the configuration. Defaults to 'config'.
            constraints (str): Field containing the constraints. Defaults to 'constraints'.
            solver (str): Field containing the solver. Defaults to 'solver'.
            target (str): Field to store the output. Defaults to 'linear_program'.
        """
        super().__init__()
        self.board: str = board
        self.config: str = config
        self.constraints: str = constraints
        self.solver: str = solver
        self.target: str = target

    def precondition_check(self, problem: Problem) -> None:
        """Check the preconditions for the command.

        Args:
            problem (Problem): The problem to check.

        Raises:
            CommandException: If any required field is missing or if the target field already exists.
        """
        if self.config not in problem:
            raise CommandException(f'{self.__class__.__name__} - {self.config} not loaded')
        if self.board not in problem:
            raise CommandException(f'{self.__class__.__name__} - {self.board} not built')
        if self.constraints not in problem:
            raise CommandException(f'{self.__class__.__name__} - {self.constraints} not built')
        if self.solver not in problem:
            raise CommandException(f'{self.__class__.__name__} - {self.solver} not built')
        if self.target in problem:
            raise CommandException(f'{self.__class__.__name__} - {self.target} already in problem')

    def execute(self, problem: Problem) -> None:
        """Produce the LP version of the problem.

        Logs a message indicating that the command is being processed. Creates a new LP solver
        in the problem, stores it in the field specified by `self.solver`, and saves the LP output
        to a temporary file. The text of that file is then stored in the field specified by `self.target`.

        Args:
            problem (Problem): The problem instance to create the LP version of.
        """
        super().execute(problem)
        logging.info(f"Creating {self.target}")
        with TemporaryFile() as tf:
            problem[self.solver].save_lp(str(tf.path))
            with tf.path.open(mode='r', encoding='utf-8') as f:
                problem[self.target] = f.read()

    def __repr__(self) -> str:
        """Return a string representation of the object.

        Returns:
            str: A string representation showing board, config, constraints, solver, and target.
        """
        return (
            f"{self.__class__.__name__}("
            f"{self.board!r}, "
            f"{self.config!r}, "
            f"{self.constraints!r}, "
            f"{self.solver!r}, "
            f"{self.target!r})"
        )
