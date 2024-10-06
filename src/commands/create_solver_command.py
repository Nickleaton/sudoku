""" Build Board Command """
import logging

from src.commands.command import CommandException
from src.commands.problem import Problem
from src.commands.simple_command import SimpleCommand
from src.items.board import Board


class CreateSolverCommand(SimpleCommand):

    def __init__(self):
        super().__init__()

    def execute(self, problem: Problem) -> None:
        """
        Build the board
        """
        super().execute(problem)
        logging.info("Creating Board")
        problem.board = Board.create('Board', problem.config)

    def precondition_check(self, problem: Problem) -> None:
        if problem.config is None:
            raise CommandException('config')
        if problem.board is not None:
            raise CommandException('board')

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}()"


self.board = Board.create('Board', self.parent.config.config)
self.the_problem = Item.create(self.board, {'Constraints': self.parent.config.config['Constraints']})
self.solver = PulpSolver(self.board, self.name, lf.name)
self.problem.add_constraint(self.solver)
self.problem.bookkeeping()
self.problem.add_bookkeeping_constraint(self.solver)
with TemporaryFile() as tf:
    self.solver.save(str(tf.name))
    with open(tf.name) as f:
        self.output = f.read()