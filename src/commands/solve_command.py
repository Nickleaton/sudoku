""" Base for different solvers """
import logging

from src.commands.command import CommandException
from src.commands.problem import Problem
from src.commands.simple_command import SimpleCommand


class SolveCommand(SimpleCommand):

    def __init__(self,
                 solver: str = 'solver',
                 target: str = 'solution',
                 log: str = 'log'):
        """
        Construct a SolveCommand.

        :param solver: The field containing the solver to use
        :param target: The field to store the solution in
        :param log: The field to store the log of the solver
        """
        super().__init__()
        self.solver = solver
        self.target = target
        self.log = log

    def precondition_check(self, problem: Problem) -> None:
        """
        Check the preconditions for the command.

        :param problem: The problem to check
        :raises CommandException: If the preconditions are not met
        """
        if self.solver not in problem:
            raise CommandException(f'{self.__class__.__name__} - {self.solver} not created')
        if self.target in problem:
            raise CommandException(f'{self.__class__.__name__} - {self.target} already in problem')
        if self.log in problem:
            raise CommandException(f'{self.__class__.__name__} - {self.log} already in problem')

    def execute(self, problem: Problem) -> None:
        """
        Solve the puzzle.

        """
        super().execute(problem)
        logging.info(f'Creating {self.solver}')
        problem[self.solver].solve()
        problem[self.target] = problem[self.solver].answer
        # Handle log

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self.solver!r}, {self.target!r}, {self.log!r})'
