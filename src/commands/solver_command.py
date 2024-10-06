""" Base for different solvers """
import logging

from src.commands.command import CommandException
from src.commands.problem import Problem
from src.commands.simple_command import SimpleCommand
from src.solvers.pulp_solver import PulpSolver
from src.utils.temporary_file import TemporaryFile


class SolverCommand(SimpleCommand):

    def __init__(self):
        """ Construct a solver """
        super().__init__()

    def execute(self, problem: Problem) -> None:
        """
        Solve the puzzle.
        1. Bookkeep to remove obvious invalid choices
        2. Add any bookkeeping constraints.
        3. Solve
        4. Output the solution
        """
        super().execute(problem)
        logging.info(f"Solving problem ({problem.name}")
        with TemporaryFile() as lf:
            solver = PulpSolver(problem.board, problem.config.name, lf.name)
            solver.solve()
            problem.solution = solver.answer
            with TemporaryFile() as tf:
                solver.save(str(tf.name))
                with open(tf.name) as f:
                    problem.lp = f.read()
            with open(lf.name) as f:
                problem.log = f.read()

    def precondition_check(self, problem: Problem) -> None:
        if problem.config is None:
            raise CommandException(f'{self.__class__.__name__} - Config not loaded')
        if problem.board is None:
            raise CommandException(f'{self.__class__.__name__} - Board not built')
        if problem.constraints is None:
            raise CommandException(f'{self.__class__.__name__} - Constraints not built')