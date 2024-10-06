""" Produce the text in LP format for the problem.
"""
from typing import Optional

from src.commands.command import CommandException
from src.commands.problem import Problem
from src.commands.simple_command import SimpleCommand
from src.items.board import Board
from src.items.item import Item
from src.solvers.pulp_solver import PulpSolver
from src.utils.config import Config
from src.utils.temporary_file import TemporaryFile

config = Config()


class CreateLPCommand(SimpleCommand):
    """ Produce LP Version of the problem"""

    def __init__(self, bookkeeping: bool = False) -> None:
        super().__init__()

    def execute(self, problem: Problem) -> None:
        super().execute(problem)
        with TemporaryFile() as lf:
            problem.solver = PulpSolver(problem.board, problem.config.name, lf.name)
            with TemporaryFile() as tf:
                problem.solver.save(str(tf.name))
                with open(tf.name) as f:
                    problem.linear_program = f.read()


    def precondition_check(self, problem: Problem) -> None:
        if problem.config is None:
            raise CommandException(f'{self.__class__.__name__} - Config not loaded')
        if problem.board is None:
            raise CommandException(f'{self.__class__.__name__} - Board not built')
        if problem.constraints is None:
            raise CommandException(f'{self.__class__.__name__} - Constraints not built')


    def __repr__(self) -> str:
        return f'{self.__class__.__name__}()'