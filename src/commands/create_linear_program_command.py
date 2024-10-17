""" Produce the text in LP format for the problem.
"""
import logging

from src.commands.command import CommandException
from src.commands.problem import Problem
from src.commands.simple_command import SimpleCommand
from src.solvers.pulp_solver import PulpSolver
from src.utils.temporary_file import TemporaryFile


class CreateLinearProgramCommand(SimpleCommand):
    """ Produce LP Version of the problem. """

    def __init__(self,
                 board: str = 'board',
                 config: str = 'config',
                 constraints: str = 'constraints',
                 solver: str = 'solver',
                 target: str = 'linear_program'
                 ):
        """
        Construct a CreateLinearProgramWithBookkeepingCommand.

        :param board: The field containing the board
        :param config: The field containing the configuration
        :param constraints: The field containing the constraints
        :param solver: The field containing the solver
        :param target: The field to store the output
        """
        super().__init__()
        self.board: str = board
        self.config: str = config
        self.constraints: str = constraints
        self.solver: str = solver
        self.target = target

    def precondition_check(self, problem: Problem) -> None:
        """
        Check the preconditions for the command.

        :param problem: The problem to check
        :raises CommandException: If the preconditions are not met
        """
        if self.config not in problem:
            raise CommandException(f'{self.__class__.__name__} - {self.config} not loaded')
        if self.board not in problem:
            raise CommandException(f'{self.__class__.__name__} - {self.board} not built')
        if self.constraints not in problem:
            raise CommandException(f'{self.__class__.__name__} - {self.constraints} not built')
        if self.solver in problem:
            raise CommandException(f'{self.__class__.__name__} - {self.solver} already in problem')
        if self.target in problem:
            raise CommandException(f'{self.__class__.__name__} - {self.target} already in problem')

    def execute(self, problem: Problem) -> None:
        """
        Produce the LP version of the problem.

        This method performs the actual work of the command. It logs an info message
        indicating that the command is being processed and creates a new LP solver in the
        problem, storing it in the field specified by `self.solver`. The LP solver is then
        saved to a temporary file and the text of that file is stored in the field
        specified by `self.target`.

        Parameters:
            problem (Problem): The problem to create the LP version of.

        Returns:
            None
        """
        super().execute(problem)
        logging.info(f"Creating {self.target}")
        with TemporaryFile() as lf:
            problem[self.solver] = PulpSolver(problem[self.board], problem[self.config].name, lf.name)
            with TemporaryFile() as tf:
                problem[self.solver].save(str(tf.name))
                with open(tf.name) as f:
                    problem[self.target] = f.read()

    def __repr__(self) -> str:
        """
        Return a string representation of the object.

        Returns:
            str: A string representation of the object.
        """
        return (
            f"{self.__class__.__name__}"
            f"("
            f"{self.board!r}, "
            f"{self.config!r}, "
            f"{self.constraints!r}, "
            f"{self.solver!r}, "
            f"{self.target!r}"
            f")"
        )
